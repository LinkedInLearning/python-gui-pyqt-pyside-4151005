import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QPushButton, QPlainTextEdit
)
from PySide6.QtGui import QIcon


class EditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini-Editor (PySide6)")
        self.resize(900, 600)

        # Zentrales Widget + Hauptlayout
        central = QWidget(self)
        self.setCentralWidget(central)
        root = QVBoxLayout(central)
        root.setContentsMargins(12, 12, 12, 12)
        root.setSpacing(8)

        # Button-Zeile (ohne Eventhandling)
        btn_row = QHBoxLayout()
        btn_row.setSpacing(8)

        self.btn_open = QPushButton("Öffnen")
        self.btn_open.setObjectName("btnOpen")
        self.btn_open.setIcon(QIcon.fromTheme("document-open"))

        self.btn_save = QPushButton("Speichern")
        self.btn_save.setObjectName("btnSave")
        self.btn_save.setIcon(QIcon.fromTheme("document-save"))

        btn_row.addWidget(self.btn_open)
        btn_row.addWidget(self.btn_save)
        btn_row.addStretch()  # schiebt die Buttons nach links

        # Einfaches Editor-Widget
        self.editor = QPlainTextEdit()
        self.editor.setPlaceholderText("Hier tippen …")
        self.editor.setTabStopDistance(4 * self.editor.fontMetrics().horizontalAdvance(' '))

        # Layout zusammenbauen
        root.addLayout(btn_row)
        root.addWidget(self.editor)

        # Optional: Statuszeile
        self.statusBar().showMessage("Bereit")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = EditorWindow()
    win.show()
    sys.exit(app.exec())
