import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from main import Simple_drawing_window

class Simple_drawing_window_most(Simple_drawing_window):
    def __init__(self):
        Simple_drawing_window.__init__(self)
    
        self.setWindowTitle("Most Drawing")
        self.rabbit = QPixmap("images/ig.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 180, 0))
        p.setBrush(QColor(0, 180, 0))
        p.drawPolygon(QPoint(95, 100), QPoint(105, 100), QPoint(100, 150)) 
        
        p.setPen(QColor(255, 0, 0))
        p.setBrush(QColor(255, 0, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 32)


        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window_most()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
