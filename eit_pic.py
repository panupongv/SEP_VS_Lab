import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from main import Simple_drawing_window

class Eit_pic(Simple_drawing_window):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/eit_pic.png")

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))

        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 300, 300, 0, 180 * 30)

        p.drawPolygon(QPoint(50, 400), QPoint(150, 200), QPoint(100, 400), QPoint(50, 200))

        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)

    w = Eit_pic()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())