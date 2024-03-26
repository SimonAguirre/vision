
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QThread
from PySide6.QtGui import QIcon

from controller import Controller
from view import GUI, MainWindow

import sys

import sys
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QEvent, QPoint
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication
from gui.main_gui import GUI

if __name__ == "__main__":
        app = QApplication(sys.argv)
        controller = Controller()
        view = GUI()
        controller.setObjectName("Controller")
        controller.show_q.give_data_to_worker.connect(view.update_preview)
        view.switch_mode.connect(controller.handle_received_data)
        # controller.start_threads() # make this a slot and have a signal from view to activate this

        app.setWindowIcon(QIcon("./gui_res/logo_1.png"))

        sys.exit(app.exec())