# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cinemaEditSelection.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CinemaEdit(object):
    def setupUi(self, CinemaEdit):
        CinemaEdit.setObjectName("CinemaEdit")
        CinemaEdit.resize(413, 458)
        CinemaEdit.setMinimumSize(QtCore.QSize(413, 458))
        CinemaEdit.setMaximumSize(QtCore.QSize(413, 458))
        self.twodthai = QtWidgets.QPushButton(CinemaEdit)
        self.twodthai.setGeometry(QtCore.QRect(20, 90, 371, 51))
        self.twodthai.setObjectName("twodthai")
        self.twodst = QtWidgets.QPushButton(CinemaEdit)
        self.twodst.setGeometry(QtCore.QRect(20, 150, 371, 51))
        self.twodst.setObjectName("twodst")
        self.threedthai = QtWidgets.QPushButton(CinemaEdit)
        self.threedthai.setGeometry(QtCore.QRect(20, 210, 371, 51))
        self.threedthai.setObjectName("threedthai")
        self.threedst = QtWidgets.QPushButton(CinemaEdit)
        self.threedst.setGeometry(QtCore.QRect(20, 270, 371, 51))
        self.threedst.setObjectName("threedst")
        self.imaxthai = QtWidgets.QPushButton(CinemaEdit)
        self.imaxthai.setGeometry(QtCore.QRect(20, 330, 371, 51))
        self.imaxthai.setObjectName("imaxthai")
        self.imaxst = QtWidgets.QPushButton(CinemaEdit)
        self.imaxst.setGeometry(QtCore.QRect(20, 390, 371, 51))
        self.imaxst.setObjectName("imaxst")
        self.label = QtWidgets.QLabel(CinemaEdit)
        self.label.setGeometry(QtCore.QRect(110, 30, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(CinemaEdit)
        QtCore.QMetaObject.connectSlotsByName(CinemaEdit)

    def retranslateUi(self, CinemaEdit):
        _translate = QtCore.QCoreApplication.translate
        CinemaEdit.setWindowTitle(_translate("CinemaEdit", "CinemaEditSelect"))
        self.twodthai.setText(_translate("CinemaEdit", "2D Thai"))
        self.twodst.setText(_translate("CinemaEdit", "2D Soundtrack"))
        self.threedthai.setText(_translate("CinemaEdit", "3D Thai"))
        self.threedst.setText(_translate("CinemaEdit", "3D Soundtrack"))
        self.imaxthai.setText(_translate("CinemaEdit", "IMAX Thai"))
        self.imaxst.setText(_translate("CinemaEdit", "IMAX Soundtrack"))
        self.label.setText(_translate("CinemaEdit", "SELECT CINEMA TO EDIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CinemaEdit = QtWidgets.QWidget()
    ui = Ui_CinemaEdit()
    ui.setupUi(CinemaEdit)
    CinemaEdit.show()
    sys.exit(app.exec_())

