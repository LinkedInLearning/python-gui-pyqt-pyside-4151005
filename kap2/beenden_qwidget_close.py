from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow

app = QApplication([])

window = QMainWindow()
button = QPushButton("Fenster schließen")
button.clicked.connect(window.close)
window.setCentralWidget(button)
window.show()

app.exec()
