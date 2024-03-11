from PySide6.QtCore import QObject, QThread
from numpy import ndarray

from data_queue import DataQueue
from PySide6.QtCore import Signal
from PySide6.QtGui import QImage

class FramePooler(QThread):
        updateFrame = Signal(QImage)
        def __init__(self, in_queue: DataQueue, 
                parent: QObject | None = None) -> None:
                super().__init__(parent)
                self.queue: DataQueue = in_queue
                print("Frame Pooler ready")
        def run(self):
                frame: ndarray = self.queue.get()
                h, w, ch = frame.shape
                img = QImage(frame.data, w, h, ch * w, QImage.Format.Format_RGB888)
                # scaled_img = img.scaled(frame_size[0], frame_size[1], Qt.KeepAspectRatio)
                del frame
                # Emit signal
                self.updateFrame.emit(img)