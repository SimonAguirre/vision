import sys
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QEvent, QPoint, Signal
from PySide6.QtGui import QMouseEvent, QImage, QPixmap
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication, QStackedWidget, QLabel
try:
        from ui_main import Ui_MainWindow
except:
        from gui.ui_main import Ui_MainWindow
from pipeline.constants import Purpose

class GUI(QMainWindow, Ui_MainWindow):
        switch_mode = Signal(tuple)
        isTerminationRequested = False
        _grip_size = 8
        _active_page = 4
        LIVE = True
        PLAYBACK = False
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

                self.header_window_control_widget.installEventFilter(self)
                self.terminate_window.clicked.connect(self.close)
                self.minimize_window.clicked.connect(lambda: self.showMinimized())
                self.dock_window.clicked.connect(lambda: self.showNormal() if self.isMaximized() else self.showMaximized())

                # Setting Up Page Stack
                self.playback_button.clicked.connect(lambda: self.change_current_page(self.playback_page_widget))
                self.live_button.clicked.connect(lambda: self.change_current_page(self.live_page_widget))
                self.model_button.clicked.connect(lambda: self.change_current_page(self.model_page_widget))
                self.charts_button.clicked.connect(lambda: self.change_current_page(self.charts_page_widget))
                self.settings_button.clicked.connect(lambda: self.change_current_page(self.settings_page_widget))

                # Setting Up Sidebar
                self.sidebar_explorer_button_live.clicked.connect(lambda: self.change_current_sidebar(self.side_panel_explorer_widget_live))
                self.sidebar_detections_button_live.clicked.connect(lambda: self.change_current_sidebar(self.side_panel_detections_widget_live))
                self.sidebar_tuning_button_live.clicked.connect(lambda: self.change_current_sidebar(self.side_panel_tuning_widget_live))

                self.sidebar_explorer_button_playback.clicked.connect(lambda: self.change_current_sidebar(self.side_panel_explorer_widget_playback))
                self.sidebar_detections_button_playback.clicked.connect(lambda: self.change_current_sidebar(self.side_panel_detections_widget_playback))
                self.sidebar_tuning_button_playback.clicked.connect(lambda: self.change_current_sidebar(self.side_panel_tuning_widget_playback))
                
                self.content_stack_widget.setCurrentWidget(self.live_page_widget)
                self.side_panel_stack_widget_live.setCurrentWidget(self.side_panel_explorer_widget_live)
                self.side_panel_stack_widget_playback.setCurrentWidget(self.side_panel_explorer_widget_playback)

                self.show()

        def update_preview(self, pack):
                sender, purpose, image = pack
                if self.LIVE:
                        self.live_pixmap_holder.setPixmap(QPixmap.fromImage(image))
                elif self.PLAYBACK:
                        self.playback_pixmap_holder.setPixmap(QPixmap.fromImage(image))

        def change_current_sidebar(self, page: QWidget):
                if self.LIVE:
                        self.side_panel_stack_widget_live.setCurrentWidget(page)
                elif self.PLAYBACK:
                        self.side_panel_stack_widget_playback.setCurrentWidget(page)


        def change_current_page(self, page: QWidget):
                if 'live' in page.objectName():
                        self.LIVE = True
                        self.PLAYBACK = False
                        self.switch_mode.emit(("VIEW",Purpose.UPDATE_PARAMETERS,0))
                elif 'playback' in page.objectName():
                        self.PLAYBACK = True
                        self.LIVE = False
                        self.switch_mode.emit(("VIEW",Purpose.UPDATE_PARAMETERS,r"./videos/traffic_2.mp4"))
                else:
                        self.LIVE = False
                        self.PLAYBACK = False
                        self.switch_mode.emit("STOP")
                self.content_stack_widget.setCurrentWidget(page)
                print(f"{self.LIVE} {self.PLAYBACK}")

        def eventFilter(self, obj, event):
                if event.type() == QEvent.Type.MouseButtonPress:
                        self.oldPos = event.globalPos()
                elif event.type() == QEvent.Type.MouseMove:
                        delta = QPoint(event.globalPos() - self.oldPos)
                        self.move(self.x() + delta.x(), self.y() + delta.y())
                        self.oldPos = event.globalPos()
                return QMainWindow.eventFilter(self, obj, event)
        
if __name__=="__main__":
        app = QApplication(sys.argv)
        gui = GUI()
        sys.exit(app.exec())