from PySide6.QtCore import QObject, Qt
from PySide6.QtWidgets import (QApplication, QComboBox, QFileDialog, QFileSystemModel, QTreeView,
                               QHBoxLayout, QLabel, QMainWindow, QPushButton, QFrame, QStackedLayout,
                               QSizePolicy, QVBoxLayout, QWidget, QSlider, QStackedWidget,
                               QTableWidget, QTableWidgetItem)
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtGui import QFont

from gui.header import Header


class Viewport(QFrame):
        def __init__(self):
                super().__init__()
                self.setStyleSheet(u"QFrame{background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #848484, stop: 0.5 #314932, stop: 1 #0f0f0f); margin: 13 13 13 13;}")
                self.logo = QSvgWidget("gui_res/logo_icon.svg")
                self.logo.setFixedSize(46, 59)
                self.logo.setStyleSheet("background-color: transparent")
                self.main_layout = QVBoxLayout()
                self.main_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
                self.main_layout.addWidget(self.logo)
                self.setLayout(self.main_layout)

        # mousePressed = Signal(tuple)
        # def __init__(self, parent=None):
        #         QLabel.__init__(self, parent)
        #         self.setMinimumSize(640, 480)
        #         self.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        #         self.setScaledContents(True)
        #         self.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)

        # def mousePressEvent(self, event: QMouseEvent) -> None:
        #         active_point = (event.position().x()/self.size().width(), event.position().y()/self.size().height())
        #         self.mousePressed.emit(active_point)

class Button(QPushButton): # for sidebar use only
                def __init__(self, icon) -> None:
                        super().__init__()
                        # self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
                        # self.setStyleSheet("color: rgb(255, 255, 255); font-size: 24px; padding: 0 24px; border: 0px solid;")
                        self.setFixedSize(45, 45)
                        main_layout = QVBoxLayout()
                        main_layout.setSpacing(0)
                        main_layout.setContentsMargins(0, 0, 0, 0)
                        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignCenter)
                        self.setLayout(main_layout)
                        item = QLabel(text = icon)
                        item.setStyleSheet("color: rgb(255, 255, 255); font-size: 22px; padding: 0px; border: 0px solid;")
                        main_layout.addWidget(item)

class SideBar(QFrame):
        def __init__(self) -> None:
                super().__init__()
                self.main_layout = QVBoxLayout()
                self.main_layout.setSpacing(0)
                self.main_layout.setContentsMargins(0,0,0,0)
                self.setStyleSheet("background-color: #393939;")  # Set sidebar background color
                self.setFixedWidth(45)  # Set sidebar width
                self.setLayout(self.main_layout)
                self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        def add_sidebar_button(self, text, slot):
                button = Button(text)
                button.clicked.connect(slot)
                self.main_layout.addWidget(button)
                # button.setStyleSheet("""
                # QPushButton {
                #         padding: 10px;
                #         text-align: left;
                #         border: none;
                #         background-color: transparent;
                #         color: white;
                # }
                # QPushButton:hover {
                #         background-color: #505050;
                # }
                # """)

class LiveMode(QWidget):
        def __init__(self) -> None:
                super().__init__()
                main_layout = QHBoxLayout()
                self.setLayout(main_layout)
                main_layout.setSpacing(0)
                main_layout.setContentsMargins(0,0,0,0)

                # sidebar contents
                self.file_explorer_panel = QWidget()
                self.file_explorer_panel_layout = QVBoxLayout()
                self.file_explorer_panel.setLayout(self.file_explorer_panel_layout)
                model = QFileSystemModel()
                model.setRootPath("")
                tree_view = QTreeView()
                tree_view.setModel(model)
                self.file_explorer_panel_layout.addWidget(tree_view)

                self.detections_panel = QWidget()
                self.detections_panel_layout = QVBoxLayout()
                self.detections_panel.setLayout(self.detections_panel_layout)
                self.detections_panel_layout.addWidget(QLabel("Detections Content"))

                self.layers_panel = QWidget()
                self.layers_panel_layout = QVBoxLayout()
                self.layers_panel.setLayout(self.layers_panel_layout)
                self.layers_panel_layout.addWidget(QLabel("Viewport Layer Settings Content"))

                # sidebar content stack
                self.content_stack = QStackedWidget()
                self.content_stack.setStyleSheet("background-color: #313131;")
                self.content_stack.setMaximumWidth(200)
                self.content_stack.addWidget(self.file_explorer_panel)
                self.content_stack.addWidget(self.detections_panel)
                self.content_stack.addWidget(self.layers_panel)
                self.content_stack.setCurrentIndex(0)

                # sidebar
                self.sidebar = SideBar()
                self.sidebar.add_sidebar_button("E", self.show_file_explorer_panel)
                self.sidebar.add_sidebar_button("D", self.show_detections_panel)
                self.sidebar.add_sidebar_button("L", self.show_layers)

                # viewport
                self.viewport = Viewport()
                main_layout.addWidget(self.sidebar)
                main_layout.addWidget(self.content_stack)
                main_layout.addWidget(self.viewport)
                

        def show_file_explorer_panel(self):
                self.content_stack.setCurrentWidget(self.file_explorer_panel)
        
        def show_detections_panel(self):
                self.content_stack.setCurrentWidget(self.detections_panel)

        def show_layers(self):
                self.content_stack.setCurrentWidget(self.layers_panel)
        


class GUI(object):
        def initializeUI(self, MainWindow: QMainWindow) -> None:
                MainWindow.resize(1280, 720)
                MainWindow.setMinimumSize(839, 480)

                # Set window flags to remove default window decorations
                MainWindow.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint)
                MainWindow.setStyleSheet("background-color: #272727;")
                # Create the central widget area
                self.central_widget = QWidget()

                # Create the main layout for the window
                central_layout = QVBoxLayout()
                central_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero
                central_layout.setSpacing(0)
                self.central_widget.setLayout(central_layout)

                # Create header
                self.header = Header()

                # Create contents widget
                self.content = QStackedWidget()

                self.page_live = LiveMode()

                # placeholder_layout_live = QVBoxLayout()
                # self.page_live.setLayout(placeholder_layout_live)
                # placeholder_label_page_live = QLabel("PAGE 1")
                # placeholder_font_page_live = QFont()
                # placeholder_font_page_live.setPointSize(40)
                # placeholder_label_page_live.setFont(placeholder_font_page_live)
                # placeholder_label_page_live.setStyleSheet("color: #000;")
                # placeholder_label_page_live.setAlignment(Qt.AlignmentFlag.AlignCenter)
                # placeholder_layout_live.addWidget(placeholder_label_page_live)

                self.content.addWidget(self.page_live)

                self.page_playback = QWidget()
                placeholder_layout_playback = QVBoxLayout()
                self.page_playback.setLayout(placeholder_layout_playback)

                placeholder_label_page_playback = QLabel("PAGE 2")
                placeholder_font_page_playback = QFont()
                placeholder_font_page_playback.setPointSize(40)
                placeholder_label_page_playback.setFont(placeholder_font_page_playback)
                placeholder_label_page_playback.setStyleSheet("color: #000;")
                placeholder_label_page_playback.setAlignment(Qt.AlignmentFlag.AlignCenter)
                placeholder_layout_playback.addWidget(placeholder_label_page_playback)
                self.content.addWidget(self.page_playback)

                self.content.setCurrentIndex(0)
                central_layout.addWidget(self.header)
                central_layout.addWidget(self.content)

                self.retranslateUI(MainWindow)

        def retranslateUI(self, MainWindow: QMainWindow):
                MainWindow.setWindowTitle(QApplication.translate("MainWindow", "Vision Drive", None))
                
                self.header.minimize_button.setText(QApplication.translate("MainWindow", "-", None))
                self.header.maximize_button.setText(QApplication.translate("MainWindow", "+", None))
                self.header.close_button.setText(QApplication.translate("MainWindow", "x", None))

                self.header.live_button.setText(QApplication.translate("MainWindow", "LIVE", None))
                self.header.playback_button.setText(QApplication.translate("MainWindow", "PLAYBACK", None))