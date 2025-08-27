from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QLabel

class CounterLabel(QLabel):
    def __init__(self):
        super().__init__("0")
        self.count = 0

        # Timer alle 1000 ms (1 Sekunde)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_counter)
        self.timer.start(1000)

    def update_counter(self):
        self.count += 1
        self.setText(str(self.count))

app = QApplication([])
label = CounterLabel()
label.show()
app.exec()
