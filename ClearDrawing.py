import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *
from Lab8_2 import Simple_drawing_window


class ClearDrawing(Simple_drawing_window):
     def clear_points(self):
        self.points.clear()
