from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsRectItem, QGraphicsLineItem, QGraphicsPolygonItem
from PyQt5.QtGui import QBrush, QPen, QPolygonF
from PyQt5.QtCore import QRectF, Qt, QPointF
import sys

app = QApplication(sys.argv)

# Szene erstellen
scene = QGraphicsScene()

# ===== Kreis =====
ellipse = QGraphicsEllipseItem(QRectF(0, 0, 100, 100))
ellipse.setBrush(QBrush(Qt.red))
ellipse.setPen(QPen(Qt.blue, 2))
scene.addItem(ellipse)

# ===== Rechteck =====
rect = QGraphicsRectItem(QRectF(120, 0, 100, 60))
rect.setBrush(QBrush(Qt.green))
rect.setPen(QPen(Qt.black, 2))
scene.addItem(rect)

# ===== Linie =====
line = QGraphicsLineItem(0, 120, 200, 120)
line.setPen(QPen(Qt.black, 3))
scene.addItem(line)

# ===== Geschlossener Polygonzug (Dreieck) =====
points = [QPointF(250, 50), QPointF(300, 150), QPointF(200, 150)]
polygon = QGraphicsPolygonItem(QPolygonF(points))
polygon.setBrush(QBrush(Qt.yellow))
polygon.setPen(QPen(Qt.darkMagenta, 2))
scene.addItem(polygon)

# ===== Ansicht =====
view = QGraphicsView(scene)
view.setWindowTitle("Canvas mit QGraphicsView und mehreren Primitiven")
view.resize(400, 300)
view.show()

sys.exit(app.exec_())
