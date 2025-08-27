import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QFormLayout

class OneSignalMultiSlots(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide-Fenster mit einem Signal und mehreren Slots")
        self.setGeometry(0,0,450,80)      
        self.label1 = QLabel("Multiplikation")
        self.label2 = QLabel("Addition")
        layout = QFormLayout()
        # 1. Eingabefeld 
        self.value1 = QLineEdit()
        # 2. Eingabefeld 
        self.value2 = QLineEdit()
        # Button 
        self.button = QPushButton("Rechne")
        layout.addRow("Zahl 1:", self.value1)
        layout.addRow("Zahl 2:", self.value2)
        layout.addRow("Button:", self.button)
        layout.addRow(self.label1, self.label2)

        # Button-Klick mit zwei Slots verbinden
        self.button.clicked.connect(self.multi)
        self.button.clicked.connect(self.add)

        # Layout setzen
        self.setLayout(layout)

    def multi(self):
        z1 = int(self.value1.text())
        z2 = int(self.value2.text())
        erg = z1 * z2
        self.label1.setText(f"{z1} * {z2}: {erg}")
    def add(self):
        z1 = int(self.value1.text())
        z2 = int(self.value2.text())
        erg = z1 + z2
        self.label2.setText(f"{z1} + {z2}: {erg}")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = OneSignalMultiSlots()
    w.show()
    sys.exit(app.exec())
