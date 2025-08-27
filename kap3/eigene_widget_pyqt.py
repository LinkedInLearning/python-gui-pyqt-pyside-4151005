import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QVBoxLayout, QWidget
import random

class ColorButton(QPushButton):
    def __init__(self, text="Klick mich"):
        super().__init__(text)
        self.clicked.connect(self.change_color)

    def change_color(self):
        # Zufällige Farbe generieren
        r = random.randint(100, 255)
        g = random.randint(100, 255)
        b = random.randint(100, 255)
        color = f"rgb({r},{g},{b})"

        # Hintergrundfarbe via Stylesheet setzen
        self.setStyleSheet(f"background-color: {color};")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Individuelles Widget-Beispiel")
        self.resize(400, 50)

        container = QWidget()
        layout = QVBoxLayout()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Unser individuelles Widget hinzufügen
        self.color_button = ColorButton()
        layout.addWidget(self.color_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
