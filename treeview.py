import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTreeView, QFileSystemModel, QWidget


class FileExplorer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.tree_view = QTreeView()
        layout.addWidget(self.tree_view)
        self.setLayout(layout)
        self.init_file_explorer()

    def init_file_explorer(self):
        model = QFileSystemModel()
        model.setRootPath('')
        self.tree_view.setModel(model)
        self.tree_view.setRootIndex(model.index(''))  # Set root index to the current directory


class Sidebar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sidebar with File Explorer")
        self.setGeometry(100, 100, 400, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout= QVBoxLayout(self.central_widget)

        self.file_explorer = FileExplorer(self)
        self.layout.addWidget(self.file_explorer)


def main():
    app = QApplication(sys.argv)
    sidebar = Sidebar()
    sidebar.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
