# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movieSetPage.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_movieListPage(object):
    def setupUi(self, movieListPage):
        movieListPage.setObjectName("movieListPage")
        movieListPage.resize(512, 412)
        movieListPage.setMinimumSize(QtCore.QSize(512, 412))
        movieListPage.setMaximumSize(QtCore.QSize(512, 412))
        self.backGround = QtWidgets.QLabel(movieListPage)
        self.backGround.setGeometry(QtCore.QRect(0, 0, 521, 411))
        self.backGround.setText("")
        self.backGround.setPixmap(QtGui.QPixmap("Backg.png"))
        self.backGround.setObjectName("backGround")
        self.saveButton = QtWidgets.QPushButton(movieListPage)
        self.saveButton.setGeometry(QtCore.QRect(210, 340, 81, 23))
        self.saveButton.setObjectName("saveButton")
        self.mname1 = QtWidgets.QLineEdit(movieListPage)
        self.mname1.setGeometry(QtCore.QRect(90, 140, 141, 20))
        self.mname1.setObjectName("mname1")
        self.mname2 = QtWidgets.QLineEdit(movieListPage)
        self.mname2.setGeometry(QtCore.QRect(90, 180, 141, 20))
        self.mname2.setObjectName("mname2")
        self.mname3 = QtWidgets.QLineEdit(movieListPage)
        self.mname3.setGeometry(QtCore.QRect(90, 220, 141, 20))
        self.mname3.setObjectName("mname3")
        self.mname4 = QtWidgets.QLineEdit(movieListPage)
        self.mname4.setGeometry(QtCore.QRect(90, 260, 141, 20))
        self.mname4.setObjectName("mname4")
        self.mname5 = QtWidgets.QLineEdit(movieListPage)
        self.mname5.setGeometry(QtCore.QRect(90, 300, 141, 20))
        self.mname5.setObjectName("mname5")
        self.photo1 = QtWidgets.QLineEdit(movieListPage)
        self.photo1.setGeometry(QtCore.QRect(310, 140, 141, 20))
        self.photo1.setObjectName("photo1")
        self.photo2 = QtWidgets.QLineEdit(movieListPage)
        self.photo2.setGeometry(QtCore.QRect(310, 180, 141, 20))
        self.photo2.setObjectName("photo2")
        self.photo3 = QtWidgets.QLineEdit(movieListPage)
        self.photo3.setGeometry(QtCore.QRect(310, 220, 141, 20))
        self.photo3.setObjectName("photo3")
        self.photo4 = QtWidgets.QLineEdit(movieListPage)
        self.photo4.setGeometry(QtCore.QRect(310, 260, 141, 20))
        self.photo4.setObjectName("photo4")
        self.photo5 = QtWidgets.QLineEdit(movieListPage)
        self.photo5.setGeometry(QtCore.QRect(310, 300, 141, 20))
        self.photo5.setObjectName("photo5")
        self.label = QtWidgets.QLabel(movieListPage)
        self.label.setGeometry(QtCore.QRect(130, 50, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(22)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(movieListPage)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 71, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(movieListPage)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 71, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(movieListPage)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 71, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(movieListPage)
        self.label_5.setGeometry(QtCore.QRect(10, 260, 71, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(movieListPage)
        self.label_6.setGeometry(QtCore.QRect(10, 300, 71, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(movieListPage)
        self.label_7.setGeometry(QtCore.QRect(250, 140, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(movieListPage)
        self.label_8.setGeometry(QtCore.QRect(250, 180, 47, 13))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(movieListPage)
        self.label_9.setGeometry(QtCore.QRect(250, 220, 47, 13))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(movieListPage)
        self.label_10.setGeometry(QtCore.QRect(250, 260, 47, 13))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(movieListPage)
        self.label_11.setGeometry(QtCore.QRect(250, 300, 47, 13))
        self.label_11.setObjectName("label_11")

        self.retranslateUi(movieListPage)
        QtCore.QMetaObject.connectSlotsByName(movieListPage)

    def retranslateUi(self, movieListPage):
        _translate = QtCore.QCoreApplication.translate
        movieListPage.setWindowTitle(_translate("movieListPage", "ListSetting"))
        self.saveButton.setText(_translate("movieListPage", "Save"))
        self.label.setText(_translate("movieListPage", "Movie List Settings"))
        self.label_2.setText(_translate("movieListPage", "Movie Name 1"))
        self.label_3.setText(_translate("movieListPage", "Movie Name 2"))
        self.label_4.setText(_translate("movieListPage", "Movie Name 3"))
        self.label_5.setText(_translate("movieListPage", "Movie Name 4"))
        self.label_6.setText(_translate("movieListPage", "Movie Name 5"))
        self.label_7.setText(_translate("movieListPage", "Photo File"))
        self.label_8.setText(_translate("movieListPage", "Photo File"))
        self.label_9.setText(_translate("movieListPage", "Photo File"))
        self.label_10.setText(_translate("movieListPage", "Photo File"))
        self.label_11.setText(_translate("movieListPage", "Photo File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    movieListPage = QtWidgets.QWidget()
    ui = Ui_movieListPage()
    ui.setupUi(movieListPage)
    movieListPage.show()
    sys.exit(app.exec_())

