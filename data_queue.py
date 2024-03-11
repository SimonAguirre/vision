import queue
from numpy import ndarray
from supervision import Detections
from cv2.typing import MatLike
from typing import Any
from PySide6.QtGui import QImage
from PySide6.QtCore import QObject, Signal, Slot
from testing import VERBOSE
import time

class DataQueue(QObject):
        dequeue = Signal(Any)
        peek = Signal(bool)
        time_of_last_insert = time.time()
        
        def __init__(self, parent = None):
                super().__init__(parent=parent)
                self.queue = queue.Queue()
        
        @Slot()
        def get(self):
                """Remove and return an item from the queue."""
                self.dequeue.emit(self.queue.get())
        
        @Slot(tuple)
        def put(self, data):
                """Put an item into the queue."""
                item, sender = data
                self.queue.put(item)
                new_time = time.time()
                print(f"{sender} added item to {self.objectName()} {new_time-self.time_of_last_insert} seconds after last insert") if VERBOSE else ...
                self.time_of_last_insert = new_time
        @Slot()
        def empty(self):
                """Return True if the queue is empty, False otherwise."""
                self.peek.emit(self.queue.empty())