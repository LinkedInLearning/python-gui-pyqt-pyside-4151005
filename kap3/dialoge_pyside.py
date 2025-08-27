import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QPushButton,
    QMessageBox, QColorDialog, QFileDialog, QFontDialog, QInputDialog
)
from PySide6.QtGui import QColor, QFont


class DialogDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialog-Demo")
        layout = QHBoxLayout()

        # Buttons
        btn_msg = QPushButton("Message")
        btn_color = QPushButton("Color Chooser")
        btn_open = QPushButton("Open File")
        btn_save = QPushButton("Save File")
        btn_font = QPushButton("Font Chooser")
        btn_input = QPushButton("Input Dialog")

        # Signale verbinden
        btn_msg.clicked.connect(self.show_message)
        btn_color.clicked.connect(self.choose_color)
        btn_open.clicked.connect(self.open_file)
        btn_save.clicked.connect(self.save_file)
        btn_font.clicked.connect(self.choose_font)
        btn_input.clicked.connect(self.input_dialog)

        # Layout befüllen
        for btn in (btn_msg, btn_color, btn_open, btn_save, btn_font, btn_input):
            layout.addWidget(btn)

        self.setLayout(layout)

    def show_message(self):
        QMessageBox.information(self, "Info", "Das ist eine Beispiel-Meldung.")

    def choose_color(self):
        color = QColorDialog.getColor(QColor("red"), self, "Farbe wählen")
        if color.isValid():
            QMessageBox.information(self, "Farbwahl", f"Gewählte Farbe: {color.name()}")

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Datei öffnen", "", "Alle Dateien (*.*)")
        if filename:
            QMessageBox.information(self, "Datei geöffnet", f"Gewählt: {filename}")

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Datei speichern", "", "Textdateien (*.txt)")
        if filename:
            QMessageBox.information(self, "Datei speichern", f"Speichern unter: {filename}")

    def choose_font(self):
        font, ok = QFontDialog.getFont(QFont("Arial", 12), self, "Schriftart wählen")
        if ok:
            QMessageBox.information(self, "Schriftwahl", f"Gewählte Schrift: {font.family()}, Größe {font.pointSize()}")

    def input_dialog(self):
        text, ok = QInputDialog.getText(self, "Eingabe", "Dein Name:")
        if ok and text:
            QMessageBox.information(self, "Hallo!", f"Hallo, {text}!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = DialogDemo()
    win.resize(600, 120)
    win.show()
    sys.exit(app.exec())
