from ast import main
from PySide6.QtCore import QEvent, QObject, Qt, QTimer, QSize
from PySide6.QtWidgets import (QApplication, QComboBox, QFileDialog, QFileSystemModel, QTreeView,
                               QHBoxLayout, QLabel, QMainWindow, QPushButton, QFrame, QStackedLayout,
                               QSizePolicy, QVBoxLayout, QWidget, QSlider, QStackedWidget, QTabBar, QTabWidget, QStylePainter, QStyleOptionTab,
                               QTableWidget, QTableWidgetItem)
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtGui import QEnterEvent, QFont, QIcon


class SideBarButton(QPushButton):
        def __init__(self, icon_path) -> None:
                super().__init__()
                self.setStyleSheet("""SideBarButton {
                                   border: none;
                                   background-color:transparent;
                                   }
                                   """)
                self._icon_path = icon_path[:-4]+"_60"+".svg"
                self.setFixedSize(45, 45)
                self.setIcon(QIcon(self._icon_path))
                self.setIconSize(QSize(25,25))
                self._hover_icon = QIcon(icon_path[:-4]+"_white"+".svg" )

        def enterEvent(self, event: QEnterEvent) -> None:
                self.setIcon(self._hover_icon)
                return super().enterEvent(event)
        def leaveEvent(self, event: QEvent) -> None:
                self.setIcon(QIcon(self._icon_path))
                return super().leaveEvent(event)

class SidePanelWidget(QStackedWidget):
        def __init__(self) -> None:
                super().__init__()

class SidePanelTabs(QFrame):
        def __init__(self) -> None:
                super().__init__()
                self.setLayout(QVBoxLayout())
                # set layout settings
                self.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
                self.layout().setSpacing(0)
                self.layout().setContentsMargins(0,0,0,0)

                # set frame style
                self.setStyleSheet("background-color: #333;")
                self.setFixedWidth(45)


class SidePanel(QWidget):
        def __init__(self):
                super().__init__()
                self.stack = SidePanelWidget()
                self.stack.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
                self.bar = SidePanelTabs()
                self.setLayout(QHBoxLayout())
                self.layout().setSpacing(0)
                self.layout().setContentsMargins(0,0,0,0)
                self.layout().addWidget(self.bar)
                self.layout().addWidget(self.stack)

        def addTab(self, widget, tab_icon_path):
                self.stack.layout().addWidget(widget)
                button = SideBarButton(tab_icon_path)
                self.bar.layout().addWidget(button)
                button.clicked.connect(lambda: self.stack.setCurrentWidget(widget))

def hide_widget():
        side_panel.stack.hide()

if __name__=="__main__":
        app = QApplication([])
        window = QMainWindow()

        main_widget = QWidget()
        layout = QHBoxLayout()
        
        main_widget.setLayout(layout)
        main_widget.setStyleSheet("background-color: #000")
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,0)
        

        SIDE_PANEL_CONTENTS = [('Explorer Side Panel', 'src/svg/explorer.svg'), ('Detections Side Panel', 'src/svg/detections.svg'), ('Tuning Side Panel', 'src/svg/tuning.svg')]

        side_panel = SidePanel()
        side_panel.setObjectName("Side Panel")

        explorer = QWidget(side_panel)
        explorer.setStyleSheet("background-color: #00f")
        explorer.setObjectName("Explorer Side Panel")
        detections = QWidget(side_panel)
        detections.setStyleSheet("background-color: #0f0")
        detections.setObjectName("Detections Side Panel")
        tuning = QWidget(side_panel)
        tuning.setStyleSheet("background-color: #f00")
        tuning.setObjectName("Tuning Side Panel")

        for index, item in enumerate(SIDE_PANEL_CONTENTS):
                name, svg_path = item
                widget = side_panel.findChild(QWidget, name)
                side_panel.addTab(widget, svg_path)

        layout.addWidget(side_panel)
        window.setCentralWidget(main_widget)
        window.show()

        app.exec()