import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget, QMessageBox
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTreeWidget mit Signal/Slot")
        self.resize(400, 300)

        container = QWidget()
        layout = QVBoxLayout()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Baum erstellen
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Name", "Typ"])

        # Wurzelknoten
        root1 = QTreeWidgetItem(["Dokumente", "Ordner"])
        root2 = QTreeWidgetItem(["Bilder", "Ordner"])

        # Kinder
        file1 = QTreeWidgetItem(["Lebenslauf.pdf", "Datei"])
        file2 = QTreeWidgetItem(["Rechnung.docx", "Datei"])
        root1.addChild(file1)
        root1.addChild(file2)

        img1 = QTreeWidgetItem(["Urlaub.jpg", "Datei"])
        img2 = QTreeWidgetItem(["Geburtstag.png", "Datei"])
        root2.addChild(img1)
        root2.addChild(img2)

        # Wurzeln hinzufügen
        self.tree.addTopLevelItem(root1)
        self.tree.addTopLevelItem(root2)

        # Signal/Slot: Klick auf einen Knoten
        self.tree.itemClicked.connect(self.on_item_clicked)

        layout.addWidget(self.tree)

    # Slot-Methode
    def on_item_clicked(self, item, column):
        QMessageBox.information(self, "Knoten geklickt", f"Du hast '{item.text(0)}' angeklickt.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
