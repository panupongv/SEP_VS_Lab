import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.points = []

        self.resize(400, 300)

        self.label = QLabel(self)
        self.label.setText("Drag mouse to draw")
        self.label.move(140, 260)

        self.button = QPushButton(self)
        self.button.setText("Clear")
        self.button.move(140, 280)
        self.button.clicked.connect(self.clear_points)

    def clear_points(self):
        self.points.clear()

    def mouseMoveEvent(self, event):
        #if event.buttons() == QtCore.Qt.LeftButton:
        self.points.append(event.pos())
        #print(event.pos()[0])
        
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 0, 0))
        for point in self.points:
        p.end()

        self.update()
        
def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())

