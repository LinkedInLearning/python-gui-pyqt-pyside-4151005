from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel
import sys

class GridExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GridLayout")

        layout = QGridLayout()
        layout.addWidget(QLabel("GridLabel"), 0, 0)
        layout.addWidget(QPushButton("GridButton"), 0, 1)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GridExample()
    window.show()
    sys.exit(app.exec())
