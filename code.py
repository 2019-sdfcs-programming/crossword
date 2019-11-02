#-*- coding:utf-8 -*-

import sys
#PyQt must be installed.

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

formClass = uic.loadUiType('PYQT.ui')[0]

class MainformClass(QMainWindow, formClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.B1.clicked.connect(self.b1)
        self.B2.clicked.connect(self.b2)
        self.B11.clicked.connect(self.b11)
        now = 0

    def initDisplay(self): 
        self.e.setPlainText('')
        self.label_14.setText('')

    def b11(self):
        K = self.e.toPlainText()
        if K =='숭덕고등학교' and self.now == 1:
            self.T1.setPlainText('숭')
            self.T2.setPlainText('덕')
            self.T3.setPlainText('고')
            self.T4.setPlainText('등')
            self.T5.setPlainText('학')
            self.T6.setPlainText('교')
        elif K == '등차수열' and self.now == 2:
            self.T4.setPlainText('등')
            self.T8.setPlainText('차')
            self.T10.setPlainText('수')
            self.T12.setPlainText('열')
        else:
            pass
            

    def b1(self):
        self.now = 1
        self.initDisplay()
        self.t.setPlainText('바보')

    def b2(self):
        self.now = 2
        self.initDisplay()
        self.t.setPlainText('설명')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainformClass()
    mainWindow.show()
    app.exec_()