import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QWidget, QMessageBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTreeView + QStandardItemModel")
        self.resize(500, 400)

        container = QWidget()
        layout = QVBoxLayout()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # TreeView erstellen
        self.tree_view = QTreeView()
        layout.addWidget(self.tree_view)

        # Model erstellen
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Name", "Typ"])

        # Wurzelknoten
        root1 = QStandardItem("Dokumente")
        root1_type = QStandardItem("Ordner")

        root2 = QStandardItem("Bilder")
        root2_type = QStandardItem("Ordner")

        # Kinder hinzufügen
        file1 = [QStandardItem("Lebenslauf.pdf"), QStandardItem("Datei")]
        file2 = [QStandardItem("Rechnung.docx"), QStandardItem("Datei")]
        root1.appendRow(file1)
        root1.appendRow(file2)

        img1 = [QStandardItem("Urlaub.jpg"), QStandardItem("Datei")]
        img2 = [QStandardItem("Geburtstag.png"), QStandardItem("Datei")]
        root2.appendRow(img1)
        root2.appendRow(img2)

        # Wurzeln ins Model
        self.model.appendRow([root1, root1_type])
        self.model.appendRow([root2, root2_type])

        # Model mit TreeView verbinden
        self.tree_view.setModel(self.model)
        self.tree_view.expandAll()  # optional: alle Knoten aufklappen

        # Signal/Slot: Klick auf Knoten
        self.tree_view.clicked.connect(self.on_item_clicked)

    # Slot-Methode
    def on_item_clicked(self, index):
        # index ist ein QModelIndex
        item = self.model.itemFromIndex(index)
        QMessageBox.information(self, "Knoten geklickt", f"Du hast '{item.text()}' angeklickt.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
