from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QLabel, QSizePolicy
from PySide6.QtCore import Qt, Signal

class Viewport(QLabel):
        mousePressed = Signal(tuple)
        def __init__(self, parent=None):
                QLabel.__init__(self, parent)
                self.setMinimumSize(640, 480)
                self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.setScaledContents(True)
                self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        def mousePressEvent(self, event: QMouseEvent) -> None:
                active_point = (event.position().x()/self.size().width(), event.position().y()/self.size().height())
                self.mousePressed.emit(active_point)