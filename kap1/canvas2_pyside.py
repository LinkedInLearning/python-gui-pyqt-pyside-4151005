from PySide6.QtWidgets import (
    QApplication, QGraphicsScene, QGraphicsView,
    QGraphicsEllipseItem, QGraphicsRectItem,
    QGraphicsLineItem, QGraphicsPolygonItem
)
from PySide6.QtGui import QBrush, QPen, QPolygonF
from PySide6.QtCore import QRectF, Qt, QPointF
import sys


class GraphicsCanvas(QGraphicsView):
    def __init__(self):
        super().__init__()

        # Szene erstellen
        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        # Shapes hinzufügen
        self._add_shapes()

        # Fenster konfigurieren
        self.setWindowTitle("Canvas mit QGraphicsView und Primitiven (PySide6)")
        self.resize(400, 300)

    def _add_shapes(self):
        """Hilfsmethode zum Hinzufügen der geometrischen Primitive."""

        # ===== Kreis =====
        ellipse = QGraphicsEllipseItem(QRectF(0, 0, 100, 100))
        ellipse.setBrush(QBrush(Qt.red))
        ellipse.setPen(QPen(Qt.blue, 2))
        self.scene.addItem(ellipse)

        # ===== Rechteck =====
        rect = QGraphicsRectItem(QRectF(120, 0, 100, 60))
        rect.setBrush(QBrush(Qt.green))
        rect.setPen(QPen(Qt.black, 2))
        self.scene.addItem(rect)

        # ===== Linie =====
        line = QGraphicsLineItem(0, 120, 200, 120)
        line.setPen(QPen(Qt.black, 3))
        self.scene.addItem(line)

        # ===== Polygon (Dreieck) =====
        points = [QPointF(250, 50), QPointF(300, 150), QPointF(200, 150)]
        polygon = QGraphicsPolygonItem(QPolygonF(points))
        polygon.setBrush(QBrush(Qt.yellow))
        polygon.setPen(QPen(Qt.darkMagenta, 2))
        self.scene.addItem(polygon)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GraphicsCanvas()
    window.show()
    sys.exit(app.exec())
