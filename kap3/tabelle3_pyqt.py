import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
)
from PyQt6.QtGui import QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabellen mit Signal/Slot")
        self.resize(600, 400)

        # Zentrales Widget
        container = QWidget()
        layout = QVBoxLayout()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Tabelle erstellen
        self.table = QTableWidget()
        self.table.setRowCount(4)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Name", "Alter", "Stadt","Typ"])

        # Daten einfügen
        data = [
            ("Susi", 5, "Mainz","Katze"),
            ("Strolch", 5, "Mainz","Kater"),
            ("Felix", 25, "Bodenheim","Mann"),
            ("Florian", 25, "Sontra","Mann")
        ]

        for row, (name, age, city, type) in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(str(age)))
            self.table.setItem(row, 2, QTableWidgetItem(city))
            self.table.setItem(row, 3, QTableWidgetItem(type))
        # Signal/Slot verbinden: Klick auf Zelle
        self.table.cellClicked.connect(self.cell_clicked)

        layout.addWidget(self.table)

    # Slot: Hintergrundfarbe ändern
    def cell_clicked(self, row, column):
        item = self.table.item(row, column)
        if item is not None:
            # Farbe zufällig auswählen (hier rot als Beispiel)
            item.setBackground(QColor(255, 200, 200))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
