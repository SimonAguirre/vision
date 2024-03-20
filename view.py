# # Python 3.12.2

import os
import time
import sys

from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QImage, QPixmap, QFont, QIcon
from PySide6.QtWidgets import (QApplication, QComboBox, QFileDialog,
                               QHBoxLayout, QLabel, QMainWindow, QPushButton,
                               QSizePolicy, QVBoxLayout, QWidget, QSlider, QStackedWidget,
                               QTableWidget, QTableWidgetItem)


from gui.main_gui import GUI


class MainWindow(QMainWindow):
        def __init__(self):
                super().__init__()

                self.ui = GUI()
                self.ui.initializeUI(self)

                self.ui.header.minimize_button.clicked.connect(self.showMinimized)
                self.ui.header.maximize_button.clicked.connect(lambda: self.showNormal() if self.isMaximized() else self.showMaximized())
                self.ui.header.close_button.clicked.connect(self.close)
                
                self.ui.header.live_button.clicked.connect(lambda: self.ui.content.setCurrentWidget(self.ui.page_live))
                self.ui.header.playback_button.clicked.connect(lambda: self.ui.content.setCurrentWidget(self.ui.page_playback))

                self.setCentralWidget(self.ui.central_widget)

        def mousePressEvent(self, event):
                if event.buttons() == Qt.MouseButton.LeftButton and event.position().y() <= self.ui.header.height():
                        self.drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
                        event.accept()
                else:
                        super().mousePressEvent(event)

        def mouseMoveEvent(self, event):
                if event.buttons() == Qt.MouseButton.LeftButton and hasattr(self, 'drag_pos'):
                        self.move(event.globalPosition().toPoint() - self.drag_pos)
                        event.accept()
                else:
                        super().mouseMoveEvent(event)

        def mouseReleaseEvent(self, event):
                if hasattr(self, 'drag_pos'):
                        delattr(self, 'drag_pos')
                        event.accept()
                else:
                        super().mouseReleaseEvent(event)

                
                

if __name__ == "__main__":
        app = QApplication()
        app.setWindowIcon(QIcon("src/logo_1.png"))
        view = MainWindow()
        view.show()
        sys.exit(app.exec())
