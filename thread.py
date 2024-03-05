
from ultralytics import YOLO

import supervision as sv

import os
import sys
import time

import cv2
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QImage


class Thread(QThread):
        updateFrame = Signal(QImage)
        tracker = sv.ByteTrack()
        box_annotator = sv.BoundingBoxAnnotator()
        label_annotator = sv.LabelAnnotator()
        verbose = False
        
        def __init__(self, parent=None, **kwargs):
                QThread.__init__(self, parent)
                self.trained_file = None        # Weights
                self.status = True              # Inference status
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
        
        def draw_fps(self, frame, start_time):
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

                return cv2.putText(frame, f"FPS: {fps:0.2f}", (10, 30), font, 1, fps_color, 2, cv2.LINE_AA)

        def run(self):
                self.cap = cv2.VideoCapture(self.media_source)
                self.fps_list = []
                while self.status: 
                        start_time = time.time()
                        # cascade = cv2.CascadeClassifier(self.trained_file)
                        ret, frame = self.cap.read()
                        if not ret:
                                print("Video frames exhausted...")
                                break

                        frame=cv2.resize(frame,(1280,720))

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
                        scaled_img = img.scaled(1280, 720, Qt.KeepAspectRatio)

                        # Emit signal
                        self.updateFrame.emit(scaled_img)
                        
                        if self.verbose:
                                print(f"Inference: {(time.time()-start_time)*1000:0.3f} ms | {(1/(time.time()-start_time)):0.2f} fps")
                sys.exit(-1)

        
                
