from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer

app = QApplication([])

def cleanup():
    print("Aufräumen vor dem Exit...")

app.aboutToQuit.connect(cleanup)

QTimer.singleShot(2000, app.quit)
app.exec()
