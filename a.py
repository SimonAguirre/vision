import sys
import queue as q
from PySide6.QtCore import QObject, QThread, Signal, Slot, QTimer
from PySide6.QtWidgets import QApplication
import time
from typing import Any
from data_queue import DataQueue
Any = type(Any)

class Worker(QObject):
    item_requested = Signal(str)  # Signal emitted to request an item from the main thread
    item_processed = Signal(tuple)  # Signal emitted when an item is processed

    def __init__(self):
        super().__init__()
        self.processing = False  # Flag to indicate whether the worker is currently processing an item
        self.score = 0
    @Slot()
    def request_item(self):
        if not self.processing:
                sender = self.objectName()
                # Only emit the request signal if not already processing an item
                self.item_requested.emit(sender)
                # print(f"{sender} requested")

    @Slot(str or None)
    def process_item(self, item):
        target, item = item
        if not target == self.objectName():
            return
        if item == "None":
            sender = self.objectName()
            # print("Queue empty!! retrying request")
            self.item_requested.emit(sender)
        else:
                self.processing = True
                sender = self.objectName()
                # Heavy processing here
                processed_item = self.process_item_expensive(item)
                self.item_processed.emit((processed_item, sender))
                self.score += 1
                # print(f"Worker {self.objectName()[-1]} Score : {self.score}")
                self.processing = False

    def process_item_expensive(self, item):
        # Simulate heavy processing
        sleep = 0.080
        start = time.time()
        while sleep >= time.time()-start:
              pass
                # print(f"processing {item} ...")
        return f"Item upgraded: {item}"

class Controller(QObject):
    write_to_q = Signal(Any)
    # give_item_w1 = Signal(str)
    # give_item_w2 = Signal(str)
    restart_cycle = Signal()
    restart_cycle_2 = Signal()
    def __init__(self):
        super().__init__()
        self.last_frame_time = time.time()
        self.fps_trail = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,]
        # Example items to be processed
        items = ['item1', 'item2', 'item3', 'item4']

        self.worker = Worker()
        self.worker_thread = QThread()
        self.worker.setObjectName("w1")
        
        self.worker_2 = Worker()
        self.worker_2.setObjectName("w2")
        self.worker_thread_2 = QThread()

        self.queue = DataQueue()
        self.queue.setObjectName("q1")
        self.queue_thread = QThread()
        
        # Move worker to the worker thread
        self.worker.moveToThread(self.worker_thread)
        self.worker_2.moveToThread(self.worker_thread_2)
        self.queue.moveToThread(self.queue_thread)

        # Connect signals and slots

        self.queue.data_output.connect(self.worker.process_item)
        self.queue.data_output.connect(self.worker_2.process_item)
        self.write_to_q.connect(self.queue.put)
        
        self.worker_thread.started.connect(self.worker.request_item)
        self.restart_cycle.connect(self.worker.request_item)
        # self.worker.item_requested.connect(self.fetch_item_from_queue)
        self.worker.item_requested.connect(self.queue.get)
        self.worker.item_processed.connect(self.process_item)
        self.worker_thread.finished.connect(self.worker_thread_ended)
        # self.give_item_w1.connect(self.worker.process_item)

        self.worker_thread_2.started.connect(self.worker_2.request_item)
        self.restart_cycle_2.connect(self.worker_2.request_item)
        # self.worker_2.item_requested.connect(self.fetch_item_from_queue)
        self.worker_2.item_requested.connect(self.queue.get)
        self.worker_2.item_processed.connect(self.process_item)
        self.worker_thread_2.finished.connect(self.worker_thread_ended)
        # self.give_item_w2.connect(self.worker_2.process_item)

        # Add items to the queue
        for item in items:
                self.write_to_q.emit(item)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.add_item_to_queue)
        self.timer.start(33)

    @Slot()
    def add_item_to_queue(self):
        self.write_to_q.emit(f"item {time.time():0.1f}")
        # print("tried to write to queue")

    @Slot()
    def worker_thread_ended(self):
         print(f"worker_thread_ended")

    @Slot(tuple)
    def process_item(self, item):
        # Handle processed item here
        item, sender = item
        if len(self.fps_trail) == 10:
              self.fps_trail.pop(0)
              self.fps_trail.append(1/(time.time()-self.last_frame_time))
        self.fps = sum(self.fps_trail)/10
        self.last_frame_time = time.time()
        print(f"{self.fps:0.2f}Received processed item: {item}, from {sender}")
        if sender == "w1":
             self.restart_cycle.emit()
        elif sender == 'w2':
             self.restart_cycle_2.emit()

    # @Slot(str)
    # def fetch_item_from_queue(self, sender):
    #     # Emit signal to worker requesting an item from the queue
    #     if not self.queue.empty():
    #             # print("fetching")
    #             item = self.queue.get()
    #             if sender == 'w1':
    #                     self.give_item_w1.emit(item)
    #             elif sender == 'w2':
    #                     self.give_item_w2.emit(item)
    #     else:
    #             if sender == 'w1':
    #                     self.give_item_w1.emit("None")
    #             elif sender == 'w2':
    #                     self.give_item_w2.emit("None")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create controller to manage worker thread
    controller = Controller()

    # Start the worker thread
    controller.queue_thread.start()
    controller.worker_thread.start()
    # time.sleep(0.040)
    controller.worker_thread_2.start()

    sys.exit(app.exec())