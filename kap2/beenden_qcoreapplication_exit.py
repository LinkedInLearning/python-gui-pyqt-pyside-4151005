from PySide6.QtCore import QCoreApplication, QTimer
from PySide6.QtWidgets import QApplication

app = QApplication([])

# nach 3 Sekunden beenden mit Code 42
QTimer.singleShot(3000, lambda: QCoreApplication.exit(42))

exit_code = app.exec()
print(f"Die Anwendung wurde mit Code {exit_code} beendet.")
