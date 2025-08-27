import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Taschenrechner")
        self.setFixedSize(300, 400)
        self.create_ui()

    def create_ui(self):
        pass

    def append_to_display(self, text):
        pass

    def clear_display(self):
        pass

    def calculate_result(self):
        pass
        # eval für die Berechnung

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
