# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_userUI(object):
    def setupUi(self, userUI, user, movieList):
        userUI.setObjectName("userUI")
        userUI.resize(971, 462)
        userUI.setMaximumSize(971, 462)
        userUI.setMinimumSize(971, 462)
        self.greeting = QtWidgets.QLabel(userUI)
        self.greeting.setGeometry(QtCore.QRect(20, 15, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.greeting.setFont(font)
        self.greeting.setObjectName("greeting")
        self.cash = QtWidgets.QLabel(userUI)
        self.cash.setGeometry(QtCore.QRect(20, 60, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cash.setFont(font)
        self.cash.setObjectName("cash")
        self.rank = QtWidgets.QLabel(userUI)
        self.rank.setGeometry(QtCore.QRect(20, 100, 131, 31))
        self.rank.setText("")
        self.rank.setObjectName("rank")
        self.label = QtWidgets.QLabel(userUI)
        self.label.setGeometry(QtCore.QRect(0, 0, 971, 651))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("userBG.jpg"))
        self.label.setObjectName("label")
        self.ticketButton = QtWidgets.QPushButton(userUI)
        self.ticketButton.setGeometry(QtCore.QRect(830, 10, 131, 41))
        self.ticketButton.setObjectName("ticketButton")
        self.quitButton = QtWidgets.QPushButton(userUI)
        self.quitButton.setGeometry(QtCore.QRect(830, 60, 131, 41))
        self.quitButton.setObjectName("quitButton")
        self.label.raise_()
        self.greeting.raise_()
        self.cash.raise_()
        self.rank.raise_()
        self.ticketButton.raise_()
        self.quitButton.raise_()

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

        self.movie1Button.raise_()
        self.movie2Button.raise_()
        self.movie3Button.raise_()
        self.movie4Button.raise_()
        self.movie5Button.raise_()

        self.retranslateUi(userUI,user)
        QtCore.QMetaObject.connectSlotsByName(userUI)

    def retranslateUi(self, userUI, user):
        _translate = QtCore.QCoreApplication.translate
        userUI.setWindowTitle(_translate("userUI", "Minor Cineprex"))
        self.greeting.setText(_translate("userUI", "Hello, "+user.firstname + user.lastname))
        self.cash.setText(_translate("userUI", "Your Cash: "+ str(user.cash) + "฿"))
        self.ticketButton.setText(_translate("userUI", "TICKET"))
        self.quitButton.setText(_translate("userUI", "QUIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    userUI = QtWidgets.QWidget()
    ui = Ui_userUI()
    ui.setupUi(userUI)
    userUI.show()
    sys.exit(app.exec_())

