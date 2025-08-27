import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

label = QLabel("Hallo mit PySide6!")
label.resize(300, 100)
label.show()

sys.exit(app.exec())
