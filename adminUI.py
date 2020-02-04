# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Admin(object):
    def setupUi(self, Admin):
        Admin.setObjectName("Admin")
        Admin.resize(488, 574)
        Admin.setMinimumSize(QtCore.QSize(488, 482))
        Admin.setMaximumSize(QtCore.QSize(488, 1000))
        self.AdminLbl = QtWidgets.QLabel(Admin)
        self.AdminLbl.setGeometry(QtCore.QRect(50, 0, 431, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.AdminLbl.setFont(font)
        self.AdminLbl.setObjectName("AdminLbl")
        self.showtimeButton = QtWidgets.QPushButton(Admin)
        self.showtimeButton.setGeometry(QtCore.QRect(90, 190, 311, 81))
        self.showtimeButton.setObjectName("showtimeButton")
        self.movieButton = QtWidgets.QPushButton(Admin)
        self.movieButton.setGeometry(QtCore.QRect(90, 280, 311, 81))
        self.movieButton.setObjectName("movieButton")
        self.topupButton = QtWidgets.QPushButton(Admin)
        self.topupButton.setGeometry(QtCore.QRect(90, 370, 311, 81))
        self.topupButton.setObjectName("topupButton")
        self.regisButton = QtWidgets.QPushButton(Admin)
        self.regisButton.setGeometry(QtCore.QRect(90, 100, 311, 81))
        self.regisButton.setObjectName("regisButton")
        self.label = QtWidgets.QLabel(Admin)
        self.label.setGeometry(QtCore.QRect(0, 0, 491, 481))
        self.label.setText("")
        self.label.setObjectName("label")
        self.logoutButton = QtWidgets.QPushButton(Admin)
        self.logoutButton.setGeometry(QtCore.QRect(90, 460, 311, 81))
        self.logoutButton.setObjectName("logoutButton")
        self.label.raise_()
        self.AdminLbl.raise_()
        self.showtimeButton.raise_()
        self.movieButton.raise_()
        self.topupButton.raise_()
        self.regisButton.raise_()
        self.logoutButton.raise_()

        self.retranslateUi(Admin)
        QtCore.QMetaObject.connectSlotsByName(Admin)

    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "Form"))
        self.AdminLbl.setText(_translate("Admin", "ADMINISTRATION"))
        self.showtimeButton.setText(_translate("Admin", "SET SHOWTIME"))
        self.movieButton.setText(_translate("Admin", "SET NOW SHOWING"))
        self.topupButton.setText(_translate("Admin", "TOPUP USER"))
        self.regisButton.setText(_translate("Admin", "NEW CUSTOMER REGISTRATION"))
        self.logoutButton.setText(_translate("Admin", "LOGOUT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admin = QtWidgets.QWidget()
    ui = Ui_Admin()
    ui.setupUi(Admin)
    Admin.show()
    sys.exit(app.exec_())

