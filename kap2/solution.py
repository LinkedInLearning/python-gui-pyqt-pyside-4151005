import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Taschenrechner")
        self.setFixedSize(300, 400)
        self.create_ui()

    def create_ui(self):
        # Layouts
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setFixedHeight(50)
        self.display.setStyleSheet("font-size: 24px;")
        main_layout.addWidget(self.display)

        # Button Grid
        grid = QGridLayout()
        main_layout.addLayout(grid)

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '%', '+'),
            ('C', '=')
        ]

        for row_idx, row in enumerate(buttons):
            for col_idx, button_text in enumerate(row):
                button = QPushButton(button_text)
                button.setFixedSize(60, 60)
                button.setStyleSheet("font-size: 18px;")
                grid.addWidget(button, row_idx, col_idx)
                if button_text not in ('=', 'C'):
                    # Zahl und Operatoren Buttons
                    button.clicked.connect(lambda checked, txt=button_text: self.append_to_display(txt))
                elif button_text == 'C':
                    button.clicked.connect(self.clear_display)
                elif button_text == '=':
                    button.clicked.connect(self.calculate_result)

    def append_to_display(self, text):
        self.display.setText(self.display.text() + text)

    def clear_display(self):
        self.display.clear()

    def calculate_result(self):
        try:
            # eval für die Berechnung
            result = eval(self.display.text())
            self.display.setText(str(result))
        except Exception:
            self.display.setText("Error")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
