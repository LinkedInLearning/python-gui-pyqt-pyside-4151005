import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QVBoxLayout, QWidget, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QListWidget-Beispiel")
        self.resize(400, 300)

        container = QWidget()
        layout = QVBoxLayout()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # QListWidget erstellen
        self.list_widget = QListWidget()

        # Elemente hinzufügen
        items = ["Apfelsaft", "Bananensaft", "Kirschsaft", "Cola", "Limonade"]
        self.list_widget.addItems(items)

        # Signal/Slot: Klick auf ein Element
        self.list_widget.itemClicked.connect(self.on_item_clicked)

        layout.addWidget(self.list_widget)

    def on_item_clicked(self, item):
        QMessageBox.information(self, "Ausgewählt: ", f"{item.text()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
