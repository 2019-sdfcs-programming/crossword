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
        self.B11.clicked.connect(self.b11)

    def b1(self):
        self.t.setPlainText('바보')
        def b11(self):
        E = self.e.toPlainText()

        if E =='숭덕고등학교':
            self.T1.setPlainText('숭')
            self.T2.setPlainText('덕')
            self.T3.setPlainText('고')
            self.T4.setPlainText('등')
            self.T5.setPlainText('학')
            self.T6.setPlainText('교')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainformClass()
    mainWindow.show()
    app.exec_()