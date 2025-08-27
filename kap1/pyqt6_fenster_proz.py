import sys
from PyQt6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

label = QLabel("Hallo mit PyQt6!")
label.resize(300, 100)
label.show()

# Achtung: exec_() gibt es in Qt6 nicht mehr, nur exec()
sys.exit(app.exec())
