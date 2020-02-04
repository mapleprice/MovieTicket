# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_userUI(object):
    def setupUi(self, userUI,user,movieList):
        userUI.setObjectName("userUI")
        userUI.resize(971, 462)
        userUI.setMaximumSize(971,462)
        userUI.setMinimumSize(971,462)
        self.logoutbutton = QtWidgets.QPushButton(userUI)
        self.logoutbutton.setGeometry(QtCore.QRect(700,62,100,41))
        self.background = QtWidgets.QLabel(userUI)
        self.background.setGeometry(QtCore.QRect(0,0,972,463))
        self.label = QtWidgets.QLabel(userUI)
        self.label.setGeometry(QtCore.QRect(20, 15, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(userUI)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 371, 41))
        self.quitButton = QtWidgets.QPushButton(userUI)
        self.quitButton.setGeometry(QtCore.QRect(830, 60, 131, 41))
        self.quitButton.setObjectName("quitButton")
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(userUI)
        self.label_3.setGeometry(QtCore.QRect(380, 140, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setKerning(True)
        if len(movieList) >= 1:
            self.movie1Button = QtWidgets.QPushButton(userUI)
            self.movie1Button.setGeometry(QtCore.QRect(20, 210, 171, 231))
            self.movie1Button.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(movieList[0].photo), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.movie1Button.setIcon(icon)
            self.movie1Button.setIconSize(QtCore.QSize(167, 229))
            self.movie1Button.setObjectName("movie1Button")
        if len(movieList) >= 2:
            self.movie2Button = QtWidgets.QPushButton(userUI)
            self.movie2Button.setGeometry(QtCore.QRect(210, 210, 171, 231))
            self.movie2Button.setText("")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(movieList[1].photo), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.movie2Button.setIcon(icon1)
            self.movie2Button.setIconSize(QtCore.QSize(167, 229))
            self.movie2Button.setObjectName("movie2Button")
        if len(movieList) >= 3:
            self.movie3Button = QtWidgets.QPushButton(userUI)
            self.movie3Button.setGeometry(QtCore.QRect(400, 210, 171, 231))
            self.movie3Button.setText("")
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap(movieList[2].photo), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.movie3Button.setIcon(icon2)
            self.movie3Button.setIconSize(QtCore.QSize(167, 229))
            self.movie3Button.setObjectName("movie3Button")
        if len(movieList) >= 4:
            self.movie4Button = QtWidgets.QPushButton(userUI)
            self.movie4Button.setGeometry(QtCore.QRect(590, 210, 171, 231))
            self.movie4Button.setText("")
            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap(movieList[3].photo), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.movie4Button.setIcon(icon3)
            self.movie4Button.setIconSize(QtCore.QSize(167, 229))
            self.movie4Button.setObjectName("movie4Button")
        if len(movieList) >= 5:
            self.movie5Button = QtWidgets.QPushButton(userUI)
            self.movie5Button.setGeometry(QtCore.QRect(780, 210, 171, 231))
            self.movie5Button.setText("")
            icon4 = QtGui.QIcon()
            icon4.addPixmap(QtGui.QPixmap(movieList[4].photo), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.movie5Button.setIcon(icon4)
            self.movie5Button.setIconSize(QtCore.QSize(167, 229))
            self.movie5Button.setObjectName("movie5Button")

        self.retranslateUi(userUI,user)
        QtCore.QMetaObject.connectSlotsByName(userUI)

    def retranslateUi(self, userUI,user):
        _translate = QtCore.QCoreApplication.translate
        userUI.setWindowTitle(_translate("userUI", "Form"))
        self.label.setText(_translate("userUI", "Hello, " + user.firstname + ' ' + user.lastname + '!'))
        self.label_2.setText(_translate("userUI", "Your Cash: " + str(user.cash) + '฿'))
        self.label_3.setText(_translate("userUI", "NOW SHOWING"))
        self.quitButton.setText(_translate("userUI", "QUIT"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    userUI = QtWidgets.QWidget()
    ui = Ui_userUI()
    ui.setupUi(userUI)
    userUI.show()
    sys.exit(app.exec_())

