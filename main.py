import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.draw = False
        uic.loadUi('UI.ui', self)
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
        for i in range(randint(1, 20)):
            qp.setPen(QPen(Qt.yellow, 5, Qt.SolidLine))
            qp.drawEllipse(randint(10, 400), randint(10, 400), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
