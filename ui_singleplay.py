# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'singleplaybpFpHe.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import singleplay


class Ui_singleplay(object):

    def setupUi(self, singleplay):
        if singleplay.objectName():
            singleplay.setObjectName(u"singleplay")
        singleplay.resize(500, 800)
        singleplay.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(singleplay)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 570, 130, 70))
        self.pushButton.setStyleSheet(u"font: 20pt \"1\ud6c8\ud654\uc591\uc5f0\ud654 R\";\n"
"color: rgb(237, 125, 49);")
        self.pushButton.setText(self.celeblist[self.startimgnum])
        self.imagelabel = QLabel(singleplay)
        self.imagelabel.setObjectName(u"imagelabel")
        self.imagelabel.setGeometry(QRect(50, 50, 400, 500))
        self.imagelabel.setStyleSheet(u"background-color: rgb(213, 213, 213);")
        self.pushButton_2 = QPushButton(singleplay)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(270, 570, 130, 70))
        self.pushButton_2.setStyleSheet(u"font: 20pt \"1\ud6c8\ud654\uc591\uc5f0\ud654 R\";\n"
"color: rgb(237, 125, 49);")
        self.pushButton_2.setText(self.celeblist[self.randomlist[0]])
        self.pushButton_3 = QPushButton(singleplay)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(90, 650, 130, 70))
        self.pushButton_3.setStyleSheet(u"font: 20pt \"1\ud6c8\ud654\uc591\uc5f0\ud654 R\";\n"
"color: rgb(237, 125, 49);")
        self.pushButton_3.setText(self.celeblist[self.randomlist[1]])
        self.pushButton_4 = QPushButton(singleplay)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(270, 650, 130, 70))
        self.pushButton_4.setStyleSheet(u"font: 20pt \"1\ud6c8\ud654\uc591\uc5f0\ud654 R\";\n"
"color: rgb(237, 125, 49);")
        self.pushButton_4.setText(self.celeblist[self.randomlist[2]])

        self.retranslateUi(singleplay)

        QMetaObject.connectSlotsByName(singleplay)
    # setupUi

    def retranslateUi(self, singleplay):
        singleplay.setWindowTitle(QCoreApplication.translate("singleplay", u"Single", None))
        self.imagelabel.setText("")
    # retranslateUi

