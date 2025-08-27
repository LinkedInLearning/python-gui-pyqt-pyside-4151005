from PyQt6.QtCore import QObject, pyqtSignal, QTimer   # Unterschied: pyqtSignal statt Signal
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QWidget


class Worker(QObject):
    # In PyQt6: pyqtSignal, in PySide6: Signal
    started = pyqtSignal()
    finished = pyqtSignal(str)

    def run(self):
        # Signal aussenden: "gestartet"
        self.started.emit()

        # Simuliere eine längere "Arbeit" (3 Sekunden Verzögerung)
        QTimer.singleShot(3000, lambda: self.finished.emit("Arbeit abgeschlossen!"))


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Signal/Slot Beispiel mit PyQt6")
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

        # Button-Klick startet Worker
        self.button.clicked.connect(self.start_worker)

    def start_worker(self):
        self.worker.run()

    def on_worker_started(self):
        self.label.setText("Worker läuft...")

    def on_worker_finished(self, msg):
        self.label.setText(msg)


# Main-Loop
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
