import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Cyrcle(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.qp = QPainter()
        self.pushButton.clicked.connect(self.get_new_coord)
        self.yellows_cyrcles = []
        self.qp.setPen(QColor(255, 255, 0))

    def paintEvent(self, QPaintEvent):
        if self.yellows_cyrcles:
            self.qp.begin(self)
            for x_y_r in self.yellows_cyrcles:
                x, y, r = x_y_r
                self.qp.drawEllipse(x, y, r, r)
            self.qp.end()
            self.update()

    def get_new_coord(self):
        x = randint(100, 500)
        y = randint(100, 300)
        r = randint(10, 100)
        self.yellows_cyrcles.append((x, y, r))



if __name__ == '__main__':
    app = QApplication(sys.argv)
ex = Cyrcle()
ex.move(600, 400)
ex.show()
sys.exit(app.exec_())
