from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

app = QApplication([])

# UI-Datei öffnen
file = QFile("mainwindow.ui")
file.open(QFile.ReadOnly)

loader = QUiLoader()
window = loader.load(file)
file.close()

window.show()
app.exec()
