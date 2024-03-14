from PySide6.QtCore import QObject, Signal, Slot
from ultralytics import YOLO
from  ultralytics.engine.results import Results
from supervision import Detections

from constants import Purpose
from typing import Any
Any = type(Any)

class ObjectDetector(QObject):
        read_from_queue = Signal(str) # request
        write_to_queue = Signal(tuple)
        score = 0
        def __init__(self):
                super().__init__()
                self.model: YOLO = YOLO("./models/best_from_past_research.pt")
                self.iou: float = 0.55
                self.conf: float = 0.7
                self.is_inferencing: bool = False

        def _request_data(self):
                """Request frame from queue"""
                if self.model == None:
                        print("No model selected!")
                        return
                sender = self.objectName()
                self.read_from_queue.emit(sender)

        def _detect(self, data):
                """Run inference on the frame and emit the result to detections queue"""
                frame = data
                results: Results = self.model(frame,verbose=False,conf=self.conf,iou=self.iou)[0]
                detections: Detections = Detections.from_ultralytics(results)
                class_names: list[str] = self.model.names
                sender = self.objectName()
                purpose = Purpose.RESTART_CYCLE
                data = (frame, detections, class_names)
                self.write_to_queue.emit((sender, purpose, data))
                self.score += 1
        
        def _initilize_model(self, data):
                """Initialize model used for object detection"""
                self.model_file, self.iou, self.conf = data
                self.model = YOLO(self.model_file)

        def _update_detection_params(self, data):
                """Update detection parameters
                params:
                        - data: tuple of (iou threshold, confidence threshold)
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
                        self._detect(data)
                elif purpose == Purpose.RESTART_CYCLE:
                        if not self.thread().isInterruptionRequested():
                                self._request_data()
                elif purpose == Purpose.UPDATE_PARAMETERS:
                        self._update_detection_params(data)
                elif purpose == Purpose.INITIALIZE:
                        self._initilize_model(data)