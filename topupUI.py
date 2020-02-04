# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'topupUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_topup(object):
    def setupUi(self, topup):
        topup.setObjectName("topup")
        topup.resize(347, 408)
        self.label = QtWidgets.QLabel(topup)
        self.label.setGeometry(QtCore.QRect(0, 0, 351, 411))
        self.label.setMinimumSize(QtCore.QSize(351, 411))
        self.label.setMaximumSize(QtCore.QSize(351, 411))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Backg.png"))
        self.label.setObjectName("label")
        self.topupButtop = QtWidgets.QPushButton(topup)
        self.topupButtop.setGeometry(QtCore.QRect(130, 340, 75, 23))
        self.topupButtop.setObjectName("topupButtop")
        self.label_2 = QtWidgets.QLabel(topup)
        self.label_2.setGeometry(QtCore.QRect(130, 30, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.idInput = QtWidgets.QLineEdit(topup)
        self.idInput.setGeometry(QtCore.QRect(112, 110, 121, 20))
        self.idInput.setObjectName("idInput")
        self.lineEdit_2 = QtWidgets.QLineEdit(topup)
        self.lineEdit_2.setGeometry(QtCore.QRect(112, 170, 121, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(topup)
        self.label_3.setGeometry(QtCore.QRect(60, 110, 47, 13))
        self.label_3.setObjectName("label_3")
        self.amountInput = QtWidgets.QLabel(topup)
        self.amountInput.setGeometry(QtCore.QRect(60, 170, 47, 13))
        self.amountInput.setObjectName("amountInput")

        self.retranslateUi(topup)
        QtCore.QMetaObject.connectSlotsByName(topup)

    def retranslateUi(self, topup):
        _translate = QtCore.QCoreApplication.translate
        topup.setWindowTitle(_translate("topup", "Topup"))
        self.topupButtop.setText(_translate("topup", "PushButton"))
        self.label_2.setText(_translate("topup", "TOPUP"))
        self.label_3.setText(_translate("topup", "Account"))
        self.amountInput.setText(_translate("topup", "Money"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    topup = QtWidgets.QWidget()
    ui = Ui_topup()
    ui.setupUi(topup)
    topup.show()
    sys.exit(app.exec_())

