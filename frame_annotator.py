from supervision import BoundingBoxAnnotator, LabelAnnotator
from PySide6.QtCore import QObject, QThread
from data_queue import DataQueue
from supervision import Detections
from cv2.typing import MatLike
import time

class Annotator(QThread):
        def __init__(self, in_queue: DataQueue, out_queue: DataQueue,
                thickness = 1, scale = 0.5,
                parent: QObject | None = None) -> None:
                super().__init__(parent)
                self.box_annotator = BoundingBoxAnnotator()
                self.label_annotator = LabelAnnotator()
                self.in_queue: DataQueue = in_queue
                self.out_queue: DataQueue = out_queue
                self.thickness: int = thickness
                self.scale: float = scale
                self.is_running: bool = True
                print("Annotator ready")
                
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