from PyQt6.QtWidgets import QApplication, QWidget, QBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt
import sys

class BoxExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BoxLayout")

        layout = QBoxLayout(QBoxLayout.Direction.LeftToRight)
        layout.addWidget(QLabel("BoxLayout Label"))
        layout.addWidget(QPushButton("BoxLayout Button"))

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BoxExample()
    window.show()
    sys.exit(app.exec())
