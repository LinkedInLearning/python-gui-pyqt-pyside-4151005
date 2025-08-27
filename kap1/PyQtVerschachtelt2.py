from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
import sys

class NestedLayoutExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Verschachteltes Layout mit Abständen")
        self.setGeometry(100, 100, 450, 200)

        # Hauptlayout (vertikal)
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(15, 20, 15, 20)  # Abstand zum Fensterrand
        main_layout.setSpacing(25)  # Abstand zwischen Label und HBox

        # Label oben
        label = QLabel("Oben im vertikalen Layout")
        main_layout.addWidget(label)

        # Unteres Layout (horizontal)
        h_layout = QHBoxLayout()
        h_layout.setContentsMargins(10, 0, 10, 0)  # Abstand innerhalb des Bereichs
        h_layout.setSpacing(40)  # Abstand zwischen den Buttons

        # Zwei Buttons hinzufügen
        h_layout.addWidget(QPushButton("Button links"))
        h_layout.addWidget(QPushButton("Button rechts"))

        # HBox ins VBox einfügen
        main_layout.addLayout(h_layout)

        # Hauptlayout anwenden
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NestedLayoutExample()
    window.show()
    sys.exit(app.exec())
