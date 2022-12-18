from fVec2 import cVec2


class cBall:
    def __init__(self, x=0, y=0, xParent=None):
        self.xPos = cVec2(x, y)
        self.xVel = cVec2(10, 0)
        self.xRadius = xParent.xRadius
        self.xFps    = xParent.xFps
        self.xAirVec = cVec2(*(1 - (xParent.xAirRes / self.xFps) for _ in range(2)))
        self.xParent = xParent
        
        #delta time scale vector
        self.xDtScale = cVec2(xParent.xFps, xParent.xFps)
        
        #gravity
        self.xGrv = cVec2(0, -9.81) / self.xDtScale
        
        
        
    def Do(self):
        #get momentary acceleration
        xAcc = self.xGrv
        
        #collision detection, for future velocity
        xFuture = self.xPos + self.xVel
        xBound = self.xRadius < xFuture.xVal < self.xParent.xSize.xVal + self.xRadius
        yBound = self.xRadius < xFuture.yVal < self.xParent.xSize.yVal + self.xRadius
        self.xVel *= cVec2(
            1 if xBound else -1 + self.xParent.xBounceLoss, 
            1 if yBound else -1 + self.xParent.xBounceLoss,
        )

        #move
        if yBound:
            self.xVel += xAcc
            
        self.xPos += self.xVel
        
        #air resistance
        self.xVel *= self.xAirVec
        
    def Draw(self, qP):
        qP.drawEllipse(
            self.xPos.xVal,
            self.xParent.xSize.yVal - self.xPos.yVal,
            self.xRadius,
            self.xRadius,                
        )
