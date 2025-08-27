from PySide6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem
from PySide6.QtGui import QBrush, QPen
from PySide6.QtCore import QRectF, Qt
import sys

app = QApplication(sys.argv)

# Szene erstellen
scene = QGraphicsScene()

# Ellipse erstellen und einfärben
ellipse = QGraphicsEllipseItem(QRectF(0, 0, 100, 100))
ellipse.setBrush(QBrush(Qt.red))       # Füllung rot
ellipse.setPen(QPen(Qt.blue, 2))       # Rand blau

scene.addItem(ellipse)

# Ansicht erstellen
view = QGraphicsView(scene)
view.setWindowTitle("Canvas mit QGraphicsView (PySide6)")
view.resize(400, 300)
view.show()

sys.exit(app.exec())
