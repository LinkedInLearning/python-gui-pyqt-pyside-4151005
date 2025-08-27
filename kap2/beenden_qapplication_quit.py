from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication([])

button = QPushButton("Beenden")
button.clicked.connect(app.quit)   # sauberes Beenden
button.show()

app.exec()
