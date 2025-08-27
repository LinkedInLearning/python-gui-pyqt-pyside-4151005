from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
import sys

class AbsoluteExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Absolutes Layout")
        self.setGeometry(100, 100, 300, 200)

        label = QLabel("Absolutes Label", self)
        label.move(50, 40)

        button = QPushButton("Absoluter Button", self)
        button.move(50, 80)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AbsoluteExample()
    window.show()
    sys.exit(app.exec())
