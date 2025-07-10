# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mock User InterfaceGHTVbH.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 241, 51))
        font = QFont()
        font.setFamily(u"Cooper Black")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(30, 80, 731, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QRect(30, 110, 350, 180))
        self.Title = QLabel(self.groupBox)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(130, 150, 71, 16))
        font1 = QFont()
        font1.setFamily(u"Cooper Black")
        font1.setPointSize(10)
        self.Title.setFont(font1)
        self.Title.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 120, 113, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Power Pedal", None))
        self.groupBox.setTitle("")
        self.Title.setText(QCoreApplication.translate("MainWindow", u"WEATHER", None))
    # retranslateUi

