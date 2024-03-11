from PySide6.QtCore import QObject, QThread, QThreadPool
from frame_grabber import *

class Controller(QThreadPool):
        def __init__(self):
                super().__init__()
                self.workers: dict[str,QThread] = {}
                
        def add_worker(self, worker: QThread):
                self.workers[str(worker).split(' ')[0]] = worker
        
        def stop_worker(self, worker: QThread):
                worker.terminate()