
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
from supervision.geometry.core import Position
from testing import verbose

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
                text_position = Position.BOTTOM_LEFT
        )
        trace_annotator = sv.TraceAnnotator()
        
        def __init__(self):
                QThread.__init__(self)
                self.trained_file = None
                self.status = True
                self.cap = True                 
                self.confidence = 0.55
                self.iou = 0.55
                self.model = None
                self.media_source = 0
                self.detection_zone = [[0,0],[0,0],[0,0],[0,0]]
                self.frame_size = (853,480)
                self.display_size = (1920,1080)
                self.COLORS = sv.ColorPalette.default()

        @staticmethod
        def initialize_polygon_zone(polygon, frame_resolution_wh, triggering_position = Position.BOTTOM_CENTER):
                polygon = [[math.ceil(point[0]*frame_resolution_wh[0]), math.ceil(point[1]*frame_resolution_wh[1])] for point in polygon]
                polygon = np.array(polygon)
                return sv.PolygonZone(polygon, frame_resolution_wh,  triggering_position)

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

                return cv2.putText(frame, f"FPS: {fps:0.2f}", (10, 30), font, self.text_scale, fps_color, self.text_thickness, cv2.LINE_AA)

        def run(self):
                self.cap = cv2.VideoCapture(self.media_source)
                self.fps_list = []
                # self.frame_size = (round(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)), round(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
                self.box_thickness = math.ceil(self.display_size[0]/(640*2))
                self.text_scale = self.display_size[0]/(1280*2)
                self.text_thickness = math.ceil(self.display_size[0]/(640*2))
                self.text_padding = math.ceil(self.display_size[0]*5*self.text_scale/(640*2))
                self.box_annotator.thickness = self.box_thickness
                self.label_annotator.text_scale = self.text_scale
                self.label_annotator.text_thickness = self.text_thickness
                self.label_annotator.text_padding = self.text_padding
                print(f"Updated: box_thickness {self.box_annotator.thickness}, text_scale {self.label_annotator.text_scale}, text_thickness {self.label_annotator.text_thickness}, text_padding {self.label_annotator.text_padding}")
                
                self.zones_in = self.initialize_polygon_zone(self.detection_zone, self.display_size, sv.Position.CENTER)
                
                while self.status: 
                        start_time = time.time()
                        # cascade = cv2.CascadeClassifier(self.trained_file)
                        ret, frame = self.cap.read()
                        
                        if not ret:
                                print("Video frames exhausted...")
                                break

                        frame_orig = frame.copy()

                        frame_orig = cv2.resize(frame_orig, self.display_size)


                        frame = cv2.resize(frame,self.frame_size)
                        # Reading the image in RGB to display it
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                        results = self.model(
                                frame,
                                verbose=False,
                                conf=self.confidence, 
                                iou=self.iou
                        )[0]

                        detections = sv.Detections.from_ultralytics(results)
                        detections = self.tracker.update_with_detections(detections)
                        detections_xyxy = detections.xyxy
                        # print(f"{detections_xyxy[0]} -> type {type(detections_xyxy[0][0])}")
                        # break
                        for index, xyxy in enumerate(detections_xyxy):
                                x1, y1, x2, y2 = xyxy
                                x1 = x1/self.frame_size[0]*self.display_size[0]
                                x2 = x2/self.frame_size[0]*self.display_size[0]
                                y1 = y1/self.frame_size[1]*self.display_size[1]
                                y2 = y2/self.frame_size[1]*self.display_size[1]
                                detections.xyxy[index] = np.array([x1,y1,x2,y2], dtype=np.float32)


                        # draw bounding boxes
                        annotated_frame = self.box_annotator.annotate(
                                scene=frame_orig,
                                detections=detections
                        )

                        # draw detection zones
                        annotated_frame = sv.draw_polygon(
                                        annotated_frame, self.zones_in.polygon, self.COLORS.colors[0]
                        )

                        # draw traces
                        annotated_frame = self.trace_annotator.annotate(annotated_frame, detections)
                        
                        # init labels
                        labels = [
                                f"#{tracker_id} {self.CLASS_NAMES_DICT[class_id]} {confidence:0.2f}"
                                for _, _, confidence, class_id, tracker_id, _
                                in detections
                        ]

                        # draw class labels
                        annotated_labeled_frame = self.label_annotator.annotate(
                                scene=annotated_frame, 
                                detections=detections,
                                labels = labels
                        )
                                
                        # Get and draw FPS
                        final_frame = self.draw_fps(annotated_labeled_frame.copy(), start_time)

                        # Creating and scaling QImage
                        h, w, ch = final_frame.shape
                        img = QImage(final_frame.data, w, h, ch * w, QImage.Format_RGB888)
                        # scaled_img = img.scaled(self.frame_size[0], self.frame_size[1], Qt.KeepAspectRatio)

                        # Emit signal
                        self.updateFrame.emit(img)
                        
                        if verbose:
                                print(f"Inference: {(time.time()-start_time)*1000:0.3f} ms | {(1/(time.time()-start_time)):0.2f} fps")
                sys.exit(-1)

        
                
