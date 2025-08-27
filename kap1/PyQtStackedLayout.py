from PyQt6.QtWidgets import (
    QApplication, QWidget, QStackedLayout, QPushButton, QLabel, QVBoxLayout
)
import sys

class StackedExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StackedLayout")

        self.layout = QStackedLayout()

        self.page1 = QWidget()
        layout1 = QVBoxLayout()
        layout1.addWidget(QLabel("Page 1"))
        btn1 = QPushButton("Go to Page 2")
        btn1.clicked.connect(self.show_page2)
        layout1.addWidget(btn1)
        self.page1.setLayout(layout1)

        self.page2 = QWidget()
        layout2 = QVBoxLayout()
        layout2.addWidget(QLabel("Page 2"))
        btn2 = QPushButton("Go to Page 1")
        btn2.clicked.connect(self.show_page1)
        layout2.addWidget(btn2)
        self.page2.setLayout(layout2)

        self.layout.addWidget(self.page1)
        self.layout.addWidget(self.page2)

        self.setLayout(self.layout)

    def show_page2(self):
        self.layout.setCurrentIndex(1)

    def show_page1(self):
        self.layout.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StackedExample()
    window.show()
    sys.exit(app.exec())
