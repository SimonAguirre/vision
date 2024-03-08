from PySide6.QtCore import QObject, QThread
from supervision import ByteTrack

class Tracker(QThread):
        def __init__(self, in_queue, out_queue,
                     parent: QObject | None = None) -> None:
                super().__init__(parent)
                self.in_queue: MessageQueue = in_queue
                self.out_queue: MessageQueue = out_queue
                self.tracker = ByteTrack()

        def run(self):
                detections = self.in_queue.get()
                detections = self.tracker.update_with_detections(detections)
                self.out_queue.put(detections)

if __name__=="__main__":
        from data_queue import MessageQueue
        from frame_grabber import FrameGrabber
        from object_detector import ObjectDetector

        import time

        iq = MessageQueue()
        detq = MessageQueue()
        traq = MessageQueue()

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
