from supervision import BoundingBoxAnnotator, LabelAnnotator
from PySide6.QtCore import QObject, QThread
from data_queue import DataQueue
from supervision import Detections
from cv2.typing import MatLike
from testing import VERBOSE
import time
from ast import Raise
from PySide6.QtCore import QObject, Signal, Slot
from supervision import Detections

import time
from constants import Purpose
from typing import Any
Any = type(Any)


class Annotator(QThread):
        read_from_queue = Signal(str) # request
        write_to_queue = Signal(tuple)
        score = 0
        def __init__(self):
                super().__init__()
                self.box_annotator = BoundingBoxAnnotator()
                self.label_annotator = LabelAnnotator()

        def _request_data(self):
                """Request frame from queue"""
                sender = self.objectName()
                self.read_from_queue.emit(sender)
                thickness = 1
                scale = 0.5

                self.thickness: int = thickness
                self.scale: float = scale
        
        def _initilize_annotators(self, data):
                """Initialize annotators used for frame annotations"""
        
        def _update_annotation_params(self, data):
                """Update annotation parameters
                params:
                        - data: tuple of (line_thickness, text_scale, )
                """
                self.iou, self.conf = data

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
        
        def stop(self, caller: str):
                self.is_running = False
                print(f"{caller} requested to stop {str(self).split('.')[1]}") if VERBOSE else ...
                time.sleep(0.2)
                self.terminate()
                
if __name__=="__main__":
        from data_queue import DataQueue