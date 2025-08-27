import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

class MeinFenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ein PyQt6-Fenster")
        self.setGeometry(100, 100, 600, 300)  # x, y, Breite, Höhe

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenster = MeinFenster()
    fenster.show()
    sys.exit(app.exec())
