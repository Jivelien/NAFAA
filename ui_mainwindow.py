# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.button = QPushButton(self.centralwidget)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(10, 560, 161, 61))
        self.pic_container = QLabel(self.centralwidget)
        self.pic_container.setObjectName(u"pic_container")
        self.pic_container.setGeometry(QRect(10, 50, 451, 501))
        self.program_list = QListView(self.centralwidget)
        self.program_list.setObjectName(u"program_list")
        self.program_list.setGeometry(QRect(10, 10, 441, 31))
        self.timer = QLCDNumber(self.centralwidget)
        self.timer.setObjectName(u"timer")
        self.timer.setGeometry(QRect(180, 560, 281, 61))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pic_container.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

