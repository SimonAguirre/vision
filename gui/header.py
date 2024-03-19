from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLayout, QLabel, QPushButton, QMainWindow, QWidget, QVBoxLayout, QSizePolicy, QGraphicsDropShadowEffect
from PySide6.QtGui import QFont, QColor, QIcon, QImage, QPixmap
from PySide6.QtSvgWidgets import QSvgWidget

class Button(QPushButton):
        def __init__(self, parent, icon) -> None:
                super().__init__(parent)
                self.setIcon(icon)
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
                self.setFixedHeight(100)  # Set header height
                
                # Set Layout for the header
                main_layout = QVBoxLayout()
                self.setLayout(main_layout)
                main_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero
                main_layout.setSpacing(0)
                
                window_control_frame = QFrame()
                window_control_layout = QHBoxLayout()
                window_control_frame.setLayout(window_control_layout)
                window_control_frame.setFixedHeight(30)
                
                # window_control_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
                window_control_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero
                window_control_layout.setSpacing(0)
                
                header_layout = QHBoxLayout()
                header_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
                header_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero
                header_layout.setSpacing(0)
                
                main_layout.addWidget(window_control_frame)
                main_layout.addLayout(header_layout)

                """
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
                """
                self.logo = QPixmap("./gui_res/logo_1.png")
                self.logo = self.logo.scaledToHeight(60, Qt.TransformationMode.FastTransformation)
                self.logo_holder = QLabel()
                self.logo_holder.setFixedSize(80, 70)
                self.logo_holder.setPixmap(self.logo)
                header_layout.addWidget(self.logo_holder)
                # Add button for Live Mode
                self.live_button = Button(self, QIcon('gui_res/live.png'))
                header_layout.addWidget(self.live_button)

                # Add button for Playback Mode
                self.playback_button = Button(self, QIcon('gui_res/live.png'))
                header_layout.addWidget(self.playback_button)


                window_title = QLabel("BATSTATEU-TNEU: Vision Drive")
                window_title.setStyleSheet("color: white; padding: 0 15px;")
                window_title.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
                window_control_layout.addWidget(window_title)
                # Add an expanding object for the alignment of important objects
                spacer = QLabel()
                window_control_layout.addWidget(spacer)

                # Add custom minimize button
                self.minimize_button = QPushButton()
                self.minimize_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
                self.minimize_button.setIcon(QIcon('gui_res/minimize.png'))
                self.minimize_button.setStyleSheet("padding: 10px; border: 0px solid;")
                window_control_layout.addWidget(self.minimize_button)

                # Add custom maximize button
                self.maximize_button = QPushButton()
                self.maximize_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
                self.maximize_button.setIcon(QIcon('gui_res/dock.png'))
                self.maximize_button.setStyleSheet("padding: 10px; border: 0px solid;")
                window_control_layout.addWidget(self.maximize_button)

                # Add custom close button
                self.close_button = QPushButton()
                self.close_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
                self.close_button.setIcon(QIcon('gui_res/close.png'))
                self.close_button.setStyleSheet("padding: 10px; border: 0px solid;")
                window_control_layout.addWidget(self.close_button)
