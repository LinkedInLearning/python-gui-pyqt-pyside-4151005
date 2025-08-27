import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget
from PyQt6.QtGui import QStandardItemModel, QStandardItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTableView Beispiel")
        self.resize(600, 400)

        # Zentrales Widget
        container = QWidget()
        layout = QVBoxLayout()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Tabelle erstellen
        table_view = QTableView()
        layout.addWidget(table_view)

        # Datenmodell erstellen
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Name", "Alter", "Stadt","Typ"])

        # Daten einfügen
        data = [
            ("Susi", 5, "Mainz","Katze"),
            ("Strolch", 5, "Mainz","Kater"),
            ("Felix", 25, "Bodenheim","Mann"),
            ("Florian", 25, "Sontra","Mann")
        ]


        for row_data in data:
            items = [QStandardItem(str(field)) for field in row_data]
            model.appendRow(items)

        # Model mit TableView verbinden
        table_view.setModel(model)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
