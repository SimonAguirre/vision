from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication
from PySide6.QtCore import QThread

from frame_grabber import FrameGrabber
from data_queue import MessageQueue
from object_detector import ObjectDetector
from tracking_msg import TrackingMsg
from object_tracker import ObjectTracker
from frame_annotator import FrameWriter
from data_queue import MessageQueue

import sys

class GUI(QMainWindow):
        def __init__(self, parent: QWidget | None = ..., flags: Qt.WindowType = ...) -> None:
                super().__init__(parent, flags)
                    # Create the message queues
                    
        input_queue = MessageQueue()
        detection_queue = MessageQueue()
        tracking_queue = MessageQueue()
        output_queue = MessageQueue()

        # Create the tasks
        frame_grabber = FrameGrabber(input_queue)
        object_detector = ObjectDetector(input_queue, detection_queue)
        object_tracker = ObjectTracker(detection_queue, tracking_queue)
        frame_writer = FrameWriter(tracking_queue, output_queue)

        # Start the tasks
        frame_grabber.start()
        object_detector.start()
        object_tracker.start()
        frame_writer.start()

        # Wait for all tasks to finish
        frame_grabber.wait()
        object_detector.wait()
        object_tracker.wait()
        frame_writer.wait()




if __name__ == "__main__":
        app = QApplication()
        w = GUI()
        w.show()
        sys.exit(app.exec())