from PyQt5.QtWidgets import *
from PyQt5 import uic
import fail_rc


form_fail = uic.loadUiType("fail.ui")[0]

class failWindow(QDialog,QWidget,form_fail):
    def __init__(self):
        super(failWindow,self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.HomeButton.clicked.connect(self.Home)


    def Home(self):
        self.close()