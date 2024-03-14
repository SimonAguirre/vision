from PySide6.QtCore import QObject, Signal, Slot
from supervision import ByteTrack
from data_queue import DataQueue
from supervision import Detections
from cv2.typing import MatLike
import cv2
from constants import Purpose

class Tracker(QObject):
        read_from_queue = Signal(str) # request
        write_to_queue = Signal(tuple)
        score = 0
        def __init__(self):
                super().__init__()
                self.tracker = ByteTrack()

        def _request_data(self):
                """Request detections from queue"""
                sender = self.objectName()
                self.read_from_queue.emit(sender)

        def _track(self, data):
                """Run tracking on the detections and emit the result to tracking queue"""
                frame, detections, class_names = data
                new_detections = self.tracker.update_with_detections(detections)
                sender = self.objectName()
                purpose = Purpose.RESTART_CYCLE
                data = (frame, new_detections, class_names)
                self.write_to_queue.emit((sender, purpose, data))
                self.score += 1

        def _initilize_tracker(self, data):
                """Initialize tracker used for tracking"""
                self.track_thresh, self.track_buffer, self.match_thresh, self.frame_rate = data
                self.tracker = ByteTrack(
                        self.track_thresh,
                        self.track_buffer,
                        self.match_thresh,
                        self.frame_rate
                )

        def _update_tracking_params(self, data):
                """Update tracking parameters
                params:
                        - data: tuple of (tracking threshold, 
                                          matching threshold)
                """
                self.track_thresh, self.match_thresh, = data
                self.tracker.track_thresh = self.track_thresh
                self.tracker.match_thresh = self.match_thresh

        @Slot(tuple)
        def handle_received_data(self, pack):
                """Validate data received and call the appropriate function to process the data"""
                try:
                        target, purpose, data = pack
                except:
                        print(f"{self.objectName()} can't parse data passed to slot -> {pack}")
                if not (target == self.objectName() or target == "all"):
                        return
                if purpose == Purpose.CONTINUE_PROCESS:
                        self._track(data)
                elif purpose == Purpose.RESTART_CYCLE:
                        if not self.thread().isInterruptionRequested():
                                self._request_data()
                elif purpose == Purpose.UPDATE_PARAMETERS:
                        self._update_tracking_params(data)
                elif purpose == Purpose.INITIALIZE:
                        self._initilize_tracker(data)