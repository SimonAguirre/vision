import cv2
from numpy import ndarray
from PySide6.QtCore import QObject

from supervision import (Detections, PolygonZone, ColorPalette,
                        BoxCornerAnnotator, LabelAnnotator, TraceAnnotator,
                        draw_polygon, calculate_dynamic_line_thickness,
                        calculate_dynamic_text_scale)
from supervision.draw.color import Color, ColorPalette
from supervision.geometry.core import Position
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtGui import QImage
from supervision import Detections
import numpy as np
from pipeline.constants import Purpose
from typing import Any
Any = type(Any)


class Annotator(QObject):
        read_from_queue = Signal(str) # request
        write_to_queue = Signal(tuple)
        status_update = Signal(tuple)
        fps = 0
        score = 0
        def __init__(self):
                super().__init__()
                self.playback_wh: tuple = (int(1920), int(1080))

                self.line_thickness = calculate_dynamic_line_thickness(resolution_wh=self.playback_wh)
                self.text_scale = calculate_dynamic_text_scale(resolution_wh=self.playback_wh)

                self.box_annotator = BoxCornerAnnotator(thickness=self.line_thickness,
                                                        corner_length=round(self.line_thickness*4))
                self.label_annotator = LabelAnnotator(text_scale=self.text_scale,
                                                        text_thickness=self.line_thickness,
                                                        text_position=Position.BOTTOM_CENTER,)
                self.trace_annotator = TraceAnnotator(thickness=self.line_thickness,
                                                        # trace_length=video_info.fps * 2,
                                                        trace_length=20,
                                                        position=Position.BOTTOM_CENTER)
                
                self.zone_polygons = [[[0.0077, 0.975],[0.2446, 0.5229],[0.4738, 0.5104],[0.4892, 0.9646]],
                                                                [[0.5031, 0.4958],[0.7338, 0.4917],[0.9954, 0.9917],[0.4969, 0.9604]]]
                
                self.COLORS = ColorPalette.default()
                self.detection_zones = self.initialize_detection_zones(self.zone_polygons, self.playback_wh)

        def _request_data(self):
                """Request frame from tracking queue"""
                sender = self.objectName()
                self.read_from_queue.emit(sender)
                
        def _annotate(self, data: tuple[ndarray, Detections, dict]):
                frame, detections, class_names = data
                # prepare labels
                labels = [
                                f"id:{tracker_id} {class_names[class_id]} {confidence:0.2f}"
                                for _, _, confidence, class_id, tracker_id, _
                                in detections]
                if not self.playback_wh == frame.shape[:2]:
                        frame = cv2.resize(frame, self.playback_wh)
                        # reshape detections to match playbaack shape
                        detections_xyxy = detections.xyxy
                        for index, xyxy in enumerate(detections_xyxy):
                                        x1, y1, x2, y2 = xyxy
                                        x1 = x1/frame.shape[0]*self.playback_wh[0]
                                        x2 = x2/frame.shape[0]*self.playback_wh[0]
                                        y1 = y1/frame.shape[1]*self.playback_wh[1]
                                        y2 = y2/frame.shape[1]*self.playback_wh[1]
                                        detections.xyxy[index] = np.array([x1,y1,x2,y2], dtype=np.float32)
                
                # draw corner boxes
                annotated_frame =  self.box_annotator.annotate(
                                scene=frame, detections=detections)
                # draw labels
                annotated_frame = self.label_annotator.annotate(
                                scene = annotated_frame, detections = detections, labels = labels)
                # draw traces
                # annotated_frame = self.trace_annotator.annotate(annotated_frame, detections)

                # draw detection zones
                annotated_frame = draw_polygon(annotated_frame,
                                                                self.detection_zones.polygon, self.COLORS.colors[0])
                # for index, detection_zones in enumerate(self.detection_zones):
                #         annotated_frame = draw_polygon(
                #                                 annotated_frame,
                #                                 detection_zones.polygon, self.COLORS.colors[-(index+1)])
                        
                # convert to QImage
                h, w, ch = annotated_frame.shape
                image = QImage(annotated_frame.data, w, h, ch * w, QImage.Format.Format_RGB888)
                sender = self.objectName()
                purpose = Purpose.RESTART_CYCLE
                self.write_to_queue.emit((sender, purpose, image))
                self.score += 1
        
        @staticmethod
        def initialize_detection_zones(polygon_zones, frame_resolution_wh, triggering_position = Position.BOTTOM_CENTER):
                for index, polygon in enumerate(polygon_zones):
                        polygon_zones[index] = [[round(point[0]*frame_resolution_wh[0]), round(point[1]*frame_resolution_wh[1])] for point in polygon]
                polygon_zones = np.array(polygon_zones)
                detection_zone = PolygonZone(polygon_zones[0], frame_resolution_wh,  triggering_position)
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
                target, purpose, data = pack
                if not (target == self.objectName() or target == "all"):
                        return
                if purpose == Purpose.CONTINUE_PROCESS:
                        self._annotate(data)
                elif purpose == Purpose.RESTART_CYCLE:
                        if not self.thread().isInterruptionRequested():
                                self._request_data()
                elif purpose == Purpose.UPDATE_PARAMETERS:
                        self._update_annotation_params(data)
                elif purpose == Purpose.INITIALIZE:
                        self._initilize_annotators(data)

        @Slot()
        def status_request_handler(self):
                self.status_update.emit((self.objectName(), Purpose.STATUS_UPDATE, {"fps" : self.fps, "score" : self.score}))