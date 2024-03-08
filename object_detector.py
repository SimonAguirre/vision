from PySide6.QtCore import QObject, QThread
from ultralytics import YOLO
from  ultralytics.engine.results import Results
from supervision import Detections
class ObjectDetector(QThread):
        def __init__(self, in_queue, out_queue,
                     model_file: str = './models/best.pt',
                     confidence_threshold: float = 0.5,
                     iou_threshold: float = 0.7,
                     parent: QObject | None = None) -> None:
                super().__init__(parent)
                self.in_queue: MessageQueue = in_queue
                self.out_queue: MessageQueue = out_queue
                self.model = YOLO(model_file)
                self.conf = confidence_threshold
                self.iou = iou_threshold

        def run(self):
                frame = self.in_queue.get()
                results: Results = self.model(
                                frame,
                                verbose=False,
                                conf=self.conf, 
                                iou=self.iou
                        )[0]
                detections = Detections.from_ultralytics(results)
                self.out_queue.put(detections)

if __name__=="__main__":
        from data_queue import MessageQueue
        from frame_grabber import FrameGrabber

        iq = MessageQueue()
        oq = MessageQueue()

        fg = FrameGrabber(iq)
        fg.start()

        od = ObjectDetector(iq, out_queue=oq)
        od.start()

        print('....')
        print(iq.get())
        print(oq.get())
