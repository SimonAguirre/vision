from cv2 import VideoCapture, cvtColor, COLOR_BGR2RGB
from typing import Any
from PySide6.QtCore import QObject, Signal, Slot
from numpy import ndarray
import time

from pyparsing import deque
from constants import Purpose
from testing import print_
Any = type(Any)

class FrameGrabber(QObject):
        write_to_queue = Signal(tuple)

        def __init__(self) -> None:
                super().__init__()
                self.media_source: int | str = 0
                self.cap: VideoCapture = VideoCapture(self.media_source)

        def _update_feed_params(self, data):
                self.media_source = data
                self.cap.release()
                self.cap: VideoCapture = VideoCapture(self.media_source)

        def _grab_frames(self):
                ok, frame = self.cap.read()
                if not ok:
                        # self.error.emit(f"Frame Grabber failed to get more frames", {self.objectName()})
                        print(f"Add error handling in {self.objectName()}")
                        return
                frame = cvtColor(frame, COLOR_BGR2RGB)
                sender = self.objectName()
                purpose = Purpose.RESTART_CYCLE
                self.write_to_queue.emit((sender, purpose, frame))
                        # self.fps.emit((1/(time.time()-start)))
        
        @Slot(Any)
        def handle_received_data(self, pack):
                """Validate data received and call the appropriate function to process the data"""
                try:
                        target, purpose, data = pack
                except:
                        print(f"{self.objectName()} can't parse data passed to slot -> {pack}")
                if not (target == self.objectName() or target == "all"):
                        return
                if purpose == Purpose.RESTART_CYCLE:
                        if not self.thread().isInterruptionRequested():
                                self._grab_frames()
                elif purpose == Purpose.UPDATE_PARAMETERS:
                        self._update_feed_params(data)