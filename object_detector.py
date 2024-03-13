from PySide6.QtCore import QObject, Signal, Slot
from ultralytics import YOLO
from  ultralytics.engine.results import Results
from supervision import Detections
from cv2.typing import MatLike

from testing import print_
from typing import Any
Any = type(Any)

class ObjectDetector(QObject):
        error = Signal(tuple)
        fps = Signal(tuple)
        put_data = Signal(tuple)
        get_data = Signal(str) # request
        finished = Signal() # connects to thread quit

        def __init__(self):
                super().__init__()
                self.model: YOLO | None = None
                self.iou: float | None = None
                self.conf: float | None = None

        def initilize_model(self, data):
                self.model_file, self.iou, self.conf = data
                self.model = YOLO(self.model_file)

        def reload_worker(self, media_source: int | str, 
                          iou: float, confidence: float):
                pass

        @Slot(Any)
        def handle_recieved_data(self, data):
                data, purpose = data
                if purpose == 'initialize model':
                        self.initilize_model(data)
                else:
                        frame = data
                        results: Results = self.model(frame,verbose=False,conf=self.conf,iou=self.iou)[0]
                        detections: Detections = Detections.from_ultralytics(results)
                        class_names: list[str] = self.model.names
                        self.put_data.emit((frame, detections, class_names))


        @Slot()
        def main_function(self):
                
                        self.get_data.emit("get raw frames")

