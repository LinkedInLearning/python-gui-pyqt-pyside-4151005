from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
import sys

class VBoxExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VBoxLayout")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("VBoxLayout Label"))
        layout.addWidget(QPushButton("VBoxLayout Button"))

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VBoxExample()
    window.show()
    sys.exit(app.exec())
