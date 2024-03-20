from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import (QTabBar, QStylePainter, QStyleOptionTab, QApplication, QStyle,
                               QTabWidget,QLabel
                               )
from PySide6.QtGui import QIcon

import sys

class SideTabBar(QTabBar):
    def __init__(self, *args, **kwargs):
        self.tabSize = QtCore.QSize(kwargs.pop('width'), kwargs.pop('height'))
        super().__init__(*args, **kwargs)
        

    def paintEvent(self, event):
        painter = QStylePainter(self)
        option = QStyleOptionTab()

        for index in range(self.count()):
            self.initStyleOption(option, index)
            tabRect = self.tabRect(index)
            painter.drawControl(QStyle.ControlElement.CE_TabBarTabShape, option)
            painter.drawText(tabRect, QtCore.Qt.AlignmentFlag.AlignVCenter | QtCore.Qt.TextFlag.TextDontClip, self.tabText(index))
            painter.drawPixmap()

    def tabSizeHint(self,index):
        return self.tabSize


if __name__=="__main__":
    app = QApplication(sys.argv)
    sidepanel = QTabWidget()
    sidepanel.setTabBar(SideTabBar(width=45,height=45))

    sidebar_items = [('Explorer','src/svg/explorer.svg'),('Detections', 'src/svg/detections.svg'),('Tuning', 'src/svg/tuning.svg')]

    for i,d in enumerate(iterable=sidebar_items):
        name, icon_path = d
        widget =  QLabel(f"Area {i} {name} Page")
        sidepanel.addTab(widget, QIcon(icon_path), name[0])

    sidepanel.setTabPosition(QTabWidget.TabPosition.West)
    sidepanel.show()
    sys.exit(app.exec())