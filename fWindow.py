
from PyQt5 import QtGui, QtWidgets, QtCore
from fBall import cBall
from fVec2 import cVec2
from random import randint


class cWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.xRadius = 20
        self.xFps = 120
        self.xSize = cVec2(1500, 700)
        
        #percentage of velocity lost to air resistance
        self.xAirRes = 0.35

        #percentage of velocity lost when colliding
        self.xBounceLoss = 0.05

        self.xBalls = [cBall(
            randint(0, self.xSize.xVal),
            randint(0, self.xSize.yVal),
            self) for x in range(10)]
        
        self.xTimer = QtCore.QTimer()
        self.xTimer.timeout.connect(self.Do)
        self.xTimer.setInterval(1000 / self.xFps)
        self.xTimer.start()
        
        self.setFixedSize(*self.xSize)
        self.show()
        
        
    def paintEvent(self, xE):
        qP = QtGui.QPainter(self)
        qP.setBrush(QtGui.QBrush(QtCore.Qt.black, QtCore.Qt.SolidPattern))
        
        for xBall in self.xBalls:
            xBall.Draw(qP)
            
    def Do(self):
        for xBall in self.xBalls:
            xBall.Do()

        self.update()
