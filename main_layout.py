# main layout

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, QFrame, QTreeView, QFileSystemModel, QSizePolicy
from PySide6.QtCore import Qt, QPoint

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App with Sidebar")
        self.setGeometry(100, 100, 800, 600)

        # Set window flags to remove default window decorations
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint)

        main_widget = QWidget()

        # Create the main layout for the window
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero
        main_layout.setSpacing(0)
        main_widget.setLayout(main_layout)

        # Create the central widget area
        central_widget = QWidget()

        # Add widgets to the central widget area
        central_layout = QHBoxLayout()
        central_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero
        central_layout.setSpacing(0)
        central_widget.setLayout(central_layout)

        # Create a custom header/navigation bar
        self.header = QFrame()
        self.header.setStyleSheet("background-color: #007ACC;")  # Set header background color
        self.header.setFixedHeight(50)  # Set header height
        header_layout = QHBoxLayout()
        self.header.setLayout(header_layout)
        header_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero

        # Add title label to the header
        title_label = QLabel("App Title")
        title_label.setStyleSheet("color: white; font-size: 20px; padding: 10px;")
        header_layout.addWidget(title_label)

        # Add custom minimize button
        minimize_button = QPushButton("-")
        minimize_button.clicked.connect(self.showMinimized)
        minimize_button.setFixedWidth(30)
        header_layout.addWidget(minimize_button)

        # Add custom maximize button
        maximize_button = QPushButton("M")
        maximize_button.clicked.connect(self.toggle_maximize)
        maximize_button.setFixedWidth(30)
        header_layout.addWidget(maximize_button)

        # Add custom close button
        close_button = QPushButton("X")
        close_button.clicked.connect(self.close)
        close_button.setFixedWidth(30)
        header_layout.addWidget(close_button)

        # Add the header/navigation bar to the central layout
        main_layout.addWidget(self.header)
        main_layout.addWidget(central_widget)

        # Create the sidebar
        self.sidebar = QFrame()
        self.sidebar.setStyleSheet("background-color: #2D2D2D;")  # Set sidebar background color
        self.sidebar.setFixedWidth(150)  # Set sidebar width
        self.sidebar_layout = QVBoxLayout()
        self.sidebar.setLayout(self.sidebar_layout)

        # Add sidebar buttons
        self.add_sidebar_button("Explorer", self.show_explorer)
        self.add_sidebar_button("Detections", self.show_detections)
        self.add_sidebar_button("Layers", self.show_layers)

        # Add the sidebar to the central layout
        central_layout.addWidget(self.sidebar)
        
         # Create the sidebar content widget
        self.sidebar_content = QWidget()
        self.sidebar_content.setStyleSheet("background-color: #3A3A3A;")
        self.sidebar_content_layout = QVBoxLayout()
        self.sidebar_content.setLayout(self.sidebar_content_layout)
        self.sidebar_content.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Add the sidebar content widget to the main layout
        central_layout.addWidget(self.sidebar_content)

        # Set the central widget to the QMainWindow
        self.setCentralWidget(main_widget)

        # Initialize variables for handling window dragging
        self.draggable = False
        self.offset = QPoint()

    def add_sidebar_button(self, text, slot):
        button = QPushButton(text)
        button.clicked.connect(slot)
        self.sidebar_layout.addWidget(button)
        button.setStyleSheet("""
            QPushButton {
                padding: 10px;
                text-align: left;
                border: none;
                background-color: transparent;
                color: white;
            }
            QPushButton:hover {
                background-color: #505050;
            }
        """)

    def show_explorer(self):
        # Clear previous content
        self.clear_sidebar_content()
        # Add tree view
        model = QFileSystemModel()
        model.setRootPath("")
        tree_view = QTreeView()
        tree_view.setModel(model)
        self.sidebar_content_layout.addWidget(tree_view)

    def show_detections(self):
        # Clear previous content
        self.clear_sidebar_content()
        # Add custom content for Detections
        self.sidebar_content_layout.addWidget(QLabel("Detections Content"))

    def show_layers(self):
        # Clear previous content
        self.clear_sidebar_content()
        # Add custom content for Layers
        self.sidebar_content_layout.addWidget(QLabel("Layers Content"))

    def clear_sidebar_content(self):
        # Clear sidebar content layout
        while self.sidebar_content_layout.count() > 0:
            item = self.sidebar_content_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def mousePressEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and event.position().y() <= self.header.height():
            self.drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and hasattr(self, 'drag_pos'):
            self.move(event.globalPosition().toPoint() - self.drag_pos)
            event.accept()
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if hasattr(self, 'drag_pos'):
            delattr(self, 'drag_pos')
            event.accept()
        else:
            super().mouseReleaseEvent(event)

    def toggle_maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())