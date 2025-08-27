import sys
from PySide6.QtWidgets import QPushButton, QApplication
app = QApplication([])
button = QPushButton("Click me")
button.show()

# Größe setzen
button.resize(200, 50)

# Größe abfragen
print(button.size().width(), button.size().height())
sys.exit(app.exec())
