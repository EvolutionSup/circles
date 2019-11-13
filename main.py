import sys

from random import randint
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QColor
from UI import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.draw = False
        self.setupUi(self)
        self.btn.clicked.connect(self.flag)

    def flag(self):
        self.draw = True
        self.update()

    def paintEvent(self, event):
        if self.draw:
            self.draw = False
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()

    def draw_circles(self, qp):
        r = randint(20, 100)  # радиус окружности
        for i in range(randint(1, 200)):
            qp.setRenderHint(QPainter.Antialiasing)
            qp.setPen(QPen(Qt.yellow, 5, Qt.SolidLine))
            qp.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            qp.drawEllipse(randint(25, 445), randint(30, 520), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
