import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from difficulty import levelwindow
import titleimage_rc
from crawling import newsCrawling, wikiListCrawling, check_string, crawling
form_main = uic.loadUiType("test.ui")[0]

class MainWindow(QMainWindow,QWidget,form_main):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowIcon(QIcon('icon.png'))
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonClicked)
        self.pushButton_3.clicked.connect(self.buttonClicked3)

    def buttonClicked(self):
        self.hide()
        self.single = levelwindow()
        self.single.exec()
        self.show()

    def buttonClicked3(self):
        self.close()



if __name__ == "__main__":
    WikiList = []
    newsCrawling()
    wikiListCrawling()
    check_string()
    crawling()
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()