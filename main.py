
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QThread
from PySide6.QtGui import QIcon

from controller import Controller
from view import GUI, MainWindow

import sys

if __name__ == "__main__":
        app = QApplication(sys.argv)
        controller = Controller()
        controller.setObjectName("Controller")
        controller_thread = QThread()
        # controller.moveToThread(controller_thread)
        controller.start_threads() # make this a slot and have a signal from view to activate this
        view = MainWindow()
        view.show()
        app.setWindowIcon(QIcon("./gui_res/logo_icon.svg"))
        sys.exit(app.exec())