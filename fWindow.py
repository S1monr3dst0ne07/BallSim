
from PyQt5 import QtGui, QtWidgets, QtCore
from fVec2 import cVec2


class cWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.xBalls = [cVec2(100, 100)]
        self.xRadius = 10
        
        self.setFixedSize(1500, 700)
        self.show()
        
        
    def paintEvent(self, xE):
        qP = QtGui.QPainter(self)
        
        for xBall in self.xBalls:
            qP.drawEllipse(
                xBall.xVal,
                xBall.yVal,
                self.xRadius,
                self.xRadius,
                
            )