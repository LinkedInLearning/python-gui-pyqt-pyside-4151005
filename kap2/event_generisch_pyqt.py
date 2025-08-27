from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtCore import QEvent


class MyLabel(QLabel):
    def event(self, event):
        if event.type() == QEvent.Type.Enter:
            self.setText("Maus über dem Label")
        elif event.type() == QEvent.Type.Leave:
            self.setText("Maus hat das Label verlassen")
        # Standardverhalten beibehalten
        return super().event(event)


app = QApplication([])
label = MyLabel("Hallo")
label.setFixedSize(300, 100)
label.show()
app.exec()
