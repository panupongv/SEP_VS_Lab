import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from main import Simple_drawing_window

class Simple_drawing_window_muse(Simple_drawing_window):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.dog = QPixmap("images/dog")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))

        p.setPen(QColor(255, 255, 0))
        p.setBrush(QColor(255, 255, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 30)

        p.drawPolygon(QPoint(150, 200), QPoint(100, 200))


        p.drawPixmap(QRect(200, 100, 320, 320), self.dog)
        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window_muse()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
