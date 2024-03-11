from cv2 import VideoCapture, cvtColor, COLOR_BGR2RGB
from typing import Any
from PySide6.QtCore import QObject, QThread, Signal, Slot
from networkx import is_regular
from numpy import ndarray
from data_queue import DataQueue
from testing import VERBOSE
import time

class FrameGrabber(QObject):
        error = Signal(tuple)
        fps = Signal(tuple)
        main_output_stream = Signal(tuple)
        finished = Signal() # connects to thread quit
        
        def __init__(self) -> None:
                super().__init__()
                self.media_source: int | str = 0
                self.cap: VideoCapture = VideoCapture(self.media_source)
                print("Frame Grabber ready")
                
        @Slot(Any)
        def reload(self, media_source: int | str):
                self.media_source = media_source
                self.cap.release()
                self.cap: VideoCapture = VideoCapture(self.media_source)
                
        @Slot()
        def main_function(self):
                self.cap: VideoCapture = VideoCapture(self.media_source)
                while not self.thread().isInterruptionRequested():
                        start = time.time()
                        ok, frame = self.cap.read()
                        if not ok:
                                self.error.emit(f"Frame Grabber failed to get more frames", {self.objectName()})
                                break
                        frame = cvtColor(frame, COLOR_BGR2RGB)
                        self.main_output_stream.emit((frame, self.objectName()))
                        self.fps.emit((1/(time.time()-start)))
                self.cap.release()
                print(f"{self.objectName()} stopped") if VERBOSE else ...
