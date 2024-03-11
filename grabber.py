from unittest import result
from PySide6.QtCore import QObject, QThread, Qt, Signal, Slot, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
import time
import sys
from data_queue import DataQueue

from frame_grabber import FrameGrabber

class Worker(QObject):
        finished = Signal()
        results = Signal(int)
        @Slot()
        def main_function(self): ...

class FrameGrabber(Worker):
        finished = Signal()
        results = Signal(int)
        def main_function(self):
                s = 0
                while True:
                        name = self.objectName()
                        s += 1
                        print(s)
                        self.results.emit(name)
                        time.sleep(1)

class Controller(QObject):
        # workerThread = QThread()
        # operate = Signal()
        # terminate = Signal(QThread)
        # work = Signal(QThread)
        # public
        def __init__(self, parent: QObject | None = None) -> None:
                super().__init__(parent)
                self.workers: dict[str, Worker] = {}
        
        def add_worker(self, worker_object: Worker, worker_name):
                worker = worker_object
                worker.setObjectName(worker_name)
                thread = QThread()
                worker.moveToThread(thread)
                worker.finished.connect(thread.quit)
                thread.started.connect(worker.main_function)
                self.workers[worker_name] = worker
                
        def stop_worker(self, worker_name):
                self.workers[worker_name].thread().quit()
                self.workers[worker_name].thread().wait()
                print(f"****{worker_name} thread terminated****")
                
        def start_worker(self, worker_name):
                print(type(self.worker_threads[worker_name]))
                print(f"****{worker_name} thread started****")
                
        @Slot(str)
        def handle_results(self, result):
                print(result)

class MainWindow(QMainWindow):
        # cue = Signal()
        def __init__(self) -> None:
                super().__init__()
                print("*******************")
                controller = Controller()
                controller.add_worker(FrameGrabber(),"Frame Grabber")
                controller.workers['Frame Grabber'].results.connect(self.handle_results)
                controller.start_worker('Frame Grabber')
                
                frame_q = DataQueue()
                
                # controller.add_worker = (QThread(), "Frame Grabber")
                # # 1 - create Worker and Thread inside the Form
                # self.worker = FrameGrabber() # no parent
                # self.worker.setObjectName("Frame Grabber")
                # self.workerThread = QThread() # no parent
                
                # # 2 - Connect Worker`s Signals to Controller method slots to post data.
                # self.worker.result_ready.connect(self.handle_results)

                # # 3 - Move the Worker to the Thread object
                # self.worker.moveToThread(self.workerThread)

                # # 4 - Connect Worker Signals to the Thread slots
                # self.worker.done.connect(self.workerThread.quit)

                # # 5 - Connect Thread started signal to Worker operational slot method
                # self.workerThread.started.connect(self.worker.grab_frame)

                # # * - Thread finished signal will close the app if you want!
                # #self.thread.finished.connect(app.exit)

                # # 6 - Start the thread
                # self.workerThread.start()

                # 7 - Start the form
                self.initialize_ui()
                
                print("****test ended****")
        def initialize_ui(self):
                pass
                # grid = QGridLayout()
                # self.setLayout(grid)
                # grid.addWidget(self.label,0,0)

                # self.move(300, 150)
                # self.setWindowTitle('thread test')
                # self.show()
        @Slot(int)
        def handle_results(self, results):
                print(results)
        
        
        # @Slot()
        # def command(self):
        #         self.cue.emit()
                
app = QApplication(sys.argv)
window = MainWindow()
app.exec()
