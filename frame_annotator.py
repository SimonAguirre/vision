from numpy import ndarray
from PySide6.QtCore import QObject

from supervision import Detections, BoundingBoxAnnotator, LabelAnnotator, TraceAnnotator, draw_polygon, PolygonZone, ColorPalette
from supervision.draw.color import Color, ColorPalette
from supervision.geometry.core import Position

from cv2.typing import MatLike
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtGui import QImage
from supervision import Detections
import numpy as np
from constants import Purpose
from typing import Any
import math
Any = type(Any)


class Annotator(QObject):
        read_from_queue = Signal(str) # request
        write_to_queue = Signal(tuple)
        score = 0
        def __init__(self):
                super().__init__()
                self.box_annotator = BoundingBoxAnnotator()
                self.label_annotator = LabelAnnotator()
                self.trace_annotator = TraceAnnotator()
                
                thickness = 1
                scale = 0.5

                self.thickness: int = thickness
                self.scale: float = scale
                
                
                self.model_detection_size = (853, 480)
                self.playback_size = (1920, 1080)
                self.zone_polygons = [[[0.0077, 0.975],[0.2446, 0.5229],[0.4738, 0.5104],[0.4892, 0.9646]],
                                                                [[0.5031, 0.4958],[0.7338, 0.4917],[0.9954, 0.9917],[0.4969, 0.9604]]]
                self.COLORS = ColorPalette.default()
                self.detection_zones = self.initialize_detection_zones(self.zone_polygons, self.playback_size)

        def _request_data(self):
                """Request frame from tracking queue"""
                sender = self.objectName()
                self.read_from_queue.emit(sender)
                
        def _track(self, data: tuple[MatLike, Detections, list]):
                frame, detections, class_names = data
                class_names = dict(class_names)
                
                # prepare labels
                labels = [
                                f"#{tracker_id} {class_names[class_id]} {confidence:0.2f}"
                                for _, _, confidence, class_id, tracker_id, _
                                in detections]
                
                # reshape detections to match playbaack shape
                detections_xyxy = detections.xyxy
                for index, xyxy in enumerate(detections_xyxy):
                                x1, y1, x2, y2 = xyxy
                                x1 = x1/self.model_detection_size[0]*self.playback_size[0]
                                x2 = x2/self.model_detection_size[0]*self.playback_size[0]
                                y1 = y1/self.model_detection_size[1]*self.playback_size[1]
                                y2 = y2/self.model_detection_size[1]*self.playback_size[1]
                                detections.xyxy[index] = np.array([x1,y1,x2,y2], dtype=np.float32)
                                
                # draw bounding boxes
                annotated_frame =  self.box_annotator.annotate(
                                scene=frame, detections=detections)
                
                # draw labels
                annotated_frame = self.label_annotator.annotate(
                                scene = annotated_frame, detections = detections, labels = labels)
                
                # draw detection zones
                for detection_zones in self.detection_zones:
                        annotated_frame = draw_polygon(
                                                annotated_frame, detection_zones.polygon, self.COLORS.colors[0])
                
                # draw traces
                annotated_frame = self.trace_annotator.annotate(annotated_frame, detections)
                
                # convert to QImage
                h, w, ch = annotated_frame.shape
                image = QImage(annotated_frame.data, w, h, ch * w, QImage.Format.Format_RGB888)
                
                sender = self.objectName()
                purpose = Purpose.RESTART_CYCLE
                self.write_to_queue.emit((sender, purpose, image))
                self.score += 1
        
        @staticmethod
        def initialize_detection_zones(polygon_zones, frame_resolution_wh, triggering_position = Position.BOTTOM_CENTER):
                polygon_zones = [np.array([math.ceil(point[0]*frame_resolution_wh[0]), math.ceil(point[1]*frame_resolution_wh[1])]) for polygon in polygon_zones for point in polygon]
                detection_zone = [PolygonZone(polygon, frame_resolution_wh,  triggering_position) for polygon in polygon_zones]
                return detection_zone
                                                                                                
        def _initilize_annotators(self, data):
                """Initialize annotators used for frame annotations"""
                
        
        def _update_annotation_params(self, data):
                """Update annotation parameters
                params:
                        - data: tuple of (line_thickness, text_scale, )
                """
                self.iou, self.conf = data
                
        @Slot(tuple)
        def handle_received_data(self, pack):
                """Validate data received and call the appropriate function to process the data"""
                try:
                        target, purpose, data = pack
                except:
                        print(f"{self.objectName()} can't parse data passed to slot -> {pack}")
                if not (target == self.objectName() or target == "all"):
                        return
                if purpose == Purpose.CONTINUE_PROCESS:
                        self._annotate(data)
                elif purpose == Purpose.RESTART_CYCLE:
                        if not self.thread().isInterruptionRequested():
                                self._request_data()
                elif purpose == Purpose.UPDATE_PARAMETERS:
                        self._update_tracking_params(data)
                elif purpose == Purpose.INITIALIZE:
                        self._initilize_tracker(data)
                        
                        
        def run(self):
                print(f"{self.objectName()} started")
                while True:
                        data = self.in_queue.get()
                        frame: MatLike = data[0]
                        detections: Detections = data[1]
                        class_names = dict(data[2])
                        del data
                        labels = [
                                f"#{tracker_id} {class_names[class_id]} {confidence:0.2f}"
                                for _, _, confidence, class_id, tracker_id, _
                                in detections]
                        del class_names
                        annotated_frame = self.box_annotator.annotate(
                                scene=frame,
                                detections=detections)
                        del frame
                        annotated_labeled_frame = self.label_annotator.annotate(
                                        scene=annotated_frame, 
                                        detections=detections,
                                        labels = labels
                                )
                        del annotated_frame
                        self.out_queue.put((annotated_labeled_frame))