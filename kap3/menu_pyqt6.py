import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QMessageBox
from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # zentrales Widget
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        # Menüleiste
        menu_bar = self.menuBar()

        # Datei-Menü
        file_menu = menu_bar.addMenu("&Datei")

        # Aktion "Neu"
        new_action = QAction("Neu", self)
        new_action.triggered.connect(self.on_new)  # Signal -> Slot
        file_menu.addAction(new_action)

        # Aktion "Beenden"
        exit_action = QAction("Beenden", self)
        exit_action.triggered.connect(self.close)  # Signal -> Slot
        file_menu.addAction(exit_action)

        # Hilfe-Menü
        help_menu = menu_bar.addMenu("&Hilfe")

        about_action = QAction("Über", self)
        about_action.triggered.connect(self.on_about)
        help_menu.addAction(about_action)

        # Fenster-Einstellungen
        self.setWindowTitle("PyQt6 Menü-Beispiel")
        self.resize(600, 400)

    # Slot-Funktion für "Neu"
    def on_new(self):
        self.text_edit.clear()

    # Slot-Funktion für "Über"
    def on_about(self):
        QMessageBox.information(self, "Über", "Dies ist ein einfaches PyQt6-Menü-Beispiel.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

