import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabellen-Beispiel")
        self.resize(600, 400)

        # Zentrales Widget
        container = QWidget()
        layout = QVBoxLayout()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Tabelle erstellen
        table = QTableWidget()
        table.setRowCount(4)    # Anzahl der Zeilen
        table.setColumnCount(4) # Anzahl der Spalten
        table.setHorizontalHeaderLabels(["Name", "Alter", "Stadt","Typ"])

        # Daten einfügen
        data = [
            ("Susi", 5, "Mainz","Katze"),
            ("Strolch", 5, "Mainz","Kater"),
            ("Felix", 25, "Bodenheim","Mann"),
            ("Florian", 25, "Sontra","Mann")
        ]

        for row, (name, age, city, type) in enumerate(data):
            table.setItem(row, 0, QTableWidgetItem(name))
            table.setItem(row, 1, QTableWidgetItem(str(age)))
            table.setItem(row, 2, QTableWidgetItem(city))
            table.setItem(row, 3, QTableWidgetItem(type))

        # Tabelle ins Layout
        layout.addWidget(table)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
