from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
import sys

class NestedLayoutExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Verschachteltes Layout")
        self.setGeometry(100, 100, 300, 200)

        # Hauptlayout (vertikal)
        main_layout = QVBoxLayout()

        # Oben ein Label
        label = QLabel("Oben im vertikalen Layout")
        main_layout.addWidget(label)

        # Unteres Layout (horizontal)
        h_layout = QHBoxLayout()
        h_layout.addWidget(QPushButton("Button links"))
        h_layout.addWidget(QPushButton("Button rechts"))

        # Das horizontale Layout ins vertikale einfügen
        main_layout.addLayout(h_layout)

        # Hauptlayout setzen
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NestedLayoutExample()
    window.show()
    sys.exit(app.exec())
