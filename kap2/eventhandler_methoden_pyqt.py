from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtCore import Qt

class MyLabel(QLabel):
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.setText("Leertaste gedrückt!")

app = QApplication([])
label = MyLabel("Drücke die Leertaste")
label.setFixedSize(300, 100)
label.show()
app.exec()
