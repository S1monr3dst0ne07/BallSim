


class cVec2:
    def __init__(self, x=0, y=0):
        self.xVal = x
        self.yVal = y
        
    def Op(self, xOp, xOth):
        return cVec2(
            xOp(self.xVal, xOth.xVal),
            xOp(self.yVal, xOth.yVal),
        )
        
    def IOp(self, xOp, xOth):
        self.xVal = xOp(self.xVal, xOth.xVal)
        self.yVal = xOp(self.yVal, xOth.yVal)
        return self
        
    def __add__(self, xOth):
        return self.Op(lambda x,y: x+y, xOth)
    def __sub__(self, xOth):
        return self.Op(lambda x,y: x-y, xOth)
    def __mul__(self, xOth):
        return self.Op(lambda x,y: x*y, xOth)
    def __truediv__(self, xOth):
        return self.Op(lambda x,y: x/y, xOth)

    def __iadd__(self, xOth):
        return self.IOp(lambda x,y: x+y, xOth)
    def __isub__(self, xOth):
        return self.IOp(lambda x,y: x-y, xOth)
    def __imul__(self, xOth):
        return self.IOp(lambda x,y: x*y, xOth)
    def __idiv__(self, xOth):
        return self.IOp(lambda x,y: x/y, xOth)

    def __iter__(self):
        return iter([self.xVal, self.yVal])