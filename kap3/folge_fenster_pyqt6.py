import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget


class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Folgefenster")
        self.resize(300, 200)
        #self.move(50,50)
        #x = self.pos().x()
        #y = self.pos().y()
        

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Hallo, ich bin das zweite Fenster!"))
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hauptfenster")
        self.resize(300, 100)

        # Button zum Öffnen des zweiten Fensters
        button = QPushButton("Folgefenster öffnen")
        button.clicked.connect(self.open_second_window)

        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(button)
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Referenz für das zweite Fenster (wichtig, sonst wird es vom Garbage Collector zerstört)
        self.second_window = None

    def open_second_window(self):
        if self.second_window is None:
            self.second_window = SecondWindow()
        self.second_window.show()
        self.second_window.raise_()   # nach vorne bringen
        self.second_window.activateWindow()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
