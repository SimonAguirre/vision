from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout

class SideBar(QWidget):
        def __init__(self, parent) -> None:
                super().__init__(parent)
                
                # Set Layout for the header
                main_layout = QHBoxLayout()
                self.setLayout(main_layout)
                main_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero

