# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWOHkgD.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSplitter, QStackedWidget,
    QTabWidget, QToolButton, QTreeView, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)
try:
        import icons_rc
except:
        import gui.icons_rc
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1013, 725)
        MainWindow.setFocusPolicy(Qt.NoFocus)
        MainWindow.setStyleSheet(u"")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockOptions(QMainWindow.AllowNestedDocks|QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_window_control_widget = QWidget(self.centralwidget)
        self.header_window_control_widget.setObjectName(u"header_window_control_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_window_control_widget.sizePolicy().hasHeightForWidth())
        self.header_window_control_widget.setSizePolicy(sizePolicy)
        self.header_window_control_widget.setStyleSheet(u"background: #282828")
        self.horizontalLayout_3 = QHBoxLayout(self.header_window_control_widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.window_title_label = QLabel(self.header_window_control_widget)
        self.window_title_label.setObjectName(u"window_title_label")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        self.window_title_label.setFont(font)
        self.window_title_label.setStyleSheet(u"color: white")
        self.window_title_label.setTextFormat(Qt.PlainText)
        self.window_title_label.setMargin(0)
        self.window_title_label.setIndent(15)

        self.horizontalLayout_3.addWidget(self.window_title_label)

        self.header_window_control_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.header_window_control_spacer)

        self.minimize_window = QPushButton(self.header_window_control_widget)
        self.minimize_window.setObjectName(u"minimize_window")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.minimize_window.sizePolicy().hasHeightForWidth())
        self.minimize_window.setSizePolicy(sizePolicy1)
        self.minimize_window.setStyleSheet(u"QAbstractButton{border: 0px; padding: 3px 10px}\n"
"QAbstractButton:hover{background-color: #333}")
        icon = QIcon()
        icon.addFile(u":/buttons/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.minimize_window)

        self.dock_window = QPushButton(self.header_window_control_widget)
        self.dock_window.setObjectName(u"dock_window")
        sizePolicy1.setHeightForWidth(self.dock_window.sizePolicy().hasHeightForWidth())
        self.dock_window.setSizePolicy(sizePolicy1)
        self.dock_window.setStyleSheet(u"QAbstractButton{border: 0px; padding: 3px 10px}\n"
"QAbstractButton:hover{background-color: #333}")
        icon1 = QIcon()
        icon1.addFile(u":/buttons/dock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dock_window.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.dock_window)

        self.terminate_window = QPushButton(self.header_window_control_widget)
        self.terminate_window.setObjectName(u"terminate_window")
        sizePolicy1.setHeightForWidth(self.terminate_window.sizePolicy().hasHeightForWidth())
        self.terminate_window.setSizePolicy(sizePolicy1)
        self.terminate_window.setStyleSheet(u"QAbstractButton{border: 0px; padding: 3px 10px}\n"
"QAbstractButton:hover{background-color: #c00}")
        icon2 = QIcon()
        icon2.addFile(u":/buttons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.terminate_window.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.terminate_window)


        self.verticalLayout.addWidget(self.header_window_control_widget)

        self.header_widget = QWidget(self.centralwidget)
        self.header_widget.setObjectName(u"header_widget")
        sizePolicy.setHeightForWidth(self.header_widget.sizePolicy().hasHeightForWidth())
        self.header_widget.setSizePolicy(sizePolicy)
        self.header_widget.setStyleSheet(u"background: #282828")
        self.horizontalLayout_2 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(9, 0, 19, 0)
        self.header_logo = QPushButton(self.header_widget)
        self.header_logo.setObjectName(u"header_logo")
        self.header_logo.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.header_logo.sizePolicy().hasHeightForWidth())
        self.header_logo.setSizePolicy(sizePolicy2)
        icon3 = QIcon()
        icon3.addFile(u":/logo/svg/logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.header_logo.setIcon(icon3)
        self.header_logo.setIconSize(QSize(49, 54))
        self.header_logo.setFlat(True)

        self.horizontalLayout_2.addWidget(self.header_logo)

        self.header_tabs_widget = QHBoxLayout()
        self.header_tabs_widget.setSpacing(10)
        self.header_tabs_widget.setObjectName(u"header_tabs_widget")
        self.header_tabs_widget.setContentsMargins(10, 9, 10, 0)
        self.settings_button = QToolButton(self.header_widget)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setEnabled(True)
        sizePolicy.setHeightForWidth(self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.settings_button.setFont(font1)
        self.settings_button.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.settings_button.setStyleSheet(u"QToolButton {background-color: transparent; color: #aaa; }QToolButton::hover{color: #fff;}")
        icon4 = QIcon()
        icon4.addFile(u":/buttons/svg/settings_60.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button.setIcon(icon4)
        self.settings_button.setIconSize(QSize(52, 25))
        self.settings_button.setCheckable(False)
        self.settings_button.setChecked(False)
        self.settings_button.setAutoRepeat(False)
        self.settings_button.setPopupMode(QToolButton.DelayedPopup)
        self.settings_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.settings_button.setAutoRaise(True)
        self.settings_button.setArrowType(Qt.NoArrow)

        self.header_tabs_widget.addWidget(self.settings_button)

        self.charts_button = QToolButton(self.header_widget)
        self.charts_button.setObjectName(u"charts_button")
        self.charts_button.setEnabled(True)
        sizePolicy.setHeightForWidth(self.charts_button.sizePolicy().hasHeightForWidth())
        self.charts_button.setSizePolicy(sizePolicy)
        self.charts_button.setFont(font1)
        self.charts_button.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.charts_button.setStyleSheet(u"QToolButton {background-color: transparent; color: #aaa; }QToolButton::hover{color: #fff;}")
        icon5 = QIcon()
        icon5.addFile(u":/buttons/svg/charts_60.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.charts_button.setIcon(icon5)
        self.charts_button.setIconSize(QSize(52, 25))
        self.charts_button.setCheckable(False)
        self.charts_button.setChecked(False)
        self.charts_button.setAutoRepeat(False)
        self.charts_button.setPopupMode(QToolButton.DelayedPopup)
        self.charts_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.charts_button.setAutoRaise(False)
        self.charts_button.setArrowType(Qt.NoArrow)

        self.header_tabs_widget.addWidget(self.charts_button)

        self.model_button = QToolButton(self.header_widget)
        self.model_button.setObjectName(u"model_button")
        self.model_button.setEnabled(True)
        sizePolicy.setHeightForWidth(self.model_button.sizePolicy().hasHeightForWidth())
        self.model_button.setSizePolicy(sizePolicy)
        self.model_button.setFont(font1)
        self.model_button.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.model_button.setStyleSheet(u"QToolButton {background-color: transparent; color: #aaa; }QToolButton::hover{color: #fff;}")
        icon6 = QIcon()
        icon6.addFile(u":/buttons/svg/model_60.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.model_button.setIcon(icon6)
        self.model_button.setIconSize(QSize(52, 25))
        self.model_button.setCheckable(False)
        self.model_button.setChecked(False)
        self.model_button.setAutoRepeat(False)
        self.model_button.setPopupMode(QToolButton.DelayedPopup)
        self.model_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.model_button.setAutoRaise(False)
        self.model_button.setArrowType(Qt.NoArrow)

        self.header_tabs_widget.addWidget(self.model_button)

        self.playback_button = QToolButton(self.header_widget)
        self.playback_button.setObjectName(u"playback_button")
        self.playback_button.setEnabled(True)
        sizePolicy.setHeightForWidth(self.playback_button.sizePolicy().hasHeightForWidth())
        self.playback_button.setSizePolicy(sizePolicy)
        self.playback_button.setFont(font1)
        self.playback_button.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.playback_button.setStyleSheet(u"QToolButton {background-color: transparent; color: #aaa; }QToolButton::hover{color: #fff;}")
        icon7 = QIcon()
        icon7.addFile(u":/buttons/svg/playback_60.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.playback_button.setIcon(icon7)
        self.playback_button.setIconSize(QSize(52, 25))
        self.playback_button.setCheckable(False)
        self.playback_button.setChecked(False)
        self.playback_button.setAutoRepeat(False)
        self.playback_button.setPopupMode(QToolButton.DelayedPopup)
        self.playback_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.playback_button.setAutoRaise(False)
        self.playback_button.setArrowType(Qt.NoArrow)

        self.header_tabs_widget.addWidget(self.playback_button)

        self.live_button = QToolButton(self.header_widget)
        self.live_button.setObjectName(u"live_button")
        self.live_button.setEnabled(True)
        sizePolicy.setHeightForWidth(self.live_button.sizePolicy().hasHeightForWidth())
        self.live_button.setSizePolicy(sizePolicy)
        self.live_button.setFont(font1)
        self.live_button.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.live_button.setStyleSheet(u"QToolButton {background-color: transparent; color: #aaa; }QToolButton::hover{color: #fff;}")
        icon8 = QIcon()
        icon8.addFile(u":/buttons/svg/live_60.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.live_button.setIcon(icon8)
        self.live_button.setIconSize(QSize(52, 25))
        self.live_button.setCheckable(False)
        self.live_button.setChecked(False)
        self.live_button.setAutoRepeat(False)
        self.live_button.setPopupMode(QToolButton.DelayedPopup)
        self.live_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.live_button.setAutoRaise(False)
        self.live_button.setArrowType(Qt.NoArrow)

        self.header_tabs_widget.addWidget(self.live_button)

        self.header_tabs_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.header_tabs_widget.addItem(self.header_tabs_spacer)


        self.horizontalLayout_2.addLayout(self.header_tabs_widget)


        self.verticalLayout.addWidget(self.header_widget)

        self.content_stack_widget = QStackedWidget(self.centralwidget)
        self.content_stack_widget.setObjectName(u"content_stack_widget")
        self.content_stack_widget.setStyleSheet(u"QWidget{background: #000} QCheckBox{color: #000;}")
        self.live_page_widget = QWidget()
        self.live_page_widget.setObjectName(u"live_page_widget")
        self.horizontalLayout_5 = QHBoxLayout(self.live_page_widget)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.side_bar_widget_live = QWidget(self.live_page_widget)
        self.side_bar_widget_live.setObjectName(u"side_bar_widget_live")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.side_bar_widget_live.sizePolicy().hasHeightForWidth())
        self.side_bar_widget_live.setSizePolicy(sizePolicy3)
        self.side_bar_widget_live.setStyleSheet(u"background-color: #393939")
        self.verticalLayout_13 = QVBoxLayout(self.side_bar_widget_live)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.sidebar_explorer_button_live = QPushButton(self.side_bar_widget_live)
        self.sidebar_explorer_button_live.setObjectName(u"sidebar_explorer_button_live")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.sidebar_explorer_button_live.sizePolicy().hasHeightForWidth())
        self.sidebar_explorer_button_live.setSizePolicy(sizePolicy4)
        self.sidebar_explorer_button_live.setMinimumSize(QSize(45, 45))
        self.sidebar_explorer_button_live.setStyleSheet(u"background-color: transparent")
        icon9 = QIcon()
        icon9.addFile(u":/buttons/svg/explorer_60.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sidebar_explorer_button_live.setIcon(icon9)
        self.sidebar_explorer_button_live.setIconSize(QSize(25, 25))

        self.verticalLayout_13.addWidget(self.sidebar_explorer_button_live)

        self.sidebar_detections_button_live = QPushButton(self.side_bar_widget_live)
        self.sidebar_detections_button_live.setObjectName(u"sidebar_detections_button_live")
        sizePolicy2.setHeightForWidth(self.sidebar_detections_button_live.sizePolicy().hasHeightForWidth())
        self.sidebar_detections_button_live.setSizePolicy(sizePolicy2)
        self.sidebar_detections_button_live.setMinimumSize(QSize(45, 45))
        self.sidebar_detections_button_live.setStyleSheet(u"background-color: transparent")
        icon10 = QIcon()
        icon10.addFile(u":/buttons/svg/detections_60.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sidebar_detections_button_live.setIcon(icon10)
        self.sidebar_detections_button_live.setIconSize(QSize(25, 25))

        self.verticalLayout_13.addWidget(self.sidebar_detections_button_live)

        self.sidebar_tuning_button_live = QPushButton(self.side_bar_widget_live)
        self.sidebar_tuning_button_live.setObjectName(u"sidebar_tuning_button_live")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.sidebar_tuning_button_live.sizePolicy().hasHeightForWidth())
        self.sidebar_tuning_button_live.setSizePolicy(sizePolicy5)
        self.sidebar_tuning_button_live.setMinimumSize(QSize(45, 45))
        self.sidebar_tuning_button_live.setStyleSheet(u"background-color: transparent")
        icon11 = QIcon()
        icon11.addFile(u":/buttons/svg/tuning_60.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sidebar_tuning_button_live.setIcon(icon11)
        self.sidebar_tuning_button_live.setIconSize(QSize(25, 25))

        self.verticalLayout_13.addWidget(self.sidebar_tuning_button_live)

        self.side_bar_widget_spacer_live = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.side_bar_widget_spacer_live)


        self.horizontalLayout_5.addWidget(self.side_bar_widget_live)

        self.splitter = QSplitter(self.live_page_widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.side_panel_stack_widget_live = QStackedWidget(self.splitter)
        self.side_panel_stack_widget_live.setObjectName(u"side_panel_stack_widget_live")
        sizePolicy1.setHeightForWidth(self.side_panel_stack_widget_live.sizePolicy().hasHeightForWidth())
        self.side_panel_stack_widget_live.setSizePolicy(sizePolicy1)
        self.side_panel_stack_widget_live.setMinimumSize(QSize(200, 0))
        self.side_panel_stack_widget_live.setStyleSheet(u"background-color: #313131")
        self.side_panel_detections_widget_live = QWidget()
        self.side_panel_detections_widget_live.setObjectName(u"side_panel_detections_widget_live")
        self.verticalLayout_14 = QVBoxLayout(self.side_panel_detections_widget_live)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.detections_side_panel_label_live = QLabel(self.side_panel_detections_widget_live)
        self.detections_side_panel_label_live.setObjectName(u"detections_side_panel_label_live")
        sizePolicy.setHeightForWidth(self.detections_side_panel_label_live.sizePolicy().hasHeightForWidth())
        self.detections_side_panel_label_live.setSizePolicy(sizePolicy)
        self.detections_side_panel_label_live.setStyleSheet(u"color: #aaa; padding: 10 0 3 0")

        self.verticalLayout_14.addWidget(self.detections_side_panel_label_live)

        self.detections_incoming_treewidget_live = QTreeWidget(self.side_panel_detections_widget_live)
        icon12 = QIcon()
        iconThemeName = u"address-book-new"
        if QIcon.hasThemeIcon(iconThemeName):
            icon12 = QIcon.fromTheme(iconThemeName)
        else:
            icon12.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        font2 = QFont()
        font2.setBold(True)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem.setFont(1, font2);
        __qtreewidgetitem.setFont(0, font2);
        __qtreewidgetitem.setIcon(0, icon12);
        self.detections_incoming_treewidget_live.setHeaderItem(__qtreewidgetitem)
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setStyleStrategy(QFont.PreferAntialias)
        __qtreewidgetitem1 = QTreeWidgetItem(self.detections_incoming_treewidget_live)
        __qtreewidgetitem1.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem2 = QTreeWidgetItem(self.detections_incoming_treewidget_live)
        __qtreewidgetitem2.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem2.setFont(1, font3);
        __qtreewidgetitem3 = QTreeWidgetItem(self.detections_incoming_treewidget_live)
        __qtreewidgetitem3.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem4 = QTreeWidgetItem(self.detections_incoming_treewidget_live)
        __qtreewidgetitem4.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem5 = QTreeWidgetItem(self.detections_incoming_treewidget_live)
        __qtreewidgetitem5.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem6 = QTreeWidgetItem(self.detections_incoming_treewidget_live)
        __qtreewidgetitem6.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem7 = QTreeWidgetItem(self.detections_incoming_treewidget_live)
        __qtreewidgetitem7.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem8 = QTreeWidgetItem(self.detections_incoming_treewidget_live)
        __qtreewidgetitem8.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem9 = QTreeWidgetItem(self.detections_incoming_treewidget_live)
        __qtreewidgetitem9.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        self.detections_incoming_treewidget_live.setObjectName(u"detections_incoming_treewidget_live")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.detections_incoming_treewidget_live.sizePolicy().hasHeightForWidth())
        self.detections_incoming_treewidget_live.setSizePolicy(sizePolicy6)
        self.detections_incoming_treewidget_live.setStyleSheet(u"QTreeWidget{color: #ddd; color: #aaa; border: 0; padding: 0 15}\n"
"QHeaderView::section{background-color: transparent; color: #ddd}\n"
"")
        self.detections_incoming_treewidget_live.setIndentation(10)
        self.detections_incoming_treewidget_live.setUniformRowHeights(True)
        self.detections_incoming_treewidget_live.setItemsExpandable(False)
        self.detections_incoming_treewidget_live.setAnimated(True)
        self.detections_incoming_treewidget_live.header().setVisible(True)
        self.detections_incoming_treewidget_live.header().setDefaultSectionSize(80)
        self.detections_incoming_treewidget_live.header().setProperty("showSortIndicator", False)
        self.detections_incoming_treewidget_live.header().setStretchLastSection(True)

        self.verticalLayout_14.addWidget(self.detections_incoming_treewidget_live)

        self.detections_outgoing_treewidget_live = QTreeWidget(self.side_panel_detections_widget_live)
        __qtreewidgetitem10 = QTreeWidgetItem()
        __qtreewidgetitem10.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem10.setFont(1, font2);
        __qtreewidgetitem10.setFont(0, font2);
        self.detections_outgoing_treewidget_live.setHeaderItem(__qtreewidgetitem10)
        __qtreewidgetitem11 = QTreeWidgetItem(self.detections_outgoing_treewidget_live)
        __qtreewidgetitem11.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem12 = QTreeWidgetItem(self.detections_outgoing_treewidget_live)
        __qtreewidgetitem12.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem12.setFont(1, font3);
        __qtreewidgetitem13 = QTreeWidgetItem(self.detections_outgoing_treewidget_live)
        __qtreewidgetitem13.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem14 = QTreeWidgetItem(self.detections_outgoing_treewidget_live)
        __qtreewidgetitem14.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem15 = QTreeWidgetItem(self.detections_outgoing_treewidget_live)
        __qtreewidgetitem15.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem16 = QTreeWidgetItem(self.detections_outgoing_treewidget_live)
        __qtreewidgetitem16.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem17 = QTreeWidgetItem(self.detections_outgoing_treewidget_live)
        __qtreewidgetitem17.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem18 = QTreeWidgetItem(self.detections_outgoing_treewidget_live)
        __qtreewidgetitem18.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem19 = QTreeWidgetItem(self.detections_outgoing_treewidget_live)
        __qtreewidgetitem19.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        self.detections_outgoing_treewidget_live.setObjectName(u"detections_outgoing_treewidget_live")
        sizePolicy6.setHeightForWidth(self.detections_outgoing_treewidget_live.sizePolicy().hasHeightForWidth())
        self.detections_outgoing_treewidget_live.setSizePolicy(sizePolicy6)
        self.detections_outgoing_treewidget_live.setStyleSheet(u"QTreeWidget{color: #ddd; color: #aaa; border: 0; padding: 0 15}\n"
"QHeaderView::section{background-color: transparent; color: #ddd}")
        self.detections_outgoing_treewidget_live.setIndentation(10)
        self.detections_outgoing_treewidget_live.setUniformRowHeights(True)
        self.detections_outgoing_treewidget_live.setItemsExpandable(False)
        self.detections_outgoing_treewidget_live.setAnimated(True)
        self.detections_outgoing_treewidget_live.header().setVisible(True)
        self.detections_outgoing_treewidget_live.header().setDefaultSectionSize(80)
        self.detections_outgoing_treewidget_live.header().setProperty("showSortIndicator", False)
        self.detections_outgoing_treewidget_live.header().setStretchLastSection(True)

        self.verticalLayout_14.addWidget(self.detections_outgoing_treewidget_live)

        self.side_panel_detections_widget_spacer_live = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.side_panel_detections_widget_spacer_live)

        self.side_panel_stack_widget_live.addWidget(self.side_panel_detections_widget_live)
        self.side_panel_tuning_widget_live = QWidget()
        self.side_panel_tuning_widget_live.setObjectName(u"side_panel_tuning_widget_live")
        self.side_panel_tuning_widget_live.setStyleSheet(u"QLabel {color: #ddd; padding: 5 0 0 15}\n"
"QCheckBox{padding: 5 15 0 0}\n"
"QSlider{padding: 5 15 0 0}")
        self.gridLayout_4 = QGridLayout(self.side_panel_tuning_widget_live)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.threshold_label_live = QLabel(self.side_panel_tuning_widget_live)
        self.threshold_label_live.setObjectName(u"threshold_label_live")
        self.threshold_label_live.setFont(font2)
        self.threshold_label_live.setStyleSheet(u"color: #ddd; padding: 5 0 0 15")

        self.gridLayout_4.addWidget(self.threshold_label_live, 5, 0, 1, 2)

        self.confidence_label_live = QLabel(self.side_panel_tuning_widget_live)
        self.confidence_label_live.setObjectName(u"confidence_label_live")
        self.confidence_label_live.setStyleSheet(u"color: #ddd; padding: 5 0 0 25")

        self.gridLayout_4.addWidget(self.confidence_label_live, 6, 0, 1, 1)

        self.confidence_slider_live = QSlider(self.side_panel_tuning_widget_live)
        self.confidence_slider_live.setObjectName(u"confidence_slider_live")
        self.confidence_slider_live.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height: 4px;\n"
"    margin: 0 0 0 28px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ddd, stop:1 #f6f6f6);\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #A0C334, stop:1 #A0C334);\n"
"    width: 14px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #A0C334, stop:1 #A0C334);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #A0C334, stop:1 #E5D429);\n"
"}")
        self.confidence_slider_live.setMaximum(100)
        self.confidence_slider_live.setValue(55)
        self.confidence_slider_live.setOrientation(Qt.Horizontal)
        self.confidence_slider_live.setTickPosition(QSlider.NoTicks)

        self.gridLayout_4.addWidget(self.confidence_slider_live, 7, 0, 1, 2)

        self.label_checkbox_live = QCheckBox(self.side_panel_tuning_widget_live)
        self.label_checkbox_live.setObjectName(u"label_checkbox_live")
        sizePolicy2.setHeightForWidth(self.label_checkbox_live.sizePolicy().hasHeightForWidth())
        self.label_checkbox_live.setSizePolicy(sizePolicy2)
        self.label_checkbox_live.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_4.addWidget(self.label_checkbox_live, 2, 1, 1, 1)

        self.overlap_label_live = QLabel(self.side_panel_tuning_widget_live)
        self.overlap_label_live.setObjectName(u"overlap_label_live")
        self.overlap_label_live.setStyleSheet(u"color: #ddd; padding: 5 0 0 25")

        self.gridLayout_4.addWidget(self.overlap_label_live, 8, 0, 1, 1)

        self.confidence_value_label_live = QLabel(self.side_panel_tuning_widget_live)
        self.confidence_value_label_live.setObjectName(u"confidence_value_label_live")
        self.confidence_value_label_live.setStyleSheet(u"color: #ddd; padding: 5 15 0 0")
        self.confidence_value_label_live.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.confidence_value_label_live, 6, 1, 1, 1)

        self.bounding_box_checkbox_live = QCheckBox(self.side_panel_tuning_widget_live)
        self.bounding_box_checkbox_live.setObjectName(u"bounding_box_checkbox_live")
        sizePolicy2.setHeightForWidth(self.bounding_box_checkbox_live.sizePolicy().hasHeightForWidth())
        self.bounding_box_checkbox_live.setSizePolicy(sizePolicy2)
        self.bounding_box_checkbox_live.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_4.addWidget(self.bounding_box_checkbox_live, 4, 1, 1, 1)

        self.tracking_checkbox_live = QCheckBox(self.side_panel_tuning_widget_live)
        self.tracking_checkbox_live.setObjectName(u"tracking_checkbox_live")
        sizePolicy2.setHeightForWidth(self.tracking_checkbox_live.sizePolicy().hasHeightForWidth())
        self.tracking_checkbox_live.setSizePolicy(sizePolicy2)
        self.tracking_checkbox_live.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_4.addWidget(self.tracking_checkbox_live, 3, 1, 1, 1)

        self.overlap_value_label_live = QLabel(self.side_panel_tuning_widget_live)
        self.overlap_value_label_live.setObjectName(u"overlap_value_label_live")
        self.overlap_value_label_live.setStyleSheet(u"color: #ddd; padding: 5 15 0 0")
        self.overlap_value_label_live.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.overlap_value_label_live, 8, 1, 1, 1)

        self.overlap_slider_live = QSlider(self.side_panel_tuning_widget_live)
        self.overlap_slider_live.setObjectName(u"overlap_slider_live")
        self.overlap_slider_live.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height: 4px;\n"
"    margin: 0 0 0 28px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ddd, stop:1 #f6f6f6);\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #A0C334, stop:1 #A0C334);\n"
"    width: 14px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #A0C334, stop:1 #A0C334);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #A0C334, stop:1 #E5D429);\n"
"}")
        self.overlap_slider_live.setMaximum(100)
        self.overlap_slider_live.setValue(55)
        self.overlap_slider_live.setOrientation(Qt.Horizontal)
        self.overlap_slider_live.setTickPosition(QSlider.NoTicks)

        self.gridLayout_4.addWidget(self.overlap_slider_live, 9, 0, 1, 2)

        self.label_label_live = QLabel(self.side_panel_tuning_widget_live)
        self.label_label_live.setObjectName(u"label_label_live")
        self.label_label_live.setStyleSheet(u"color: #ddd; padding: 5 0 0 25")

        self.gridLayout_4.addWidget(self.label_label_live, 2, 0, 1, 1)

        self.bounding_box_label_live = QLabel(self.side_panel_tuning_widget_live)
        self.bounding_box_label_live.setObjectName(u"bounding_box_label_live")
        self.bounding_box_label_live.setStyleSheet(u"color: #ddd; padding: 5 0 0 25")

        self.gridLayout_4.addWidget(self.bounding_box_label_live, 4, 0, 1, 1)

        self.side_panel_tuning_widget_spacer_live = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.side_panel_tuning_widget_spacer_live, 10, 0, 1, 2)

        self.tracking_label_live = QLabel(self.side_panel_tuning_widget_live)
        self.tracking_label_live.setObjectName(u"tracking_label_live")
        self.tracking_label_live.setStyleSheet(u"color: #ddd; padding: 5 0 0 25")

        self.gridLayout_4.addWidget(self.tracking_label_live, 3, 0, 1, 1)

        self.visible_layers_label_live = QLabel(self.side_panel_tuning_widget_live)
        self.visible_layers_label_live.setObjectName(u"visible_layers_label_live")
        self.visible_layers_label_live.setFont(font2)
        self.visible_layers_label_live.setStyleSheet(u"color: #ddd; padding: 5 0 0 15")

        self.gridLayout_4.addWidget(self.visible_layers_label_live, 1, 0, 1, 2)

        self.tuning_side_panel_live = QLabel(self.side_panel_tuning_widget_live)
        self.tuning_side_panel_live.setObjectName(u"tuning_side_panel_live")
        sizePolicy.setHeightForWidth(self.tuning_side_panel_live.sizePolicy().hasHeightForWidth())
        self.tuning_side_panel_live.setSizePolicy(sizePolicy)
        self.tuning_side_panel_live.setStyleSheet(u"color: #aaa; padding: 10 0 3 0")

        self.gridLayout_4.addWidget(self.tuning_side_panel_live, 0, 0, 1, 2)

        self.side_panel_stack_widget_live.addWidget(self.side_panel_tuning_widget_live)
        self.side_panel_explorer_widget_live = QWidget()
        self.side_panel_explorer_widget_live.setObjectName(u"side_panel_explorer_widget_live")
        self.verticalLayout_15 = QVBoxLayout(self.side_panel_explorer_widget_live)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.explorer_side_panel_label_live = QLabel(self.side_panel_explorer_widget_live)
        self.explorer_side_panel_label_live.setObjectName(u"explorer_side_panel_label_live")
        sizePolicy.setHeightForWidth(self.explorer_side_panel_label_live.sizePolicy().hasHeightForWidth())
        self.explorer_side_panel_label_live.setSizePolicy(sizePolicy)
        self.explorer_side_panel_label_live.setStyleSheet(u"color: #aaa; padding: 10 0 3 0")

        self.verticalLayout_15.addWidget(self.explorer_side_panel_label_live)

        self.filesystem_treeview_live = QTreeView(self.side_panel_explorer_widget_live)
        self.filesystem_treeview_live.setObjectName(u"filesystem_treeview_live")
        self.filesystem_treeview_live.setMinimumSize(QSize(200, 0))
        self.filesystem_treeview_live.setFrameShape(QFrame.NoFrame)
        self.filesystem_treeview_live.setAutoScroll(False)
        self.filesystem_treeview_live.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.filesystem_treeview_live.setSelectionMode(QAbstractItemView.NoSelection)
        self.filesystem_treeview_live.setTextElideMode(Qt.ElideNone)
        self.filesystem_treeview_live.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_15.addWidget(self.filesystem_treeview_live)

        self.side_panel_stack_widget_live.addWidget(self.side_panel_explorer_widget_live)
        self.splitter.addWidget(self.side_panel_stack_widget_live)
        self.viewport_widget_live = QWidget(self.splitter)
        self.viewport_widget_live.setObjectName(u"viewport_widget_live")
        self.viewport_widget_live.setMinimumSize(QSize(500, 0))
        self.viewport_widget_live.setStyleSheet(u"background-color: #464646")
        self.gridLayout_6 = QGridLayout(self.viewport_widget_live)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.viewport_widget_live)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_9 = QVBoxLayout(self.widget_5)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.source_name_label_live = QLabel(self.widget_5)
        self.source_name_label_live.setObjectName(u"source_name_label_live")
        sizePolicy.setHeightForWidth(self.source_name_label_live.sizePolicy().hasHeightForWidth())
        self.source_name_label_live.setSizePolicy(sizePolicy)
        self.source_name_label_live.setStyleSheet(u"background-color: #000;\n"
"color: #aaa;\n"
"padding: 2 15 2 15")

        self.verticalLayout_9.addWidget(self.source_name_label_live)

        self.live_pixmap_holder = QLabel(self.widget_5)
        self.live_pixmap_holder.setObjectName(u"live_pixmap_holder")
        self.live_pixmap_holder.setStyleSheet(u"padding: 2;\n"
"background-color: #000")
        self.live_pixmap_holder.setPixmap(QPixmap(u"../../Pictures/Screenshots/Screenshot 2024-02-21 144522.png"))
        self.live_pixmap_holder.setScaledContents(True)
        self.live_pixmap_holder.setAlignment(Qt.AlignCenter)
        self.live_pixmap_holder.setWordWrap(False)
        self.live_pixmap_holder.setMargin(0)

        self.verticalLayout_9.addWidget(self.live_pixmap_holder)


        self.gridLayout_6.addWidget(self.widget_5, 0, 0, 1, 1)

        self.splitter.addWidget(self.viewport_widget_live)

        self.horizontalLayout_5.addWidget(self.splitter)

        self.content_stack_widget.addWidget(self.live_page_widget)
        self.playback_page_widget = QWidget()
        self.playback_page_widget.setObjectName(u"playback_page_widget")
        self.horizontalLayout = QHBoxLayout(self.playback_page_widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_bar_widget_playback = QWidget(self.playback_page_widget)
        self.side_bar_widget_playback.setObjectName(u"side_bar_widget_playback")
        sizePolicy3.setHeightForWidth(self.side_bar_widget_playback.sizePolicy().hasHeightForWidth())
        self.side_bar_widget_playback.setSizePolicy(sizePolicy3)
        self.side_bar_widget_playback.setStyleSheet(u"background-color: #393939")
        self.verticalLayout_2 = QVBoxLayout(self.side_bar_widget_playback)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidebar_explorer_button_playback = QPushButton(self.side_bar_widget_playback)
        self.sidebar_explorer_button_playback.setObjectName(u"sidebar_explorer_button_playback")
        sizePolicy4.setHeightForWidth(self.sidebar_explorer_button_playback.sizePolicy().hasHeightForWidth())
        self.sidebar_explorer_button_playback.setSizePolicy(sizePolicy4)
        self.sidebar_explorer_button_playback.setMinimumSize(QSize(45, 45))
        self.sidebar_explorer_button_playback.setStyleSheet(u"background-color: transparent")
        self.sidebar_explorer_button_playback.setIcon(icon9)
        self.sidebar_explorer_button_playback.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.sidebar_explorer_button_playback)

        self.sidebar_detections_button_playback = QPushButton(self.side_bar_widget_playback)
        self.sidebar_detections_button_playback.setObjectName(u"sidebar_detections_button_playback")
        sizePolicy2.setHeightForWidth(self.sidebar_detections_button_playback.sizePolicy().hasHeightForWidth())
        self.sidebar_detections_button_playback.setSizePolicy(sizePolicy2)
        self.sidebar_detections_button_playback.setMinimumSize(QSize(45, 45))
        self.sidebar_detections_button_playback.setStyleSheet(u"background-color: transparent")
        self.sidebar_detections_button_playback.setIcon(icon10)
        self.sidebar_detections_button_playback.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.sidebar_detections_button_playback)

        self.sidebar_tuning_button_playback = QPushButton(self.side_bar_widget_playback)
        self.sidebar_tuning_button_playback.setObjectName(u"sidebar_tuning_button_playback")
        sizePolicy5.setHeightForWidth(self.sidebar_tuning_button_playback.sizePolicy().hasHeightForWidth())
        self.sidebar_tuning_button_playback.setSizePolicy(sizePolicy5)
        self.sidebar_tuning_button_playback.setMinimumSize(QSize(45, 45))
        self.sidebar_tuning_button_playback.setStyleSheet(u"background-color: transparent")
        self.sidebar_tuning_button_playback.setIcon(icon11)
        self.sidebar_tuning_button_playback.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.sidebar_tuning_button_playback)

        self.side_bar_widget_spacer_playback = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.side_bar_widget_spacer_playback)


        self.horizontalLayout.addWidget(self.side_bar_widget_playback)

        self.splitter_playback = QSplitter(self.playback_page_widget)
        self.splitter_playback.setObjectName(u"splitter_playback")
        self.splitter_playback.setFrameShape(QFrame.NoFrame)
        self.splitter_playback.setOrientation(Qt.Horizontal)
        self.splitter_playback.setOpaqueResize(True)
        self.splitter_playback.setHandleWidth(0)
        self.splitter_playback.setChildrenCollapsible(True)
        self.side_panel_stack_widget_playback = QStackedWidget(self.splitter_playback)
        self.side_panel_stack_widget_playback.setObjectName(u"side_panel_stack_widget_playback")
        sizePolicy1.setHeightForWidth(self.side_panel_stack_widget_playback.sizePolicy().hasHeightForWidth())
        self.side_panel_stack_widget_playback.setSizePolicy(sizePolicy1)
        self.side_panel_stack_widget_playback.setMinimumSize(QSize(200, 0))
        self.side_panel_stack_widget_playback.setStyleSheet(u"background-color: #313131")
        self.side_panel_detections_widget_playback = QWidget()
        self.side_panel_detections_widget_playback.setObjectName(u"side_panel_detections_widget_playback")
        self.verticalLayout_3 = QVBoxLayout(self.side_panel_detections_widget_playback)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.detections_side_panel_label_playback = QLabel(self.side_panel_detections_widget_playback)
        self.detections_side_panel_label_playback.setObjectName(u"detections_side_panel_label_playback")
        sizePolicy.setHeightForWidth(self.detections_side_panel_label_playback.sizePolicy().hasHeightForWidth())
        self.detections_side_panel_label_playback.setSizePolicy(sizePolicy)
        self.detections_side_panel_label_playback.setStyleSheet(u"color: #aaa; padding: 10 0 3 0")

        self.verticalLayout_3.addWidget(self.detections_side_panel_label_playback)

        self.detections_incoming_treewidget_playback = QTreeWidget(self.side_panel_detections_widget_playback)
        __qtreewidgetitem20 = QTreeWidgetItem()
        __qtreewidgetitem20.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem20.setFont(1, font2);
        __qtreewidgetitem20.setFont(0, font2);
        __qtreewidgetitem20.setIcon(0, icon12);
        self.detections_incoming_treewidget_playback.setHeaderItem(__qtreewidgetitem20)
        __qtreewidgetitem21 = QTreeWidgetItem(self.detections_incoming_treewidget_playback)
        __qtreewidgetitem21.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem22 = QTreeWidgetItem(self.detections_incoming_treewidget_playback)
        __qtreewidgetitem22.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem22.setFont(1, font3);
        __qtreewidgetitem23 = QTreeWidgetItem(self.detections_incoming_treewidget_playback)
        __qtreewidgetitem23.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem24 = QTreeWidgetItem(self.detections_incoming_treewidget_playback)
        __qtreewidgetitem24.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem25 = QTreeWidgetItem(self.detections_incoming_treewidget_playback)
        __qtreewidgetitem25.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem26 = QTreeWidgetItem(self.detections_incoming_treewidget_playback)
        __qtreewidgetitem26.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem27 = QTreeWidgetItem(self.detections_incoming_treewidget_playback)
        __qtreewidgetitem27.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem28 = QTreeWidgetItem(self.detections_incoming_treewidget_playback)
        __qtreewidgetitem28.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem29 = QTreeWidgetItem(self.detections_incoming_treewidget_playback)
        __qtreewidgetitem29.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        self.detections_incoming_treewidget_playback.setObjectName(u"detections_incoming_treewidget_playback")
        sizePolicy6.setHeightForWidth(self.detections_incoming_treewidget_playback.sizePolicy().hasHeightForWidth())
        self.detections_incoming_treewidget_playback.setSizePolicy(sizePolicy6)
        self.detections_incoming_treewidget_playback.setStyleSheet(u"QTreeWidget{color: #ddd; color: #aaa; border: 0; padding: 0 15}\n"
"QHeaderView::section{background-color: transparent; color: #ddd}\n"
"")
        self.detections_incoming_treewidget_playback.setIndentation(10)
        self.detections_incoming_treewidget_playback.setUniformRowHeights(True)
        self.detections_incoming_treewidget_playback.setItemsExpandable(False)
        self.detections_incoming_treewidget_playback.setAnimated(True)
        self.detections_incoming_treewidget_playback.header().setVisible(True)
        self.detections_incoming_treewidget_playback.header().setDefaultSectionSize(80)
        self.detections_incoming_treewidget_playback.header().setProperty("showSortIndicator", False)
        self.detections_incoming_treewidget_playback.header().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.detections_incoming_treewidget_playback)

        self.detections_outgoing_treewidget_playback = QTreeWidget(self.side_panel_detections_widget_playback)
        __qtreewidgetitem30 = QTreeWidgetItem()
        __qtreewidgetitem30.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem30.setFont(1, font2);
        __qtreewidgetitem30.setFont(0, font2);
        self.detections_outgoing_treewidget_playback.setHeaderItem(__qtreewidgetitem30)
        __qtreewidgetitem31 = QTreeWidgetItem(self.detections_outgoing_treewidget_playback)
        __qtreewidgetitem31.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem32 = QTreeWidgetItem(self.detections_outgoing_treewidget_playback)
        __qtreewidgetitem32.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem32.setFont(1, font3);
        __qtreewidgetitem33 = QTreeWidgetItem(self.detections_outgoing_treewidget_playback)
        __qtreewidgetitem33.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem34 = QTreeWidgetItem(self.detections_outgoing_treewidget_playback)
        __qtreewidgetitem34.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem35 = QTreeWidgetItem(self.detections_outgoing_treewidget_playback)
        __qtreewidgetitem35.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem36 = QTreeWidgetItem(self.detections_outgoing_treewidget_playback)
        __qtreewidgetitem36.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem37 = QTreeWidgetItem(self.detections_outgoing_treewidget_playback)
        __qtreewidgetitem37.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem38 = QTreeWidgetItem(self.detections_outgoing_treewidget_playback)
        __qtreewidgetitem38.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem39 = QTreeWidgetItem(self.detections_outgoing_treewidget_playback)
        __qtreewidgetitem39.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        self.detections_outgoing_treewidget_playback.setObjectName(u"detections_outgoing_treewidget_playback")
        sizePolicy6.setHeightForWidth(self.detections_outgoing_treewidget_playback.sizePolicy().hasHeightForWidth())
        self.detections_outgoing_treewidget_playback.setSizePolicy(sizePolicy6)
        self.detections_outgoing_treewidget_playback.setStyleSheet(u"QTreeWidget{color: #ddd; color: #aaa; border: 0; padding: 0 15}\n"
"QHeaderView::section{background-color: transparent; color: #ddd}")
        self.detections_outgoing_treewidget_playback.setIndentation(10)
        self.detections_outgoing_treewidget_playback.setUniformRowHeights(True)
        self.detections_outgoing_treewidget_playback.setItemsExpandable(False)
        self.detections_outgoing_treewidget_playback.setAnimated(True)
        self.detections_outgoing_treewidget_playback.header().setVisible(True)
        self.detections_outgoing_treewidget_playback.header().setDefaultSectionSize(80)
        self.detections_outgoing_treewidget_playback.header().setProperty("showSortIndicator", False)
        self.detections_outgoing_treewidget_playback.header().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.detections_outgoing_treewidget_playback)

        self.side_panel_detections_widget_spacer_playback = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.side_panel_detections_widget_spacer_playback)

        self.side_panel_stack_widget_playback.addWidget(self.side_panel_detections_widget_playback)
        self.side_panel_tuning_widget_playback = QWidget()
        self.side_panel_tuning_widget_playback.setObjectName(u"side_panel_tuning_widget_playback")
        self.side_panel_tuning_widget_playback.setStyleSheet(u"QLabel {color: #ddd; padding: 5 0 0 15}\n"
"QCheckBox{padding: 5 15 0 0}\n"
"QSlider{padding: 5 15 0 0}")
        self.gridLayout = QGridLayout(self.side_panel_tuning_widget_playback)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tuning_side_panel_label = QLabel(self.side_panel_tuning_widget_playback)
        self.tuning_side_panel_label.setObjectName(u"tuning_side_panel_label")
        sizePolicy.setHeightForWidth(self.tuning_side_panel_label.sizePolicy().hasHeightForWidth())
        self.tuning_side_panel_label.setSizePolicy(sizePolicy)
        self.tuning_side_panel_label.setStyleSheet(u"color: #aaa; padding: 10 0 3 0")

        self.gridLayout.addWidget(self.tuning_side_panel_label, 0, 0, 1, 2)

        self.visible_layers_label_playback = QLabel(self.side_panel_tuning_widget_playback)
        self.visible_layers_label_playback.setObjectName(u"visible_layers_label_playback")
        self.visible_layers_label_playback.setFont(font2)
        self.visible_layers_label_playback.setStyleSheet(u"color: #ddd; padding: 5 0 0 15")

        self.gridLayout.addWidget(self.visible_layers_label_playback, 1, 0, 1, 2)

        self.label_label_playback = QLabel(self.side_panel_tuning_widget_playback)
        self.label_label_playback.setObjectName(u"label_label_playback")
        self.label_label_playback.setStyleSheet(u"color: #ddd; padding: 5 0 0 25")

        self.gridLayout.addWidget(self.label_label_playback, 2, 0, 1, 1)

        self.label_checkbox_playback = QCheckBox(self.side_panel_tuning_widget_playback)
        self.label_checkbox_playback.setObjectName(u"label_checkbox_playback")
        sizePolicy2.setHeightForWidth(self.label_checkbox_playback.sizePolicy().hasHeightForWidth())
        self.label_checkbox_playback.setSizePolicy(sizePolicy2)
        self.label_checkbox_playback.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.label_checkbox_playback, 2, 1, 1, 1)

        self.tracking_label_playback = QLabel(self.side_panel_tuning_widget_playback)
        self.tracking_label_playback.setObjectName(u"tracking_label_playback")
        self.tracking_label_playback.setStyleSheet(u"color: #ddd; padding: 5 0 0 25")

        self.gridLayout.addWidget(self.tracking_label_playback, 3, 0, 1, 1)

        self.tracking_checkbox_playback = QCheckBox(self.side_panel_tuning_widget_playback)
        self.tracking_checkbox_playback.setObjectName(u"tracking_checkbox_playback")
        sizePolicy2.setHeightForWidth(self.tracking_checkbox_playback.sizePolicy().hasHeightForWidth())
        self.tracking_checkbox_playback.setSizePolicy(sizePolicy2)
        self.tracking_checkbox_playback.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.tracking_checkbox_playback, 3, 1, 1, 1)

        self.bounding_box_label_playback = QLabel(self.side_panel_tuning_widget_playback)
        self.bounding_box_label_playback.setObjectName(u"bounding_box_label_playback")
        self.bounding_box_label_playback.setStyleSheet(u"color: #ddd; padding: 5 0 0 25")

        self.gridLayout.addWidget(self.bounding_box_label_playback, 4, 0, 1, 1)

        self.bounding_box_checkbox_playback = QCheckBox(self.side_panel_tuning_widget_playback)
        self.bounding_box_checkbox_playback.setObjectName(u"bounding_box_checkbox_playback")
        sizePolicy2.setHeightForWidth(self.bounding_box_checkbox_playback.sizePolicy().hasHeightForWidth())
        self.bounding_box_checkbox_playback.setSizePolicy(sizePolicy2)
        self.bounding_box_checkbox_playback.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.bounding_box_checkbox_playback, 4, 1, 1, 1)

        self.threshold_label_playback = QLabel(self.side_panel_tuning_widget_playback)
        self.threshold_label_playback.setObjectName(u"threshold_label_playback")
        self.threshold_label_playback.setFont(font2)
        self.threshold_label_playback.setStyleSheet(u"color: #ddd; padding: 5 0 0 15")

        self.gridLayout.addWidget(self.threshold_label_playback, 5, 0, 1, 2)

        self.confidence_label_playback = QLabel(self.side_panel_tuning_widget_playback)
        self.confidence_label_playback.setObjectName(u"confidence_label_playback")
        self.confidence_label_playback.setStyleSheet(u"color: #ddd; padding: 5 0 0 25")

        self.gridLayout.addWidget(self.confidence_label_playback, 6, 0, 1, 1)

        self.confidence_value_label_playback = QLabel(self.side_panel_tuning_widget_playback)
        self.confidence_value_label_playback.setObjectName(u"confidence_value_label_playback")
        self.confidence_value_label_playback.setStyleSheet(u"color: #ddd; padding: 5 15 0 0")
        self.confidence_value_label_playback.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.confidence_value_label_playback, 6, 1, 1, 1)

        self.confidence_slider_playback = QSlider(self.side_panel_tuning_widget_playback)
        self.confidence_slider_playback.setObjectName(u"confidence_slider_playback")
        self.confidence_slider_playback.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height: 4px;\n"
"    margin: 0 0 0 28px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ddd, stop:1 #f6f6f6);\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #A0C334, stop:1 #A0C334);\n"
"    width: 14px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #A0C334, stop:1 #A0C334);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #A0C334, stop:1 #E5D429);\n"
"}")
        self.confidence_slider_playback.setMaximum(100)
        self.confidence_slider_playback.setValue(55)
        self.confidence_slider_playback.setOrientation(Qt.Horizontal)
        self.confidence_slider_playback.setTickPosition(QSlider.NoTicks)

        self.gridLayout.addWidget(self.confidence_slider_playback, 7, 0, 1, 2)

        self.overlap_label_playback = QLabel(self.side_panel_tuning_widget_playback)
        self.overlap_label_playback.setObjectName(u"overlap_label_playback")
        self.overlap_label_playback.setStyleSheet(u"color: #ddd; padding: 5 0 0 25")

        self.gridLayout.addWidget(self.overlap_label_playback, 8, 0, 1, 1)

        self.overlap_value_label_playback = QLabel(self.side_panel_tuning_widget_playback)
        self.overlap_value_label_playback.setObjectName(u"overlap_value_label_playback")
        self.overlap_value_label_playback.setStyleSheet(u"color: #ddd; padding: 5 15 0 0")
        self.overlap_value_label_playback.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.overlap_value_label_playback, 8, 1, 1, 1)

        self.overlap_slider_playback = QSlider(self.side_panel_tuning_widget_playback)
        self.overlap_slider_playback.setObjectName(u"overlap_slider_playback")
        self.overlap_slider_playback.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height: 4px;\n"
"    margin: 0 0 0 28px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ddd, stop:1 #f6f6f6);\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #A0C334, stop:1 #A0C334);\n"
"    width: 14px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #A0C334, stop:1 #A0C334);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #A0C334, stop:1 #E5D429);\n"
"}")
        self.overlap_slider_playback.setMaximum(100)
        self.overlap_slider_playback.setValue(55)
        self.overlap_slider_playback.setOrientation(Qt.Horizontal)
        self.overlap_slider_playback.setTickPosition(QSlider.NoTicks)

        self.gridLayout.addWidget(self.overlap_slider_playback, 9, 0, 1, 2)

        self.side_panel_tuning_widget_spacer_playback = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.side_panel_tuning_widget_spacer_playback, 10, 0, 1, 2)

        self.side_panel_stack_widget_playback.addWidget(self.side_panel_tuning_widget_playback)
        self.side_panel_explorer_widget_playback = QWidget()
        self.side_panel_explorer_widget_playback.setObjectName(u"side_panel_explorer_widget_playback")
        self.verticalLayout_4 = QVBoxLayout(self.side_panel_explorer_widget_playback)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.explorer_side_panel_label_playback = QLabel(self.side_panel_explorer_widget_playback)
        self.explorer_side_panel_label_playback.setObjectName(u"explorer_side_panel_label_playback")
        sizePolicy.setHeightForWidth(self.explorer_side_panel_label_playback.sizePolicy().hasHeightForWidth())
        self.explorer_side_panel_label_playback.setSizePolicy(sizePolicy)
        self.explorer_side_panel_label_playback.setStyleSheet(u"color: #aaa; padding: 10 0 3 0")

        self.verticalLayout_4.addWidget(self.explorer_side_panel_label_playback)

        self.filesystem_treeview_playback = QTreeView(self.side_panel_explorer_widget_playback)
        self.filesystem_treeview_playback.setObjectName(u"filesystem_treeview_playback")
        self.filesystem_treeview_playback.setMinimumSize(QSize(200, 0))
        self.filesystem_treeview_playback.setFrameShape(QFrame.NoFrame)
        self.filesystem_treeview_playback.setAutoScroll(False)
        self.filesystem_treeview_playback.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.filesystem_treeview_playback.setSelectionMode(QAbstractItemView.NoSelection)
        self.filesystem_treeview_playback.setTextElideMode(Qt.ElideNone)
        self.filesystem_treeview_playback.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_4.addWidget(self.filesystem_treeview_playback)

        self.side_panel_stack_widget_playback.addWidget(self.side_panel_explorer_widget_playback)
        self.splitter_playback.addWidget(self.side_panel_stack_widget_playback)
        self.viewport_widget_playback = QWidget(self.splitter_playback)
        self.viewport_widget_playback.setObjectName(u"viewport_widget_playback")
        self.viewport_widget_playback.setMinimumSize(QSize(500, 0))
        self.viewport_widget_playback.setStyleSheet(u"background-color: #464646")
        self.gridLayout_2 = QGridLayout(self.viewport_widget_playback)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.playback_widget = QWidget(self.viewport_widget_playback)
        self.playback_widget.setObjectName(u"playback_widget")
        self.verticalLayout_6 = QVBoxLayout(self.playback_widget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.source_name_label_playback = QLabel(self.playback_widget)
        self.source_name_label_playback.setObjectName(u"source_name_label_playback")
        sizePolicy.setHeightForWidth(self.source_name_label_playback.sizePolicy().hasHeightForWidth())
        self.source_name_label_playback.setSizePolicy(sizePolicy)
        self.source_name_label_playback.setStyleSheet(u"background-color: #000;\n"
"color: #aaa;\n"
"padding: 2 15 2 15")

        self.verticalLayout_6.addWidget(self.source_name_label_playback)

        self.playback_pixmap_holder = QLabel(self.playback_widget)
        self.playback_pixmap_holder.setObjectName(u"playback_pixmap_holder")
        self.playback_pixmap_holder.setStyleSheet(u"padding: 2;\n"
"background-color: #000")
        self.playback_pixmap_holder.setPixmap(QPixmap(u"../../Pictures/Screenshots/Screenshot 2024-02-21 144522.png"))
        self.playback_pixmap_holder.setScaledContents(True)
        self.playback_pixmap_holder.setAlignment(Qt.AlignCenter)
        self.playback_pixmap_holder.setWordWrap(False)
        self.playback_pixmap_holder.setMargin(0)

        self.verticalLayout_6.addWidget(self.playback_pixmap_holder)


        self.gridLayout_2.addWidget(self.playback_widget, 0, 0, 1, 1)

        self.splitter_playback.addWidget(self.viewport_widget_playback)

        self.horizontalLayout.addWidget(self.splitter_playback)

        self.content_stack_widget.addWidget(self.playback_page_widget)
        self.model_page_widget = QWidget()
        self.model_page_widget.setObjectName(u"model_page_widget")
        self.horizontalLayout_6 = QHBoxLayout(self.model_page_widget)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.model_page_widget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_7 = QVBoxLayout(self.widget_3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 86, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setPointSize(20)
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color: #ccc")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: #aaa")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)

        self.verticalSpacer_6 = QSpacerItem(20, 175, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_6)

        self.verticalLayout_7.setStretch(0, 2)
        self.verticalLayout_7.setStretch(3, 4)

        self.horizontalLayout_6.addWidget(self.widget_3)

        self.content_stack_widget.addWidget(self.model_page_widget)
        self.charts_page_widget = QWidget()
        self.charts_page_widget.setObjectName(u"charts_page_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.charts_page_widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.charts_page_widget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color: #ccc")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: #aaa")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.verticalLayout_5.setStretch(0, 2)
        self.verticalLayout_5.setStretch(3, 4)

        self.horizontalLayout_4.addWidget(self.widget)

        self.content_stack_widget.addWidget(self.charts_page_widget)
        self.settings_page_widget = QWidget()
        self.settings_page_widget.setObjectName(u"settings_page_widget")
        self.horizontalLayout_7 = QHBoxLayout(self.settings_page_widget)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.settings_page_widget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_8 = QVBoxLayout(self.widget_4)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_9 = QSpacerItem(20, 144, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_9)

        self.label_7 = QLabel(self.widget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"color: #ccc")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: #aaa")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_8)

        self.verticalSpacer_8 = QSpacerItem(20, 292, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_8)

        self.verticalLayout_8.setStretch(0, 2)
        self.verticalLayout_8.setStretch(3, 4)

        self.horizontalLayout_7.addWidget(self.widget_4)

        self.content_stack_widget.addWidget(self.settings_page_widget)

        self.verticalLayout.addWidget(self.content_stack_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.content_stack_widget.setCurrentIndex(0)
        self.side_panel_stack_widget_live.setCurrentIndex(1)
        self.side_panel_stack_widget_playback.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.window_title_label.setText(QCoreApplication.translate("MainWindow", u"BATSTATE-U: Vision Drive", None))
        self.minimize_window.setText("")
        self.dock_window.setText("")
        self.terminate_window.setText("")
        self.header_logo.setText("")
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.charts_button.setText(QCoreApplication.translate("MainWindow", u"CHARTS", None))
        self.model_button.setText(QCoreApplication.translate("MainWindow", u"MODEL", None))
        self.playback_button.setText(QCoreApplication.translate("MainWindow", u"PLAYBACK", None))
        self.live_button.setText(QCoreApplication.translate("MainWindow", u"LIVE", None))
#if QT_CONFIG(tooltip)
        self.sidebar_explorer_button_live.setToolTip(QCoreApplication.translate("MainWindow", u"Explorer", None))
#endif // QT_CONFIG(tooltip)
        self.sidebar_explorer_button_live.setText("")
#if QT_CONFIG(tooltip)
        self.sidebar_detections_button_live.setToolTip(QCoreApplication.translate("MainWindow", u"Detections", None))
#endif // QT_CONFIG(tooltip)
        self.sidebar_detections_button_live.setText("")
#if QT_CONFIG(tooltip)
        self.sidebar_tuning_button_live.setToolTip(QCoreApplication.translate("MainWindow", u"Tuning", None))
#endif // QT_CONFIG(tooltip)
        self.sidebar_tuning_button_live.setText("")
        self.detections_side_panel_label_live.setText(QCoreApplication.translate("MainWindow", u"DETECTIONS", None))
        ___qtreewidgetitem = self.detections_incoming_treewidget_live.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Count", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Incoming", None));

        __sortingEnabled = self.detections_incoming_treewidget_live.isSortingEnabled()
        self.detections_incoming_treewidget_live.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.detections_incoming_treewidget_live.topLevelItem(0)
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Bicycle", None));
        ___qtreewidgetitem2 = self.detections_incoming_treewidget_live.topLevelItem(1)
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Bus", None));
        ___qtreewidgetitem3 = self.detections_incoming_treewidget_live.topLevelItem(2)
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"Car", None));
        ___qtreewidgetitem4 = self.detections_incoming_treewidget_live.topLevelItem(3)
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"E-Bike", None));
        ___qtreewidgetitem5 = self.detections_incoming_treewidget_live.topLevelItem(4)
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"Jeepney", None));
        ___qtreewidgetitem6 = self.detections_incoming_treewidget_live.topLevelItem(5)
        ___qtreewidgetitem6.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"Motorcycle", None));
        ___qtreewidgetitem7 = self.detections_incoming_treewidget_live.topLevelItem(6)
        ___qtreewidgetitem7.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"Tricycle", None));
        ___qtreewidgetitem8 = self.detections_incoming_treewidget_live.topLevelItem(7)
        ___qtreewidgetitem8.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"Truck", None));
        ___qtreewidgetitem9 = self.detections_incoming_treewidget_live.topLevelItem(8)
        ___qtreewidgetitem9.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"Van", None));
        self.detections_incoming_treewidget_live.setSortingEnabled(__sortingEnabled)

        ___qtreewidgetitem10 = self.detections_outgoing_treewidget_live.headerItem()
        ___qtreewidgetitem10.setText(1, QCoreApplication.translate("MainWindow", u"Count", None));
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"Outgoing", None));

        __sortingEnabled1 = self.detections_outgoing_treewidget_live.isSortingEnabled()
        self.detections_outgoing_treewidget_live.setSortingEnabled(False)
        ___qtreewidgetitem11 = self.detections_outgoing_treewidget_live.topLevelItem(0)
        ___qtreewidgetitem11.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"Bicycle", None));
        ___qtreewidgetitem12 = self.detections_outgoing_treewidget_live.topLevelItem(1)
        ___qtreewidgetitem12.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"Bus", None));
        ___qtreewidgetitem13 = self.detections_outgoing_treewidget_live.topLevelItem(2)
        ___qtreewidgetitem13.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"Car", None));
        ___qtreewidgetitem14 = self.detections_outgoing_treewidget_live.topLevelItem(3)
        ___qtreewidgetitem14.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"E-Bike", None));
        ___qtreewidgetitem15 = self.detections_outgoing_treewidget_live.topLevelItem(4)
        ___qtreewidgetitem15.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"Jeepney", None));
        ___qtreewidgetitem16 = self.detections_outgoing_treewidget_live.topLevelItem(5)
        ___qtreewidgetitem16.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"Motorcycle", None));
        ___qtreewidgetitem17 = self.detections_outgoing_treewidget_live.topLevelItem(6)
        ___qtreewidgetitem17.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"Tricycle", None));
        ___qtreewidgetitem18 = self.detections_outgoing_treewidget_live.topLevelItem(7)
        ___qtreewidgetitem18.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MainWindow", u"Truck", None));
        ___qtreewidgetitem19 = self.detections_outgoing_treewidget_live.topLevelItem(8)
        ___qtreewidgetitem19.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("MainWindow", u"Van", None));
        self.detections_outgoing_treewidget_live.setSortingEnabled(__sortingEnabled1)

        self.threshold_label_live.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.confidence_label_live.setText(QCoreApplication.translate("MainWindow", u"Confidence", None))
        self.label_checkbox_live.setText("")
        self.overlap_label_live.setText(QCoreApplication.translate("MainWindow", u"Overlap", None))
        self.confidence_value_label_live.setText(QCoreApplication.translate("MainWindow", u"0.54", None))
        self.bounding_box_checkbox_live.setText("")
        self.tracking_checkbox_live.setText("")
        self.overlap_value_label_live.setText(QCoreApplication.translate("MainWindow", u"0.54", None))
        self.label_label_live.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.bounding_box_label_live.setText(QCoreApplication.translate("MainWindow", u"Bounding Box", None))
        self.tracking_label_live.setText(QCoreApplication.translate("MainWindow", u"Tracking", None))
        self.visible_layers_label_live.setText(QCoreApplication.translate("MainWindow", u"Visible Layes", None))
        self.tuning_side_panel_live.setText(QCoreApplication.translate("MainWindow", u"TUNING", None))
        self.explorer_side_panel_label_live.setText(QCoreApplication.translate("MainWindow", u"EXPLORER", None))
        self.source_name_label_live.setText(QCoreApplication.translate("MainWindow", u"Camera 1", None))
        self.live_pixmap_holder.setText("")
#if QT_CONFIG(tooltip)
        self.sidebar_explorer_button_playback.setToolTip(QCoreApplication.translate("MainWindow", u"Explorer", None))
#endif // QT_CONFIG(tooltip)
        self.sidebar_explorer_button_playback.setText("")
#if QT_CONFIG(tooltip)
        self.sidebar_detections_button_playback.setToolTip(QCoreApplication.translate("MainWindow", u"Detections", None))
#endif // QT_CONFIG(tooltip)
        self.sidebar_detections_button_playback.setText("")
#if QT_CONFIG(tooltip)
        self.sidebar_tuning_button_playback.setToolTip(QCoreApplication.translate("MainWindow", u"Tuning", None))
#endif // QT_CONFIG(tooltip)
        self.sidebar_tuning_button_playback.setText("")
        self.detections_side_panel_label_playback.setText(QCoreApplication.translate("MainWindow", u"DETECTIONS", None))
        ___qtreewidgetitem20 = self.detections_incoming_treewidget_playback.headerItem()
        ___qtreewidgetitem20.setText(1, QCoreApplication.translate("MainWindow", u"Count", None));
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("MainWindow", u"Incoming", None));

        __sortingEnabled2 = self.detections_incoming_treewidget_playback.isSortingEnabled()
        self.detections_incoming_treewidget_playback.setSortingEnabled(False)
        ___qtreewidgetitem21 = self.detections_incoming_treewidget_playback.topLevelItem(0)
        ___qtreewidgetitem21.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("MainWindow", u"Bicycle", None));
        ___qtreewidgetitem22 = self.detections_incoming_treewidget_playback.topLevelItem(1)
        ___qtreewidgetitem22.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("MainWindow", u"Bus", None));
        ___qtreewidgetitem23 = self.detections_incoming_treewidget_playback.topLevelItem(2)
        ___qtreewidgetitem23.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("MainWindow", u"Car", None));
        ___qtreewidgetitem24 = self.detections_incoming_treewidget_playback.topLevelItem(3)
        ___qtreewidgetitem24.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("MainWindow", u"E-Bike", None));
        ___qtreewidgetitem25 = self.detections_incoming_treewidget_playback.topLevelItem(4)
        ___qtreewidgetitem25.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("MainWindow", u"Jeepney", None));
        ___qtreewidgetitem26 = self.detections_incoming_treewidget_playback.topLevelItem(5)
        ___qtreewidgetitem26.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("MainWindow", u"Motorcycle", None));
        ___qtreewidgetitem27 = self.detections_incoming_treewidget_playback.topLevelItem(6)
        ___qtreewidgetitem27.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem27.setText(0, QCoreApplication.translate("MainWindow", u"Tricycle", None));
        ___qtreewidgetitem28 = self.detections_incoming_treewidget_playback.topLevelItem(7)
        ___qtreewidgetitem28.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem28.setText(0, QCoreApplication.translate("MainWindow", u"Truck", None));
        ___qtreewidgetitem29 = self.detections_incoming_treewidget_playback.topLevelItem(8)
        ___qtreewidgetitem29.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem29.setText(0, QCoreApplication.translate("MainWindow", u"Van", None));
        self.detections_incoming_treewidget_playback.setSortingEnabled(__sortingEnabled2)

        ___qtreewidgetitem30 = self.detections_outgoing_treewidget_playback.headerItem()
        ___qtreewidgetitem30.setText(1, QCoreApplication.translate("MainWindow", u"Count", None));
        ___qtreewidgetitem30.setText(0, QCoreApplication.translate("MainWindow", u"Outgoing", None));

        __sortingEnabled3 = self.detections_outgoing_treewidget_playback.isSortingEnabled()
        self.detections_outgoing_treewidget_playback.setSortingEnabled(False)
        ___qtreewidgetitem31 = self.detections_outgoing_treewidget_playback.topLevelItem(0)
        ___qtreewidgetitem31.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem31.setText(0, QCoreApplication.translate("MainWindow", u"Bicycle", None));
        ___qtreewidgetitem32 = self.detections_outgoing_treewidget_playback.topLevelItem(1)
        ___qtreewidgetitem32.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem32.setText(0, QCoreApplication.translate("MainWindow", u"Bus", None));
        ___qtreewidgetitem33 = self.detections_outgoing_treewidget_playback.topLevelItem(2)
        ___qtreewidgetitem33.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem33.setText(0, QCoreApplication.translate("MainWindow", u"Car", None));
        ___qtreewidgetitem34 = self.detections_outgoing_treewidget_playback.topLevelItem(3)
        ___qtreewidgetitem34.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem34.setText(0, QCoreApplication.translate("MainWindow", u"E-Bike", None));
        ___qtreewidgetitem35 = self.detections_outgoing_treewidget_playback.topLevelItem(4)
        ___qtreewidgetitem35.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem35.setText(0, QCoreApplication.translate("MainWindow", u"Jeepney", None));
        ___qtreewidgetitem36 = self.detections_outgoing_treewidget_playback.topLevelItem(5)
        ___qtreewidgetitem36.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem36.setText(0, QCoreApplication.translate("MainWindow", u"Motorcycle", None));
        ___qtreewidgetitem37 = self.detections_outgoing_treewidget_playback.topLevelItem(6)
        ___qtreewidgetitem37.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem37.setText(0, QCoreApplication.translate("MainWindow", u"Tricycle", None));
        ___qtreewidgetitem38 = self.detections_outgoing_treewidget_playback.topLevelItem(7)
        ___qtreewidgetitem38.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem38.setText(0, QCoreApplication.translate("MainWindow", u"Truck", None));
        ___qtreewidgetitem39 = self.detections_outgoing_treewidget_playback.topLevelItem(8)
        ___qtreewidgetitem39.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem39.setText(0, QCoreApplication.translate("MainWindow", u"Van", None));
        self.detections_outgoing_treewidget_playback.setSortingEnabled(__sortingEnabled3)

        self.tuning_side_panel_label.setText(QCoreApplication.translate("MainWindow", u"TUNING", None))
        self.visible_layers_label_playback.setText(QCoreApplication.translate("MainWindow", u"Visible Layes", None))
        self.label_label_playback.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.label_checkbox_playback.setText("")
        self.tracking_label_playback.setText(QCoreApplication.translate("MainWindow", u"Tracking", None))
        self.tracking_checkbox_playback.setText("")
        self.bounding_box_label_playback.setText(QCoreApplication.translate("MainWindow", u"Bounding Box", None))
        self.bounding_box_checkbox_playback.setText("")
        self.threshold_label_playback.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.confidence_label_playback.setText(QCoreApplication.translate("MainWindow", u"Confidence", None))
        self.confidence_value_label_playback.setText(QCoreApplication.translate("MainWindow", u"0.54", None))
        self.overlap_label_playback.setText(QCoreApplication.translate("MainWindow", u"Overlap", None))
        self.overlap_value_label_playback.setText(QCoreApplication.translate("MainWindow", u"0.54", None))
        self.explorer_side_panel_label_playback.setText(QCoreApplication.translate("MainWindow", u"EXPLORER", None))
        self.source_name_label_playback.setText(QCoreApplication.translate("MainWindow", u"Camera 1", None))
        self.playback_pixmap_holder.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"MODEL PAGE", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"under development", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CHARTS PAGE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"under development", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"SETTINGS PAGE", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"under development", None))
    # retranslateUi

