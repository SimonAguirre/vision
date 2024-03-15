from cv2 import VideoCapture, cvtColor, COLOR_BGR2RGB
from typing import Any
from PySide6.QtCore import QObject, Signal, Slot
from pipeline.constants import Purpose
Any = type(Any)

class FrameGrabber(QObject):
        write_to_queue = Signal(tuple)
        status_update = Signal(tuple)
        fps = 0
        score = 0
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
                        return
                frame = cvtColor(frame, COLOR_BGR2RGB)
                sender = self.objectName()
                purpose = Purpose.RESTART_CYCLE
                self.write_to_queue.emit((sender, purpose, frame))
                self.score +=1
        
        @Slot(Any)
        def handle_received_data(self, pack):
                """Validate data received and call the appropriate function to process the data"""
                target, purpose, data = pack
                if not (target == self.objectName() or target == "all"):
                        return
                if purpose == Purpose.RESTART_CYCLE:
                        if not self.thread().isInterruptionRequested():
                                self._grab_frames()
                elif purpose == Purpose.UPDATE_PARAMETERS:
                        self._update_feed_params(data)
        @Slot()
        def status_request_handler(self):
                self.status_update.emit((self.objectName(), Purpose.STATUS_UPDATE, {"fps" : self.fps, "score" : self.score}))