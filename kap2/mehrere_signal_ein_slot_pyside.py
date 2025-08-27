import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QSlider, QSpinBox, QGridLayout
)
from PySide6.QtCore import Qt


class MultiSignalsOneSlot(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mehrere Signale, ein Slot")

        layout = QGridLayout()
        self.label = QLabel("Wert")
        # QLabel
        layout.addWidget(self.label, 0, 0)


        # QSlider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setValue(1)
        layout.addWidget(self.slider, 1, 0)

        # QSpinBox
        self.spin = QSpinBox()
        self.spin.setValue(1)
        layout.addWidget(self.spin, 1, 1)
        self.slider.valueChanged.connect(self.update_label)
        self.spin.valueChanged.connect(self.update_label)

        self.setLayout(layout)
    def update_label(self):
        wert = int(self.spin.value()) + int(self.slider.value())
        self.label.setText(
            f"Gesamtwert: {wert}, SpinBox: {self.spin.value()}, Slider: {self.slider.value()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MultiSignalsOneSlot()
    w.resize(450, 80)
    w.show()
    sys.exit(app.exec())
