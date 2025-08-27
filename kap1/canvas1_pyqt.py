from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import QRectF, Qt
import sys

app = QApplication(sys.argv)

# Szene erstellen
scene = QGraphicsScene()

# Ellipse erstellen
ellipse = QGraphicsEllipseItem(QRectF(0, 0, 100, 100))

# Farben setzen: Füllung = rot, Rand = blau
ellipse.setBrush(QBrush(Qt.red))       # Innenfarbe
ellipse.setPen(QPen(Qt.blue, 2))       # Randfarbe und -dicke

# Ellipse zur Szene hinzufügen
scene.addItem(ellipse)

# Ansicht erstellen
view = QGraphicsView(scene)
view.setWindowTitle("Canvas mit QGraphicsView")
view.resize(400, 300)
view.show()

sys.exit(app.exec_())
