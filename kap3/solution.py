import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem
)


DB_NAME = "database.db"


def init_db():
    """Erzeugt eine SQLite-Datenbank."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS personen (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Fenster aufbauen
        self.setWindowTitle("Datenbank-App mit PyQt6 & SQLite")
        self.resize(500, 300)

        # Widgets
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")

        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Alter")

        self.add_button = QPushButton("Hinzufügen")
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Alter"])

        # Layout
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.name_input)
        input_layout.addWidget(self.age_input)
        input_layout.addWidget(self.add_button)

        layout = QVBoxLayout()
        layout.addLayout(input_layout)
        layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Signale
        self.add_button.clicked.connect(self.add_entry)

        # Tabelle laden
        self.load_data()

    def load_data(self):
        """Lädt alle Daten aus der Datenbank in die Tabelle."""
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM personen")
        rows = cursor.fetchall()
        conn.close()
        # Daten in Tabelle
        self.table.setRowCount(len(rows))
        for row_idx, row_data in enumerate(rows):
            for col_idx, value in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def add_entry(self):
        """Fügt neuen Eintrag in die DB ein und aktualisiert Tabelle."""
        name = self.name_input.text().strip()
        age_text = self.age_input.text().strip()
        # Kontrolle, ob Felder korrket
        if not name or not age_text.isdigit():
            return  # ungültige Eingabe

        # SQL ausführen - Variablen müssen vorher deklariert und gefüllt werden
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO personen (name, age) VALUES (?, ?)", (name, int(age_text)))
        conn.commit()
        conn.close()
        # Eingabefelder leeren
        self.name_input.clear()
        self.age_input.clear()
        # Daten laden
        self.load_data()

if __name__ == "__main__":
    init_db()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
