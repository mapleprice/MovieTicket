# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cinemaSelect.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cinemaSelect(object):
    def setupUi(self, cinemaSelect,movie,selectedMovie):
        cinemaSelect.setObjectName("cinemaSelect")
        cinemaSelect.resize(538, 609)
        cinemaSelect.setMaximumSize(QtCore.QSize(538, 609))
        self.label = QtWidgets.QLabel(cinemaSelect)
        self.label.setGeometry(QtCore.QRect(150, 40, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(cinemaSelect)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(cinemaSelect)
        self.label_3.setGeometry(QtCore.QRect(40, 445, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(cinemaSelect)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 71, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(cinemaSelect)
        self.label_5.setGeometry(QtCore.QRect(30, 210, 71, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(cinemaSelect)
        self.label_6.setGeometry(QtCore.QRect(30, 250, 71, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(cinemaSelect)
        self.label_7.setGeometry(QtCore.QRect(30, 290, 71, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(cinemaSelect)
        self.label_8.setGeometry(QtCore.QRect(30, 330, 81, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(cinemaSelect)
        self.label_9.setGeometry(QtCore.QRect(170, 440, 341, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_9.setFont(font)
        self.label_9.setText(selectedMovie.name)
        self.label_9.setObjectName("label_9")
        self.background = QtWidgets.QLabel(cinemaSelect)
        self.background.setGeometry(QtCore.QRect(0, 0, 541, 611))
        self.background.setText(movie.name)
        self.background.setPixmap(QtGui.QPixmap("Backg.png"))
        self.background.setObjectName("background")
        self.background.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()

        self.retranslateUi(cinemaSelect)
        QtCore.QMetaObject.connectSlotsByName(cinemaSelect)

    def retranslateUi(self, cinemaSelect, ):
        _translate = QtCore.QCoreApplication.translate
        cinemaSelect.setWindowTitle(_translate("cinemaSelect", "Cinema Selection"))
        self.label.setText(_translate("cinemaSelect", "Cinema Selection"))
        self.label_2.setText(_translate("cinemaSelect", "2D Thai"))
        self.label_3.setText(_translate("cinemaSelect", "Selected Movie :"))
        self.label_4.setText(_translate("cinemaSelect", "2D Soundtrack"))
        self.label_5.setText(_translate("cinemaSelect", "3D Thai"))
        self.label_6.setText(_translate("cinemaSelect", "3D Soundtrack"))
        self.label_7.setText(_translate("cinemaSelect", "IMAX Thai"))
        self.label_8.setText(_translate("cinemaSelect", "IMAX Soundtrack"))

