import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from singleplay import sptitle
import difficulty_rc

form_difficulty = uic.loadUiType('difficulty.ui')[0]



class levelwindow(QDialog,QWidget,form_difficulty):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.startButton.clicked.connect(self.startbutton)
        self.levelbutton1.clicked.connect(self.levelset)
        self.levelbutton2.clicked.connect(self.levelset)
        self.levelbutton3.clicked.connect(self.levelset)
        self.playerbutton1.clicked.connect(self.playerset)
        self.playerbutton2.clicked.connect(self.playerset)
        self.playerbutton3.clicked.connect(self.playerset)

    def startbutton(self):
        self.hide()
        self.single = sptitle(self.level,self.playernum)
        self.single.exec()
        self.show()
        self.close()

    def levelset(self):
        if self.levelbutton1.isChecked():
            self.level = 1
        elif self.levelbutton2.isChecked():
            self.level = 2
        elif self.levelbutton3.isChecked():
            self.level = 3
    def playerset(self):
        if self.playerbutton1.isChecked():
            self.playernum = 1
        elif self.playerbutton2.isChecked():
            self.playernum = 3
        elif self.playerbutton3.isChecked():
            self.playernum = 5
