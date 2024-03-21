from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLayout, QLabel, QPushButton, QMainWindow, QWidget, QVBoxLayout, QSizePolicy, QGraphicsDropShadowEffect, QApplication
from PySide6.QtGui import QFont, QColor, QIcon, QImage, QPixmap
from PySide6.QtSvgWidgets import QSvgWidget

class HeaderButton(QPushButton):
        def __init__(self, parent, icon) -> None:
                super().__init__(parent)
                self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
                # self.setStyleSheet("color: rgb(255, 255, 255); font-size: 24px; padding: 13 24px; border: 0px solid;")
                self.button_icon = QSvgWidget(icon)
                main_layout = QVBoxLayout()
                main_layout.setContentsMargins(15,13,15,13)
                main_layout.setSpacing(0)
                main_layout.setContentsMargins(0, 0, 0, 0)
                self.setLayout(main_layout)

                main_layout.addWidget(self.button_icon)

class Header(QWidget):
        def __init__(self) -> None:
                super().__init__()
                self.setObjectName("Header")
                self.setStyleSheet("""background-color: #444;""")  # Set header background color
                self.setFixedHeight(100)  # Set header height
                
                # Set Layout for the header
                main_layout = QVBoxLayout()
                self.setLayout(main_layout)
                main_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero
                main_layout.setSpacing(0)
                
                window_control_frame = QWidget()
                window_control_layout = QHBoxLayout()
                window_control_frame.setLayout(window_control_layout)
                window_control_frame.setFixedHeight(30)
                # window_control_frame.setStyleSheet("background-color: 'black'")
                
                # window_control_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
                window_control_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero
                window_control_layout.setSpacing(0)
                
                header_layout = QHBoxLayout()
                header_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
                # header_layout.setContentsMargins(19, 15, 15, 15)  # Set margins to zero
                header_layout.setSpacing(10)
                
                main_layout.addWidget(window_control_frame)
                main_layout.addLayout(header_layout)

                self.logo = QSvgWidget("src/svg/logo.svg")
                self.logo.setFixedSize(53, 59)
                header_layout.addWidget(self.logo)

                # Add button for Live Mode
                self.live_button = HeaderButton(self, 'src/svg/live_60.svg')
                header_layout.addWidget(self.live_button)

                # Add button for Playback Mode
                self.playback_button = HeaderButton(self, 'src/svg/playback_60.svg')
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
                self.minimize_button.setIcon(QIcon('src/minimize.png'))
                self.minimize_button.setStyleSheet("padding: 10px; border: 0px solid;")
                window_control_layout.addWidget(self.minimize_button)

                # Add custom maximize button
                self.maximize_button = QPushButton()
                self.maximize_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
                self.maximize_button.setIcon(QIcon('src/dock.png'))
                self.maximize_button.setStyleSheet("padding: 10px; border: 0px solid;")
                window_control_layout.addWidget(self.maximize_button)

                # Add custom close button
                self.close_button = QPushButton()
                self.close_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
                self.close_button.setIcon(QIcon('src/close.png'))
                self.close_button.setStyleSheet("padding: 10px; border: 0px solid;")
                window_control_layout.addWidget(self.close_button)


if __name__=="__main__":
        app = QApplication([])
        window = QMainWindow()

        main_widget = QWidget()
        layout = QHBoxLayout()
        
        main_widget.setLayout(layout)
        main_widget.setStyleSheet("background-color: #000")
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,0)
        header = Header()
        layout.addWidget(header)
        window.setCentralWidget(main_widget)
        window.show()

        app.exec()