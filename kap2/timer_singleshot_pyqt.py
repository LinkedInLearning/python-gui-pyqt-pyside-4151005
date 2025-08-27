from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel("Warte 2 Sekunden...")
label.show()

# Nach 2000 ms Text ändern
QTimer.singleShot(2000, lambda: label.setText("Zeit abgelaufen!"))

app.exec()
