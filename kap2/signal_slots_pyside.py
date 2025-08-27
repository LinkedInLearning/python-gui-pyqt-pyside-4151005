import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout

class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Einfaches PySide6-Fenster")

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

        # Button-Klick mit Funktion verbinden
        self.button.clicked.connect(self.on_button_clicked)

        # Layout setzen
        self.setLayout(layout)

    def on_button_clicked(self):
        text = self.input_field.text()
        self.label.setText(f"Du hast eingegeben: {text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleWindow()
    window.show()
    sys.exit(app.exec())
