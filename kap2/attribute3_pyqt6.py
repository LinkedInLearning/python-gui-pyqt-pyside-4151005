import sys
from PyQt6.QtWidgets import QApplication, QLabel
app = QApplication([])

label = QLabel("Hallo PyQt6")
label.setStyleSheet("color: red; background-color: yellow")
label.show()



sys.exit(app.exec())
