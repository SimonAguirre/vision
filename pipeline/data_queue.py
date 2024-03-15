import queue
from PySide6.QtCore import QObject, Signal, Slot
from typing import Any
from pipeline.constants import Purpose
Any = type(Any)


class DataQueue(QObject):
        give_data_to_worker = Signal(tuple)
        status_update = Signal(tuple)
        counter = 0
        on_q = 0
        

        def __init__(self, parent = None):
                super().__init__(parent=parent)
                self.queue = queue.LifoQueue()

        @Slot(str)
        def get(self, sender):
                """Request queue thread to emit an item 
                parameters:
                        - sender: str -> the name of the worker that requested
                results:
                        - a signal emitting a tuple of (name_of_requesting_worker, data)
                """
                target = sender
                try:
                        data = self.queue.get(block=False)
                        purpose = Purpose.CONTINUE_PROCESS
                        self.on_q -= 1
                except:
                        purpose = Purpose.RESTART_CYCLE
                        data = "None"
                self.give_data_to_worker.emit((target, purpose, data))
        
        @Slot(tuple)
        def put(self, pack):
                """Put item to the queue
                parameters:
                        - data: Any -> the item to be added to the queue
                """
                sender, purpose, data = pack
                item = data
                self.queue.put(item, block=False)
                self.on_q += 1
                self.counter += 1
                if purpose == Purpose.RESTART_CYCLE:
                        self.give_data_to_worker.emit((sender, purpose, "None"))

        @Slot()
        def status_request_handler(self):
                self.status_update.emit((self.objectName(), Purpose.STATUS_UPDATE, {"on_queue" : self.on_q, "total" : self.counter}))