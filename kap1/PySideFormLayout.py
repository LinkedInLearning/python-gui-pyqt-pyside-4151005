from PySide6.QtWidgets import QApplication, QWidget, QFormLayout, QPushButton, QLabel
import sys

class FormExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FormLayout")

        layout = QFormLayout()
        layout.addRow("Label:", QLabel("FormLayout Label"))
        layout.addRow("Button:", QPushButton("FormLayout Button"))

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormExample()
    window.show()
    sys.exit(app.exec())
