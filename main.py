
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QThread

from controller import Controller
from view import GUI

import sys

if __name__ == "__main__":
        app = QApplication()
        controller = Controller()
        controller.setObjectName("Controller")
        controller_thread = QThread()
        # controller.moveToThread(controller_thread)
        controller.start_threads() # make this a slot and have a signal from view to activate this
        # view = GUI()
        # view.show()
        sys.exit(app.exec())