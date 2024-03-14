from asyncio.proactor_events import _ProactorBaseWritePipeTransport
from xml.dom.pulldom import PullDOM
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication
from PySide6.QtCore import QThread, QThreadPool, Slot, QTimer, Signal
from data_queue import DataQueue
from frame_grabber import FrameGrabber

from typing import Any
from testing import VERBOSE
from constants import Purpose
from frame_pooler import FramePooler
from object_detector import ObjectDetector
# from tracking_msg import TrackingMsg
from object_tracker import Tracker
from frame_annotator import Annotator

import time
import sys
Any = type(Any)

class GUI(QMainWindow):
        read_queue_stats = Signal()
        start_cycle = Signal(Any)

        frame_grabber_thread = QThread()
        object_detector_thread = QThread()
        object_detector_thread_2 = QThread()
        # frame_annotator_thread = QThread()
        # frame_viewer_thread = QThread()

        frame_grabber = FrameGrabber()
        frame_q = DataQueue()
        object_detector = ObjectDetector()
        object_detector_2 = ObjectDetector()
        detection_q = DataQueue()
        # annotator = Annotator()
        # playback = FramePooler()

        log_count = 0
        frame_q_items = 0
        detection_q_items = 0

        def __init__(self, parent: QWidget | None = None) -> None:
                super().__init__(parent)
                # Stage 1
                self.media_source: int | str = 0
                self.frame_grabber.setObjectName("Frame Grabber")
                self.frame_q.setObjectName("Input Frames Queue")
                self.frame_grabber.moveToThread(self.frame_grabber_thread)

                self.frame_q.give_data_to_worker.connect(self.frame_grabber.handle_received_data)
                self.frame_grabber.write_to_queue.connect(self.frame_q.put)

                # Stage 2
                self.model_file: str = './models/best_from_past_research.pt'
                self.overlap_threshold: float = 0.54
                self.confidence: float = 0.7

                self.object_detector.setObjectName("Object Detector")
                self.detection_q.setObjectName("Detections Queue")
                self.object_detector.moveToThread(self.object_detector_thread)

                self.detection_q.give_data_to_worker.connect(self.object_detector.handle_received_data)

                self.object_detector.read_from_queue.connect(self.frame_q.get)

                self.frame_q.give_data_to_worker.connect(self.object_detector.handle_received_data)
                self.object_detector.write_to_queue.connect(self.detection_q.put)

                self.object_detector_2.setObjectName("Object Detector_2")
                self.object_detector_2.moveToThread(self.object_detector_thread_2)

                self.detection_q.give_data_to_worker.connect(self.object_detector_2.handle_received_data)

                self.object_detector_2.read_from_queue.connect(self.frame_q.get)

                self.frame_q.give_data_to_worker.connect(self.object_detector_2.handle_received_data)
                self.object_detector_2.write_to_queue.connect(self.detection_q.put)


                self.read_queue_stats.connect(self.frame_q.status_request_handler)
                self.read_queue_stats.connect(self.detection_q.status_request_handler)
                
                self.frame_q.status_update.connect(self.handle_received_data)
                self.detection_q.status_update.connect(self.handle_received_data)

                self.start_cycle.connect(self.frame_grabber.handle_received_data)
                self.start_cycle.connect(self.object_detector.handle_received_data)
                self.start_cycle.connect(self.object_detector_2.handle_received_data)
                
                self.status_logger_timer = QTimer(self)
                self.status_logger_timer.timeout.connect(self.cycle_timeout_handler)
        
        @Slot(Any)
        def handle_received_data(self, data):
                try:
                        sender, purpose, data  = data
                except:
                        print(f"{self.objectName()} can't parse data passed to slot -> {data}")
                
                if purpose == Purpose.STATUS_UPDATE:
                        if sender == self.frame_q.objectName():
                                self.frame_q_items = data[0]
                        if sender == self.detection_q.objectName():
                                self.detection_q_items = data[0]
        @Slot()
        def cycle_timeout_handler(self):
                self.read_queue_stats.emit()
                self._status_logger()
                # self.start_cycle.emit((self.object_detector.objectName(), Purpose.RESTART_CYCLE, "None"))

        def _status_logger(self):
                self.log_count += 1
                print(f"{self.log_count} {self.frame_grabber.objectName()} : r-{self.frame_grabber_thread.isRunning()}")
                print(f"Frame Q: items-{self.frame_q_items} | Detections: -items-{self.detection_q_items}")
                print(f"{self.object_detector.objectName()} : r-{self.object_detector_thread.isRunning()} -score {self.object_detector.score}")
                print(f"{self.object_detector_2.objectName()} : r-{self.object_detector_thread_2.isRunning()} -score {self.object_detector_2.score}")
                if self.log_count == 60:
                        self.status_logger_timer.stop()
        def _start_threads(self):
                self.frame_grabber_thread.start()
                self.object_detector_thread.start()
                self.object_detector_thread_2.start()
                self.start_cycle.emit(("all", Purpose.RESTART_CYCLE, "None"))
                self.status_logger_timer.start(1000)

        @Slot()
        def exit_app(self):
                self.thread().quit()
                
if __name__ == "__main__":
        app = QApplication()
        controller = GUI()
        controller.show()
        controller.setObjectName("Main Thread")
        controller._start_threads()
        sys.exit(app.exec())