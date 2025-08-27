import sys
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

label = QLabel("Hallo mit PyQt5!")
label.resize(300, 100)
label.show()

sys.exit(app.exec_())
