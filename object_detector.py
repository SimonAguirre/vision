from PySide6.QtCore import QObject, QThread
from cv2 import Mat
from ultralytics import YOLO
from  ultralytics.engine.results import Results
from supervision import Detections
from data_queue import DataQueue
from cv2.typing import MatLike
from testing import VERBOSE

class ObjectDetector(QObject):
        def __init__(self, in_queue: DataQueue, out_queue: DataQueue,
                model_file: str = './models/best.pt',
                confidence_threshold: float = 0.5,
                iou_threshold: float = 0.7,
                parent: QObject | None = None) -> None:
                
                super().__init__(parent)
                self.in_queue: DataQueue = in_queue
                self.out_queue: DataQueue = out_queue
                self.model = YOLO(model_file)
                self.conf: float = confidence_threshold
                self.iou: float = iou_threshold
                print("Detector ready")

        def run(self):
                count = 0
                while True:
                        count +=1
                        frame: MatLike = self.in_queue.get()
                        results: Results = self.model(frame,verbose=False,conf=self.conf,iou=self.iou)[0]
                        detections: Detections = Detections.from_ultralytics(results)
                        class_names: list[str] = self.model.names
                        self.out_queue.put((frame, detections, class_names))
                        print(f"Successfuly put item {count} to detections queue") if VERBOSE else ...

if __name__=="__main__":
        from data_queue import DataQueue
        from frame_grabber import FrameGrabber

        iq = DataQueue()
        oq = DataQueue()

        fg = FrameGrabber(iq)
        fg.start()

        od = ObjectDetector(iq, out_queue=oq)
        od.start()

        print('....')
        print(iq.get())
        print(oq.get())
