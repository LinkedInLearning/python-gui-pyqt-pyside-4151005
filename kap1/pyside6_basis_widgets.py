import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit, QTextEdit,
    QCheckBox, QRadioButton, QComboBox, QListWidget, QTableWidget,
    QTableWidgetItem, QSlider, QProgressBar, QGridLayout
)
from PySide6.QtCore import Qt


class WidgetDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basis-Widgets")

        layout = QGridLayout()

        # QLabel
        layout.addWidget(QLabel("👉 QLabel (Textanzeige)"), 0, 0)

        # QPushButton
        layout.addWidget(QPushButton("QPushButton"), 0, 1)

        # QLineEdit
        layout.addWidget(QLineEdit("QLineEdit: Text hier"), 1, 0)

        # QTextEdit
        layout.addWidget(QTextEdit("QTextEdit: Mehrzeiliger Text"), 1, 1)

        # QCheckBox
        layout.addWidget(QCheckBox("QCheckBox"), 2, 0)

        # QRadioButton
        layout.addWidget(QRadioButton("QRadioButton"), 2, 1)

        # QComboBox
        combo = QComboBox()
        combo.addItems(["Option 1", "Option 2", "Option 3"])
        layout.addWidget(combo, 3, 0)

        # QListWidget
        list_widget = QListWidget()
        list_widget.addItems(["Eintrag A", "Eintrag B", "Eintrag C"])
        layout.addWidget(list_widget, 3, 1)

        # QTableWidget
        table = QTableWidget(2, 2)
        table.setHorizontalHeaderLabels(["Spalte 1", "Spalte 2"])
        table.setItem(0, 0, QTableWidgetItem("Zelle (0,0)"))
        table.setItem(0, 1, QTableWidgetItem("Zelle (0,1)"))
        table.setItem(1, 0, QTableWidgetItem("Zelle (1,0)"))
        table.setItem(1, 1, QTableWidgetItem("Zelle (1,1)"))
        layout.addWidget(table, 4, 0, 1, 2)

        # QSlider
        slider = QSlider(Qt.Horizontal)
        layout.addWidget(slider, 5, 0)

        # QProgressBar
        progress = QProgressBar()
        progress.setValue(40)
        layout.addWidget(progress, 5, 1)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = WidgetDemo()
    demo.resize(500, 400)
    demo.show()
    sys.exit(app.exec())
