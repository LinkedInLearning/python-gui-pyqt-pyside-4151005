import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel("Hallo")
label.show()

sys.exit(app.exec())
