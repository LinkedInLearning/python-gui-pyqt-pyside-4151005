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
        

        # Widgets
        

        # Layout
        

        # Signale
        

        # Tabelle laden
        

    def load_data(self):
        """Lädt alle Daten aus der Datenbank in die Tabelle."""
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM personen")
        rows = cursor.fetchall()
        conn.close()
        # Daten in Tabelle

    def add_entry(self):
        """Fügt neuen Eintrag in die DB ein und aktualisiert Tabelle."""

        # Kontrolle, ob Felder korrket

        # SQL ausführen - Variablen müssen vorher deklariert und gefüllt werden
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO personen (name, age) VALUES (?, ?)", (name, int(age_text)))
        conn.commit()
        conn.close()
        # Eingabefelder leeren
     
        # Daten laden
    

if __name__ == "__main__":
    pass
