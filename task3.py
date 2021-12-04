import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 300, 300)
        self.setWindowTitle('3 задача')

        self.btn = QPushButton('CLICK', self)
        self.btn.setGeometry(80, 230, 150, 41)


class MyWidget(Window):
    def __init__(self):
        super().__init__()
        self.btn.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(*[randint(0, 255) for i in range(3)]))
        x = randint(0, 300)
        w = randint(0, 300 - x)
        y = randint(0, 210)
        h = randint(0, 210 - y)
        qp.drawEllipse(x, y, w, h)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())