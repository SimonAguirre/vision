from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QThread, Slot, QTimer, Signal, QObject

from collections import defaultdict
from typing import Any
Any = type(Any)

from pipeline.constants import Purpose
from pipeline.data_queue import DataQueue
from pipeline.frame_grabber import FrameGrabber
from pipeline.object_detector import ObjectDetector
from pipeline.frame_annotator import Annotator

class Controller(QObject):
        # Controller Signals
        status_request = Signal()
        start_cycle = Signal(tuple)
        update_parameter = Signal(tuple)

        # Controller Members
        log_count = 0
        frame_q_items = 0
        detection_q_items = 0
        media_source: int | str = 0
        model_file: str = './models/best_from_past_research.pt'
        overlap_threshold: float = 0.54
        confidence: float = 0.7

        # Stage 1
        frame_grabber = FrameGrabber()
        frame_grabber_thread = QThread()
        frame_q = DataQueue()
        frame_q_thread = QThread()

        # Stage 2
        object_detector = ObjectDetector()
        object_detector_thread = QThread()

        # Stage 3
        detection_q = DataQueue()
        detection_q_thread = QThread()

        # Stage 4
        frame_annotator = Annotator()
        frame_annotator_thread = QThread()

        # Stage 5
        show_q = DataQueue()
        show_q_thread = QThread()

        def __init__(self, parent: QWidget | None = None) -> None:
                super().__init__(parent)

                # Set Unique Object Names and move to their own threads
                self.frame_grabber.setObjectName("Frame Grabber")
                self.frame_q.setObjectName("Input Frames Queue")
                self.object_detector.setObjectName("Object Detector")
                self.detection_q.setObjectName("Detections Queue")
                self.frame_annotator.setObjectName("Frame Annotator")
                self.show_q.setObjectName("Show Queue")

                self.global_stats = defaultdict(lambda: [])

                self.objects = {self.frame_grabber.objectName(): self.frame_grabber,
                                                self.frame_q.objectName(): self.frame_q,
                                                self.object_detector.objectName(): self.object_detector,
                                                self.detection_q.objectName(): self.detection_q,
                                                self.frame_annotator.objectName() : self.frame_annotator,
                                                self.show_q.objectName(): self.show_q}
                
                self.frame_grabber.moveToThread(self.frame_grabber_thread)
                self.frame_q.moveToThread(self.frame_q_thread)
                self.object_detector.moveToThread(self.object_detector_thread)
                self.detection_q.moveToThread(self.detection_q_thread)
                self.frame_annotator.moveToThread(self.frame_annotator_thread)
                self.show_q.moveToThread(self.show_q_thread)

                #Stage 1 connections
                self.frame_q.give_data_to_worker.connect(self.frame_grabber.handle_received_data)
                self.frame_grabber.write_to_queue.connect(self.frame_q.put)

                # Stage 2 connections
                self.object_detector.read_from_queue.connect(self.frame_q.get)
                self.frame_q.give_data_to_worker.connect(self.object_detector.handle_received_data)

                #Stage 3 connections
                self.object_detector.write_to_queue.connect(self.detection_q.put)
                self.detection_q.give_data_to_worker.connect(self.object_detector.handle_received_data)

                #Stage 4 connections
                self.frame_annotator.read_from_queue.connect(self.detection_q.get)
                self.detection_q.give_data_to_worker.connect(self.frame_annotator.handle_received_data)

                # Stage 5 connections
                self.frame_annotator.write_to_queue.connect(self.show_q.put)
                self.show_q.give_data_to_worker.connect(self.frame_annotator.handle_received_data)
                

                # Controller connections
                self.status_request.connect(self.frame_q.status_request_handler)
                self.status_request.connect(self.detection_q.status_request_handler)
                self.status_request.connect(self.show_q.status_request_handler)
                self.status_request.connect(self.frame_grabber.status_request_handler)
                self.status_request.connect(self.object_detector.status_request_handler)
                self.status_request.connect(self.frame_annotator.status_request_handler)

                self.frame_q.status_update.connect(self.handle_received_data)
                self.detection_q.status_update.connect(self.handle_received_data)
                self.show_q.status_update.connect(self.handle_received_data)
                self.frame_annotator.status_update.connect(self.handle_received_data)
                self.frame_grabber.status_update.connect(self.handle_received_data)
                self.object_detector.status_update.connect(self.handle_received_data)

                self.start_cycle.connect(self.frame_grabber.handle_received_data)
                self.start_cycle.connect(self.object_detector.handle_received_data)
                self.start_cycle.connect(self.frame_annotator.handle_received_data)

                # Timer for testing
                self.status_logger_timer = QTimer(self)
                self.status_logger_timer.timeout.connect(self.cycle_timeout_handler)

        def _status_logger(self):
                self.log_count += 1
                log = f"{self.log_count}"
                for name, object in self.objects.items():
                        log += f" | {name} {self.global_stats[name][-1]}"
                print(log)
                if self.log_count == 60:
                        self.status_logger_timer.stop()

        def start_threads(self):
                self.frame_q_thread.start()
                self.detection_q_thread.start()
                self.show_q_thread.start()
                self.frame_grabber_thread.start()
                self.object_detector_thread.start()
                self.frame_annotator_thread.start()
                
                self.start_cycle.emit(("all", Purpose.RESTART_CYCLE, "None"))
                self.status_logger_timer.start(1000)

        @Slot(Any)
        def handle_received_data(self, pack):
                sender, purpose, data  = pack
                if purpose == Purpose.STATUS_UPDATE:
                        object_stats = self.global_stats[sender]
                        object_stats.append(data)
                if sender == "VIEW" and purpose == Purpose.UPDATE_PARAMETERS:
                        self.update_parameter.emit((self.frame_grabber.objectName(), Purpose.UPDATE_PARAMETERS, data))
                        self.start_threads()
                # elif sender == "VIEW" and purpose == "STOP":
                        # self.stop_threads()
        @Slot()
        def cycle_timeout_handler(self):
                self.status_request.emit()
                self._status_logger()

        @Slot()
        def exit_app(self):
                self.thread().quit()