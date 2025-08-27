import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout

class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6-Fenster mit Signal-Slot-Reaktion")
        self.setGeometry(0,0,450,80)
        
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

        # Button-Klick mit Funktion verbinden - hier mit Lambda statt Methodenreferenz
  
        self.button.clicked.connect(
            lambda: self.label.setText(f"Du hast eingegeben: {self.input_field.text()}"))  # Slot: Lambda

        # Layout setzen
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleWindow()
    window.show()
    sys.exit(app.exec())
