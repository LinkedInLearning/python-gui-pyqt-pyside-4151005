import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot

class Backend(QObject):
    @Slot()
    def button_clicked(self):
        print("Button wurde geklickt!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    backend = Backend()

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("backend", backend)
    engine.load("main3.qml")

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
