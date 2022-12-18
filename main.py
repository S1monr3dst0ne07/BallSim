
from PyQt5 import QtGui, QtWidgets, QtCore
from fWindow import cWindow
import sys

if __name__ == '__main__':
    xApp = QtWidgets.QApplication(sys.argv)
    xWindow = cWindow()
    sys.exit(xApp.exec())
    
    