from cv2 import VideoCapture, cvtColor, COLOR_BGR2RGB
from typing import Any
from PySide6.QtCore import QObject, Signal, Slot
from numpy import ndarray
import time

from pyparsing import deque

from testing import print_
Any = type(Any)

class FrameGrabber(QObject):
        write_queue = Signal(tuple)
        stopped = Signal() # connects to thread quit

        def __init__(self) -> None:
                super().__init__()
                self.media_source: int | str = 0
                self.cap: VideoCapture = VideoCapture(self.media_source)
        
        @Slot(Any)
        def update_config(self, config):
                self.media_source = config
                self.cap.release()
                self.cap: VideoCapture = VideoCapture(self.media_source)

        @Slot()
        def main_function(self):
                self.cap: VideoCapture = VideoCapture(self.media_source)
                while not self.thread().isInterruptionRequested():
                        # start = time.time()
                        ok, frame = self.cap.read()
                        if not ok:
                                # self.error.emit(f"Frame Grabber failed to get more frames", {self.objectName()})
                                print(f"Add error handling in {self.objectName()}")
                                break
                        frame = cvtColor(frame, COLOR_BGR2RGB)
                        self.write_queue.emit((frame, self.objectName()))
                        # self.fps.emit((1/(time.time()-start)))
                self.cap.release()
                print(f"{self.objectName()} stopped")
