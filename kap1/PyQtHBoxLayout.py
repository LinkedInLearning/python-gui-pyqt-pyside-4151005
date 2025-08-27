from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel
import sys

class HBoxExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HBoxLayout")

        layout = QHBoxLayout()
        layout.addWidget(QLabel("HBoxLayout Label"))
        layout.addWidget(QPushButton("HBoxLayout Button"))

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HBoxExample()
    window.show()
    sys.exit(app.exec())
