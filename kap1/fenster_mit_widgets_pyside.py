import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout

class MeinFenster(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ein PyQt5-Fenster mit Widgets")
        self.setGeometry(100, 100, 350, 100)  # x, y, Breite, Höhe
        # Layout erstellen
        layout = QVBoxLayout()
        # Label hinzufügen
        self.label = QLabel("Gib etwas ein:")
        layout.addWidget(self.label)
        # Eingabefeld hinzufügen
        self.input_field = QLineEdit()
        layout.addWidget(self.input_field)
        # Button hinzufügen
        self.button = QPushButton("Klick mich")
        layout.addWidget(self.button)
        # Layout setzen
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MeinFenster()
    window.show()
    sys.exit(app.exec())
