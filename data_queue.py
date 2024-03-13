import queue
from numpy import ndarray
from supervision import Detections
from cv2.typing import MatLike
from PySide6.QtGui import QImage
from PySide6.QtCore import QObject, Signal, Slot
from testing import print_
import time
from typing import Any
Any = type(Any)


class DataQueue(QObject):
        data_output = Signal(Any)
        peek = Signal(bool)
        time_of_last_insert = time.time()
        
        def __init__(self, parent = None):
                super().__init__(parent=parent)
                self.queue = queue.Queue()
        
        @Slot(str)
        def get(self, sender):
                print_(f"@{self.objectName()}: {sender} requested an item", end = ' ... ')
                self.data_output.emit(self.queue.get())
                print_("Done")
        
        @Slot(tuple)
        def put(self, data):
                item, sender = data
                self.queue.put(item)
                new_time = time.time()
                print_(f"{sender} added item to {self.objectName()} {new_time-self.time_of_last_insert} seconds after last insert")
                self.time_of_last_insert = new_time
        @Slot()
        def empty(self):
                """Return True if the queue is empty, False otherwise."""
                self.peek.emit(self.queue.empty())