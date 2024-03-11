from PySide6.QtCore import QObject, QThread
from supervision import ByteTrack
from data_queue import DataQueue
from supervision import Detections
from cv2.typing import MatLike
import cv2

class Tracker(QThread):
        def __init__(self, in_queue: DataQueue, out_queue: DataQueue, 
                parent: QObject | None = None) -> None:
                super().__init__(parent)
                self.in_queue: DataQueue = in_queue
                self.out_queue: DataQueue = out_queue
                self.tracker = ByteTrack()
                print("Tracker ready")

        def run(self):
                data = self.in_queue.get()
                frame: MatLike = data[0]
                detections: Detections = data[1]
                class_names: list[str] = data[2]
                del data
                detections = self.tracker.update_with_detections(detections)
                self.out_queue.put((frame, detections, class_names))

if __name__=="__main__":
        from data_queue import DataQueue
        from frame_grabber import FrameGrabber
        from object_detector import ObjectDetector

        import time

        iq = DataQueue()
        detq = DataQueue()
        traq = DataQueue()

        fg = FrameGrabber(iq)
        od = ObjectDetector(iq, detq)
        ot = Tracker(detq,traq)

        fg.start()
        print(iq.empty())
        # od.start()
        print(detq.empty())
        # ot.start()
        print(traq.empty())
        time.sleep(1)
        print(iq.empty())

        # print(iq.get())
        # print(detq.get())
        # print(traq.get())
