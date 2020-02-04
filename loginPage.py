# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginPage.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loginPage(object):
    def setupUi(self, loginPage):
        loginPage.setObjectName("loginPage")
        loginPage.resize(401, 723)
        loginPage.setMinimumSize(QtCore.QSize(401, 723))
        loginPage.setMaximumSize(QtCore.QSize(401, 723))
        self.userlbl = QtWidgets.QLabel(loginPage)
        self.userlbl.setGeometry(QtCore.QRect(90, 370, 47, 13))
        self.userlbl.setObjectName("userlbl")
        self.passlbl = QtWidgets.QLabel(loginPage)
        self.passlbl.setGeometry(QtCore.QRect(90, 400, 47, 13))
        self.passlbl.setObjectName("passlbl")
        self.background = QtWidgets.QLabel(loginPage)
        self.background.setGeometry(QtCore.QRect(0, 0, 401, 731))
        self.background.setText("")
        self.background.setObjectName("background")
        self.userInput = QtWidgets.QLineEdit(loginPage)
        self.userInput.setGeometry(QtCore.QRect(150, 370, 131, 20))
        self.userInput.setObjectName("userInput")
        self.passInput = QtWidgets.QLineEdit(loginPage)
        self.passInput.setGeometry(QtCore.QRect(150, 400, 131, 20))
        self.passInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passInput.setObjectName("passInput")
        self.appPicture = QtWidgets.QLabel(loginPage)
        self.appPicture.setGeometry(QtCore.QRect(20, 300, 374, 58))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.appPicture.setFont(font)
        self.appPicture.setObjectName("appPicture")
        self.loginButton = QtWidgets.QPushButton(loginPage)
        self.loginButton.setGeometry(QtCore.QRect(150, 430, 131, 23))
        self.loginButton.setObjectName("loginButton")
        self.background.raise_()
        self.userlbl.raise_()
        self.passlbl.raise_()
        self.userInput.raise_()
        self.passInput.raise_()
        self.appPicture.raise_()
        self.loginButton.raise_()


        self.retranslateUi(loginPage)
        QtCore.QMetaObject.connectSlotsByName(loginPage)

    def retranslateUi(self, loginPage):
        _translate = QtCore.QCoreApplication.translate
        loginPage.setWindowTitle(_translate("loginPage", "Form"))
        self.userlbl.setText(_translate("loginPage", "Username"))
        self.passlbl.setText(_translate("loginPage", "Password"))
        self.appPicture.setText(_translate("loginPage", "MINOR CINEPLEX"))
        self.loginButton.setText(_translate("loginPage", "Login"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginPage = QtWidgets.QWidget()
    ui = Ui_loginPage()
    ui.setupUi(loginPage)
    loginPage.show()
    sys.exit(app.exec_())

