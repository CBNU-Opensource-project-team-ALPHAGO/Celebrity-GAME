import random
import sys
from PyQt5.QtWidgets import*
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import random
from fail import failWindow
from clear import clearWindow
import gameplay_rc

form_singleplay = uic.loadUiType('singleplay.ui')[0]

class sptitle(QDialog,QWidget,form_singleplay):

    def __init__(self,level,player):
        super(sptitle,self).__init__()
        self.level = level
        self.playernum = player
        self.dataList = os.listdir('MainData')
        self.datalenth = len(self.dataList)
        self.startimgnum = 0
        self.randomnum = 0
        self.btn_random = 0
        self.maximg = 0
        self.clearnum = 0

        f = open('finalList.txt', 'r', encoding='UTF-8')
        data = f.read().splitlines()
        self.celeblist = data
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.pushButton.clicked.connect(self.answerButton)
        self.pushButton_2.clicked.connect(self.answerButton_2)
        self.pushButton_3.clicked.connect(self.answerButton_3)
        self.pushButton_4.clicked.connect(self.answerButton_4)
        self.loadimage()


    def selectbtn(self):
        self.randomnum = random.randrange(0,4)
        self.randomlist = list(range(0,self.datalenth))
        self.randomlist.pop(self.startimgnum)
        self.randomlist.pop(0)
        random.shuffle(self.randomlist)

        print(self.randomlist)

        if self.randomnum == 0:
            self.pushButton.setText(self.celeblist[self.startimgnum])
            self.pushButton_2.setText(self.celeblist[self.randomlist[0]])
            self.pushButton_3.setText(self.celeblist[self.randomlist[1]])
            self.pushButton_4.setText(self.celeblist[self.randomlist[2]])

        elif self.randomnum == 1:
            self.pushButton.setText(self.celeblist[self.randomlist[0]])
            self.pushButton_2.setText(self.celeblist[self.startimgnum])
            self.pushButton_3.setText(self.celeblist[self.randomlist[1]])
            self.pushButton_4.setText(self.celeblist[self.randomlist[2]])

        elif self.randomnum == 2:
            self.pushButton.setText(self.celeblist[self.randomlist[1]])
            self.pushButton_2.setText(self.celeblist[self.randomlist[0]])
            self.pushButton_3.setText(self.celeblist[self.startimgnum])
            self.pushButton_4.setText(self.celeblist[self.randomlist[2]])

        elif self.randomnum == 3:
            self.pushButton.setText(self.celeblist[self.randomlist[0]])
            self.pushButton_2.setText(self.celeblist[self.randomlist[1]])
            self.pushButton_3.setText(self.celeblist[self.randomlist[2]])
            self.pushButton_4.setText(self.celeblist[self.startimgnum])

    def answerButton(self):
        if self.startimgnum == 0:
            self.startimgnum += 1
            self.selectbtn()
            self.timer.stop()
            self.loadimage()
        elif self.pushButton.text() == self.celeblist[self.startimgnum]:
            self.startimgnum += 1
            self.clearnum += 1
            self.selectbtn()
            self.timer.stop()
            self.loadimage()
        else:
            self.failmenu()

    def answerButton_2(self):
        if self.startimgnum == 0:
            self.startimgnum += 1
            self.selectbtn()
            self.timer.stop()
            self.loadimage()
        elif self.pushButton_2.text() == self.celeblist[self.startimgnum]:
            self.startimgnum += 1
            self.clearnum += 1
            self.selectbtn()
            self.timer.stop()
            self.loadimage()
        else:
            self.failmenu()

    def answerButton_3(self):
        if self.startimgnum == 0:
            self.startimgnum += 1
            self.selectbtn()
            self.timer.stop()
            self.loadimage()
        elif self.pushButton_3.text() == self.celeblist[self.startimgnum]:
            self.startimgnum += 1
            self.clearnum += 1
            self.selectbtn()
            self.timer.stop()
            self.loadimage()
        else:
            self.failmenu()

    def answerButton_4(self):
        if self.startimgnum == 0:
            self.startimgnum += 1
            self.selectbtn()
            self.timer.stop()
            self.loadimage()
        elif self.pushButton_4.text() == self.celeblist[self.startimgnum]:
            self.startimgnum += 1
            self.clearnum += 1
            self.timer.stop()
            self.selectbtn()
            self.loadimage()
        else:
            self.failmenu()

    def loadimage(self):

        if self.playernum == 1:
            self.maximg = 5
        else:
            self.maximg = self.playernum * 2 - 1

        self.imgNum = self.startimgnum

        ## 이미지 출력
        self.imagefile = QPixmap()
        self.imagefile.load("MainData/"+str(self.imgNum)+".jpg")
        self.imagelabel.setPixmap(self.imagefile)
        self.setLevel()
        self.clearcheck()



    def setLevel(self):
        if self.level == 1:
            self.leveltime = 6000

        if self.level == 2:
            self.leveltime = 4000

        if self.level == 3:
            self.leveltime = 2000

        self.timer = QTimer()
        self.timer.start(self.leveltime)
        self.timer.timeout.connect(self.failmenu)



    def failmenu(self):
        self.timer.stop()
        self.close()
        self.fail = failWindow()
        self.fail.exec()
        self.show()
        self.close()

    def clearmenu(self):
        self.timer.stop()
        self.close()
        self.clear = clearWindow()
        self.clear.exec()
        self.show()
        self.close()

    def clearcheck(self):

        if self.clearnum == self.maximg:
            self.clearmenu()