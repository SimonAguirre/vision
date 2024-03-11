import time
import sys

from frame_grabber import FrameGrabber
from data_queue import DataQueue
from PySide6.QtCore import QThread, Qt, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

class MainWindow(QMainWindow):
        def __init__(self, parent: QWidget | None = None) -> None:
                super().__init__(parent)
                
                self.start = time.time()
 
                frame_q = DataQueue()
                self.frame_grabber = FrameGrabber(queue=frame_q)
                self.frame_grabber.fps.connect(self.logger)
                self.frame_grabber.error.connect(self.error_handler)
                self.frame_grabber.finished.connect(self.thread_ended)
                
                frame_q_2 = DataQueue()
                self.frame_grabber_2 = FrameGrabber(queue=frame_q_2)
                self.frame_grabber_2.fps.connect(self.logger)
                self.frame_grabber_2.error.connect(self.error_handler)
                self.frame_grabber_2.finished.connect(self.thread_ended)
                self.frame_grabber_2.media_source = 1
                
                print("Starting 1")
                self.frame_grabber.start()
                time.sleep(0.5)
                
                print("Ending 1")
                self.frame_grabber.stop("GUI")
                
                print("Starting 2")
                self.frame_grabber_2.start()
                time.sleep(0.5)
                
                print("Ending 2")
                self.frame_grabber_2.stop("GUI")
                
                print("Restarting 1")
                self.frame_grabber.start()
                time.sleep(0.5)
                
                print("Ending 1")
                self.frame_grabber.stop("GUI")
                
                time.sleep(0.25)
                sys.exit()
                
        def lap(self):
                print(f"{(time.time()-self.start)} secs")
                return time.time()

        def thread_ended(self):
                print("*****thread work finished*****")
        
        # Prints the data into CLI
        def logger(self, data):
                text, source = data
                print(f"{source}: {text}")

        @Slot(tuple)
        def error_handler(self, data: tuple[str,QThread]):
                error, source = data
                print(f"GUI_thread: Terminating {source} thread due to error: {error}")
                if (source == 1):
                        self.frame_grabber.terminate()
                        self.frame_grabber_2.terminate()
                time.sleep(1)
                        
app = QApplication(sys.argv)
window = MainWindow()
app.exec()
