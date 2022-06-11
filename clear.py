import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import Clear_rc


form_clear = uic.loadUiType("clear.ui")[0]

class clearWindow(QDialog,QWidget,form_clear):
    def __init__(self):
        super(clearWindow,self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.HomeButton.clicked.connect(self.Home)


    def Home(self):
        self.close()