from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication
from PySide6.QtCore import QThread, QThreadPool, Slot, QTimer

from data_queue import DataQueue
from frame_grabber import FrameGrabber


from frame_pooler import FramePooler
from object_detector import ObjectDetector
# from tracking_msg import TrackingMsg
from object_tracker import Tracker
from frame_annotator import Annotator

import time
import sys

class GUI(QMainWindow):
        def __init__(self, parent: QWidget | None = None) -> None:
                super().__init__(parent)
                
                self.frame_q = DataQueue()
                self.frame_q.setObjectName("Input Frames Queue")
                
                self.frame_grabber = FrameGrabber()
                self.frame_grabber.setObjectName("Frame Grabber")
                
                self.frame_grabber_thread = QThread()
                self.frame_grabber_thread.started.connect(self.frame_grabber.main_function)
                self.frame_grabber.finished.connect(self.frame_grabber_thread.quit)
                self.frame_grabber.main_output_stream.connect(self.frame_q.put)
                self.frame_grabber.moveToThread(self.frame_grabber_thread)
                # self.frame_grabber.main_output_stream.connect()
                self.frame_grabber_thread.start()
                
                end_timer = QTimer(self)
                end_timer.timeout.connect(self.exit_app)
                end_timer.setSingleShot(True)
                end_timer.start(10000)
                
        @Slot()
        def exit_app(self):
                self.thread().quit()
                
if __name__ == "__main__":
        app = QApplication()
        w = GUI()
        w.show()
        sys.exit(app.exec())