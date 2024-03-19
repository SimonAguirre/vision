from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton, QMainWindow, QWidget, QVBoxLayout, QSizePolicy, QGraphicsDropShadowEffect
from PySide6.QtGui import QFont, QColor
from PySide6.QtSvgWidgets import QSvgWidget

class Button(QPushButton):
        def __init__(self, parent) -> None:
                super().__init__(parent)
                self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
                self.setStyleSheet("color: rgb(255, 255, 255); font-size: 24px; padding: 0 24px; border: 0px solid;")
                main_layout = QVBoxLayout()
                main_layout.setSpacing(0)
                main_layout.setContentsMargins(0, 0, 0, 0)
                self.setLayout(main_layout)


class Header(QFrame):
        def __init__(self) -> None:
                super().__init__()
                self.setStyleSheet("background-color: #414141;")  # Set header background color
                self.setFixedHeight(60)  # Set header height
                
                # Set Layout for the header
                main_layout = QHBoxLayout()
                self.setLayout(main_layout)
                main_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero
                main_layout.setSpacing(0)

                # Add title label to the header
                self.title_label = QLabel()
                self.title_label_layout = QVBoxLayout()
                self.title_label_layout.setContentsMargins(24,13,24,13)
                self.title_label.setLayout(self.title_label_layout)

                self.logo = QSvgWidget("./gui_res/logo.svg")
                self.logo.setFixedSize(150, 33)

                self.title_label_layout.addWidget(self.logo)
                self.title_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
                self.title_label.setFixedWidth(198)
                main_layout.addWidget(self.title_label)

                # Add button for Live Mode
                self.live_button = Button(self, )
                main_layout.addWidget(self.live_button)

                # Add button for Playback Mode
                self.playback_button = Button(self)
                main_layout.addWidget(self.playback_button)

                # Add an expanding object for the alignment of important objects
                spacer = QLabel()
                main_layout.addWidget(spacer)

                # Add custom minimize button
                self.minimize_button = QPushButton("-")
                self.minimize_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
                # self.minimize_button.setFixedWidth(30)
                self.minimize_button.setStyleSheet("color: rgb(255, 255, 255); font-size: 20px; padding: 10px; border: 0px solid;")
                main_layout.addWidget(self.minimize_button)

                # Add custom maximize button
                self.maximize_button = QPushButton("M")
                self.maximize_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
                # self.maximize_button.setFixedWidth(30)
                self.maximize_button.setStyleSheet("color: rgb(255, 255, 255); font-size: 20px; padding: 10px; border: 0px solid;")
                main_layout.addWidget(self.maximize_button)

                # Add custom close button
                self.close_button = QPushButton("X")
                self.close_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
                # self.close_button.setFixedWidth(30)
                self.close_button.setStyleSheet("color: rgb(255, 255, 255); font-size: 20px; padding: 10px; border: 0px solid;")
                main_layout.addWidget(self.close_button)
