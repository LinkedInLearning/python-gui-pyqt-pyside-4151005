import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QMessageBox, QToolBar
)
from PyQt6.QtGui import QAction, QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # zentrales Widget
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)

 

        # Aktionen
        new_action = QAction(QIcon(), "Neu", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self.new_file)

        exit_action = QAction(QIcon(), "Beenden", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)

        about_action = QAction("Über", self)
        about_action.triggered.connect(self.show_about)

 

        # Toolbar erstellen und hinzufügen
        toolbar = QToolBar("Haupt-Werkzeugleiste")
        toolbar.addAction(new_action)   
        toolbar.addAction(exit_action)
        toolbar.addAction(about_action)

        self.addToolBar(toolbar)

        # Fenster
        self.setWindowTitle("Toolbar-Beispiel")
        self.resize(600, 400)

    # Slots
    def new_file(self):
        self.editor.clear()

    def show_about(self):
        QMessageBox.information(self, "Über", "Einfaches Beispiel mit Toolbar.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
