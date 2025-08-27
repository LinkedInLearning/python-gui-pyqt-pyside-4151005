from PyQt6.QtWidgets import QApplication, QPushButton, QLabel
from PyQt6.QtCore import QObject, QEvent

class MyFilter(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            print("Button-Klick abgefangen!")
            return True   # Event nicht weitergeben
        return False      # Standardverarbeitung erlauben

app = QApplication([])
button = QPushButton("Klick mich")
filter = MyFilter()
button.installEventFilter(filter)
button.show()
app.exec()
