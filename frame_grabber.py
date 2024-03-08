from cv2 import VideoCapture, cvtColor, COLOR_BGR2RGB
from PySide6.QtCore import QObject, QThread


class FrameGrabber(QThread):
        def __init__(self, queue, parent: QObject | None = None) -> None:
                super().__init__(parent)
                self.media_source: int | str = 0
                self.cap: VideoCapture = VideoCapture(self.media_source)
                self.queue: MessageQueue = queue

        def run(self) -> None:
                ok, frame = self.cap.read()
                if not ok:
                        print("Frame Grabber failed to get more frames")
                frame = cvtColor(frame, COLOR_BGR2RGB)
                self.queue.put(item=frame)

if __name__=="__main__":
        from data_queue import MessageQueue
        mq = MessageQueue()
        fg = FrameGrabber(mq)
        fg.start()
        while True:
                print('....')
                print(mq.get())
