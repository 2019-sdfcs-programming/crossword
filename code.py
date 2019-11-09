#-*- coding:utf-8 -*-

import sys
#PyQt must be installed.

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic

formClass = uic.loadUiType('PYQT.ui')[0]

state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

class MainformClass(QMainWindow, formClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.B1.clicked.connect(self.b1)
        self.B2.clicked.connect(self.b2)
        self.B3.clicked.connect(self.b3)
        self.B4.clicked.connect(self.b4)
        self.B5.clicked.connect(self.b5)
        self.B6.clicked.connect(self.b6)
        self.B7.clicked.connect(self.b7)
        self.B8.clicked.connect(self.b8)
        self.B9.clicked.connect(self.b9)
        self.B10.clicked.connect(self.b10)
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
            self.label_14.setText('정답')
            self.B1.hide()
            state[0] = 1

        elif K == '등차수열' and self.now == 2:
            self.T4.setPlainText('등')
            self.T8.setPlainText('차')
            self.T10.setPlainText('수')
            self.T12.setPlainText('열')
            self.label_14.setText('정답')
            self.B2.hide()
            state[1] = 1
        elif K == '열역학제2법칙' and self.now ==3:
            self.T12.setPlainText('열')
            self.T13.setPlainText('역')
            self.T14.setPlainText('학')
            self.T15.setPlainText('제')
            self.T16.setPlainText('2')
            self.T17.setPlainText('법')
            self.T18.setPlainText('칙')
            self.label_14.setText('정답')
            self.B3.hide()
            state[2] = 1
        elif K == '학술제' and self.now ==4:
            self.T14.setPlainText('학')
            self.T19.setPlainText('술')
            self.T25.setPlainText('제')
            self.label_14.setText('정답')
            self.B4.hide()
            state[3] = 1
        elif K == '고교학점제' and self.now ==5:
            self.T21.setPlainText('고')
            self.T22.setPlainText('교')
            self.T23.setPlainText('학')
            self.T24.setPlainText('점')
            self.T25.setPlainText('제')
            self.label_14.setText('정답')
            self.B5.hide()
            state[4] = 1
        elif K == '점근선' and self.now ==6:
            self.T24.setPlainText('점')
            self.T27.setPlainText('근')
            self.T29.setPlainText('선')
            self.label_14.setText('정답')
            self.B6.hide()
            state[5] = 1
        elif K == '선행사' and self.now ==7:
            self.T29.setPlainText('선')
            self.T30.setPlainText('행')
            self.T31.setPlainText('사')
            self.label_14.setText('정답')
            self.B7.hide()
            state[6] = 1
        elif K == '법무부장관' and self.now ==8:
            self.T17.setPlainText('법')
            self.T20.setPlainText('무')
            self.T26.setPlainText('부')
            self.T28.setPlainText('장')
            self.T32.setPlainText('관')
            self.label_14.setText('정답')
            self.B8.hide()
            state[7] = 1
        elif K == '관형사' and self.now ==9:
            self.T32.setPlainText('관')
            self.T33.setPlainText('형')
            self.T34.setPlainText('사')
            self.label_14.setText('정답')
            self.B9.hide()
            state[8] = 1
        elif K == '훈트규칙' and self.now ==10:
            self.T7.setPlainText('훈')
            self.T9.setPlainText('트')
            self.T11.setPlainText('규')
            self.T18.setPlainText('칙')
            self.label_14.setText('정답')
            self.B10.hide()
            state[9] = 1
        else:
            self.label_14.setText('땡')

        if 0 not in state:
            msg = QMessageBox()
            font = QFont()
            font.setPointSize(24)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Clear!')
            msg.setText('축하합니다 \n모든 문제를 맞추셨습니다')
            msg.setFont(font)
            msg.exec_()

    def b1(self):
        self.now = 1
        self.initDisplay()
        self.t.setPlainText('명문 中 명문 \n우리가 재학중인 \n바로 이곳은?')

    def b2(self):
        self.now = 2
        self.initDisplay()
        self.t.setPlainText('이웃하는 항들의 차가 \n일정한 수열\n\n이 일정한 차를 공차라고한다\n\n영어로 A.P.\n(Arithmetic Progression)\n라고도 하는 이 수열은?')

    def b3(self):
        self.now = 3
        self.initDisplay()
        self.t.setPlainText('자발적으로 일어나는 비가역 \n현상에는 방향성이 있다, \n\n열은 항상 고온에서 저온으로 \n이동한다,\n\n고립계에서 자발적으로 \n일어나는 자연현상은 \n항상 확률이 높은 방향으로 \n진행된다\n\n를 의미하는 물리 법칙은?')
    
    def b4(self):
        self.now = 4
        self.initDisplay()
        self.t.setPlainText('EBL, SD FORUM,\nReading Books Festival \n등으로 구성된 \n숭덕고 학생들의 축제는?')
    
    def b5(self):
        self.now = 5
        self.initDisplay()
        self.t.setPlainText('고등학교 학생들이 진로에 따라 \n다양한 과목을 선택 · 이수하고 \n누적학점이 기준에 도달할 경우 \n졸업을 인정받는 제도는?')

    def b6(self):
        self.now = 6
        self.initDisplay()
        self.t.setPlainText('무한히 뻗어나가는 곡선이 \n한없이 가까워지는 직선\n\n우리가 배운 것 중에는\n유리함수, 지수함수, \n로그함수, 쌍곡선\n등에서 볼 수 있다')

    def b7(self):
        self.now = 7
        self.initDisplay()
        self.t.setPlainText('영어에서 관계사 앞에오는 말 \n관계대명사 중 what은 \n이것을 가지지 않는다')

    def b8(self):
        self.now = 8
        self.initDisplay()
        self.t.setPlainText('9월 9일 조국이 임명된 직책 \n검찰과 치열한 공방을 펼치다\n43일만에 사퇴했다')

    def b9(self):
        self.now = 9
        self.initDisplay()
        self.t.setPlainText('우리 말 9품사 중의 하나\n체언을 수식하는 역할을 한다.')

    def b10(self):
        self.now = 10
        self.initDisplay()
        self.t.setPlainText('에너지 준위가 같은 오비탈에\n전자가 배치될 때\n홀전자 수가 가장 큰 배치를\n한다는 규칙')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainformClass()
    mainWindow.show()
    app.exec_()