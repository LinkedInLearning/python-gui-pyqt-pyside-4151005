from PySide6.QtCore import QObject, Signal, QTimer
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QWidget


# Worker-Klasse mit eigenem Signal
class Worker(QObject):
    # Benutzerdefiniertes Signal (ohne Argument + mit String-Argument)
    started = Signal()
    finished = Signal(str)

    def run(self):
        # Signal aussenden: "gestartet"
        self.started.emit()
        # Nach einer kurzen "Arbeitspause" fertig melden
        QTimer.singleShot(3000, lambda: self.finished.emit("Arbeit abgeschlossen!"))

# Hauptfenster
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Signal/Slot Beispiel mit PySide6")
        self.resize(300, 150)

        # Widgets
        self.label = QLabel("Bereit")
        self.button = QPushButton("Starte Worker")

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Worker-Instanz
        self.worker = Worker()

        # Signale verbinden
        self.worker.started.connect(self.on_worker_started)
        self.worker.finished.connect(self.on_worker_finished)

        # Button-Klick starten
        self.button.clicked.connect(self.start_worker)

    def start_worker(self):
        # Hier könnte man einen Thread starten – für das Beispiel nutzen wir einen Timer
        QTimer.singleShot(500, self.worker.run)  # Worker nach 0,5s starten

    def on_worker_started(self):
        self.label.setText("Worker läuft...")

    def on_worker_finished(self, msg):
        self.label.setText(msg)


# Main-Loop starten
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
