
from ultralytics import YOLO

import supervision as sv

import os
import sys
import time
import math
import numpy as np

import cv2
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QImage
from supervision.draw.color import Color, ColorPalette

class Thread(QThread):
        box_thickness = 2
        text_scale = 1
        text_thickness = 2
        text_padding = 10
        
        updateFrame = Signal(QImage)
        tracker = sv.ByteTrack()
        box_annotator = sv.BoundingBoxAnnotator(
                thickness=box_thickness
        )
        label_annotator = sv.LabelAnnotator(
                text_scale = text_scale,
                text_thickness = text_thickness,
                text_padding = text_padding,
        )
        verbose = False
        
        def __init__(self, parent=None, **kwargs):
                QThread.__init__(self, parent)
                self.trained_file = None
                self.status = True
                self.cap = True                 
                self.confidence = ...
                self.iou = ...
                self.model = None
                self.media_source = 0
                
                try:
                        self.verbose = kwargs['verbose']
                except:
                        pass
                
        def set_file(self, fname):
                # The data comes with the 'opencv-python' module
                assert fname, "No Model Selected"
                self.trained_file = fname
                print(f"getting model: {self.trained_file}")
                self.model = YOLO(os.path.join("./models",self.trained_file))
                self.CLASS_NAMES_DICT = dict(self.model.model.names)
        
        def set_media_source(self, source):
                self.media_source = source
        
        def draw_fps(self, frame, start_time) -> cv2.typing.MatLike:
                font = cv2.FONT_HERSHEY_SIMPLEX
                
                fps = 1/(time.time()-start_time)
                self.fps_list.append(fps)
                
                if len(self.fps_list) == 15:
                        fps_sum = 0
                        for i in self.fps_list:
                                fps_sum += i
                        self.fps_list.pop(0)
                        fps = fps_sum/15
                        
                if fps <= self.cap.get(cv2.CAP_PROP_FPS):
                        fps_color = (255, 0, 0)
                else:
                        fps_color = (100, 255, 0)

                return cv2.putText(frame, f"FPS: {fps:0.2f}", (self.text_padding, int(self.text_padding*3)), font, self.text_scale, fps_color, self.text_thickness, cv2.LINE_AA)

        def run(self):
                self.cap = cv2.VideoCapture(self.media_source)
                self.fps_list = []
                frame_width = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
                self.box_thickness = math.ceil(frame_width/500)
                self.text_scale = math.ceil(self.box_thickness/3)
                self.text_thickness = math.ceil(self.box_thickness/2)
                self.text_padding = math.ceil(self.text_scale*10)
                self.box_annotator.thickness = self.box_thickness
                self.label_annotator.text_scale = self.text_scale
                self.label_annotator.text_thickness = self.text_thickness
                self.label_annotator.text_padding = self.text_padding
                print(f"Updated: box_thickness {self.box_annotator.thickness}, text_scale {self.label_annotator.text_scale}, text_thickness {self.label_annotator.text_thickness}, text_padding {self.label_annotator.text_padding}")
                while self.status: 
                        start_time = time.time()
                        # cascade = cv2.CascadeClassifier(self.trained_file)
                        ret, frame = self.cap.read()
                        if not ret:
                                print("Video frames exhausted...")
                                break

                        frame=cv2.resize(frame,(853,480))

                        results = self.model(
                                frame,
                                verbose=False,
                                conf=self.confidence, 
                                iou=self.iou
                        )[0]
                        detections = sv.Detections.from_ultralytics(results)
                        detections = self.tracker.update_with_detections(detections)
                        
                        annotated_frame = self.box_annotator.annotate(
                                scene=frame.copy(),
                                detections=detections
                        )
                             
                        labels = [
                                f"#{tracker_id} {self.CLASS_NAMES_DICT[class_id]} {confidence:0.2f}"
                                for _, _, confidence, class_id, tracker_id, _
                                in detections
                        ]
                        
                        annotated_labeled_frame = self.label_annotator.annotate(
                                scene=annotated_frame, 
                                detections=detections,
                                labels = labels
                        )
                        
                        # Reading the image in RGB to display it
                        color_frame = cv2.cvtColor(annotated_labeled_frame, cv2.COLOR_BGR2RGB)
                                
                        # Get and draw FPS
                        color_frame = self.draw_fps(color_frame, start_time)

                        # Creating and scaling QImage
                        h, w, ch = color_frame.shape
                        img = QImage(color_frame.data, w, h, ch * w, QImage.Format_RGB888)
                        scaled_img = img.scaled(853, 480, Qt.KeepAspectRatio)

                        # Emit signal
                        self.updateFrame.emit(scaled_img)
                        
                        if self.verbose:
                                print(f"Inference: {(time.time()-start_time)*1000:0.3f} ms | {(1/(time.time()-start_time)):0.2f} fps")
                sys.exit(-1)

        
                
