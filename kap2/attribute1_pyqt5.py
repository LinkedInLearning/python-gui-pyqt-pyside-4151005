import sys
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])

label = QLabel("Hallo PyQt")
label.show()

# Text ändern
label.setText("Neuer Text")

# Text abfragen
print(label.text())

sys.exit(app.exec_())
