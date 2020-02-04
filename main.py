from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtGui import QPixmap,QIcon
import abc
import pickle
from functools import partial

#USER CLASSES
class Date:
    def __init__(self,day,month,year):
        self.day = int(day)
        self.year = int(year)
        self.month = month

class User(metaclass = abc.ABCMeta):

    def __init__(self,firstname ,lastname,age,dateofBirth,address,username,password):
        self.username = str(username)
        self.password = str(password)
        self.firstname = str(firstname)
        self.lastname = str(lastname)
        self.age = int(age)
        self.dob = Date
        self.address = str(address)
        self.ownedSeat = []
        self.cash = 0

    def topup(self,money):
        self.cash +=  money

    def pay(self,money):
        if self.cash - money < 0:
            return 0
        else:
            self.cash -= money
            return 1


class Admin(User):
    def __init__(self,firstname ,lastname,age,dateofBirth,address,username,password):
        super().__init__(firstname ,lastname,age,dateofBirth,address,username,password)

class Guest(User):
    def __init__(self,firstname ,lastname,age,dateofBirth,address,username,password):
        super().__init__(firstname ,lastname,age,dateofBirth,address,username,password)

class DefaultUser(User):
    def __init__(self,firstname ,lastname,age,dateofBirth,address,username,password):
        super().__init__(firstname ,lastname,age,dateofBirth,address,username,password)
        self.discount = 20

class StudentUser(User):
    def __init__(self,firstname ,lastname,age,dateofBirth,address,username,password):
        super().__init__(firstname ,lastname,age,dateofBirth,address,username,password)
        self.discount = 50

#THEATRE CLASSES

class Round:
    def __init__(self,time,movie,imax = 0):
        if imax == 0:
            self.rows = 11
            self.column = 20
            self.hrows = 3
        else :
            self.rows = 18
            self.column = 36
            self.hrows = 6
        self.time = time
        self.movie = movie
        self.seat = []
        for i in range(self.rows):
            self.seatLine = []
            for j in range(self.column):
                if i < self.rows - self.hrows:
                    self.seatLine.append(Seat(i , j, False))
                else:
                    self.seatLine.append(Seat(i , j, True))
            self.seat.append(seatLine)


class Movie:
    def __init__(self,name,photo):
        self.name = name
        self.photo = photo

class Ticket:
    def __init__(self,time,seat,movie):
        self.time = time
        self.seat = seat
        self.movie = movie

class Seat:
    def __init__(self, row, column, honeymoon):
        self.row = row
        self.column = column
        self.honeymoon = honeymoon
        self.owned = False

class Cinema(metaclass = abc.ABCMeta):
    def __init__(self,normalcost,honeymooncost,rows,columns):
        self.currentMovie = str()
        self.normalcost = normalcost
        self.honeymooncost = honeymooncost
        self.rows = rows
        self.columns = columns
        self.rounds = []

class TwoDCinema(Cinema):
    def __init__(self):
        super().__init__(140, 170 , 11, 20)

class ThreeDCinema(Cinema):
    def __init__(self):
        super().__init__(170, 200 , 11, 20)

class IMAXCinema(Cinema):
    def __init__(self):
        super().__init__( 360, 440 , 18, 36)

#GUICLASS
from loginPage import  Ui_loginPage
from registrationForm import Ui_RegistratioForm
from userUI import Ui_userUI
from adminUI import Ui_Admin
from cinemaSelect import Ui_cinemaSelect
from movieSetPage import Ui_movieListPage

class MainApp(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)

        #Load Files
        userFile = open("users.bin", "rb")
        self.userList = pickle.load(userFile)
        userFile.close()
        movieListfile = open("movieList.bin","rb")
        self.movieList = pickle.load(movieListfile)
        movieListfile.close()
        cinemaFile = open("cinemas.bin","rb")
        self.cinemas = pickle.load(cinemaFile)
        cinemaFile.close()

        #Creating Ui Objects
        self.loginPage = Ui_loginPage()
        self.registrationPage =  Ui_RegistratioForm()
        self.userInterface = Ui_userUI()
        self.adminInterface = Ui_Admin()
        self.cinemaSelectionUi = Ui_cinemaSelect()
        self.movieSettingInterface = Ui_movieListPage()

        #Creating Windows
        self.regisWindow = QtWidgets.QMainWindow()
        self.userWindow = QtWidgets.QMainWindow()
        self.adminWindow = QtWidgets.QMainWindow()
        self.normalSelectWindow = QtWidgets.QMainWindow()
        self.imaxSelectionWindow = QtWidgets.QMainWindow()

        self.startLoginPage()

    def startLoginPage(self):
        print("LoginPage")
        self.loginPage.setupUi(self)
        self.loginPage.loginButton.clicked.connect(self.login)
        self.loginPage.background.setPixmap(QPixmap('Back.jpg'))
        self.show()

    def startRegPage(self):
        print("Regpage")
        self.registrationPage.setupUi(self.regisWindow)
        self.registrationPage.pushButton.clicked.connect(self.newUserRegister)
        self.regisWindow.show()

    def newUserRegister(self):
        firstname = self.registrationPage.nameIn.text()
        lastname = self.registrationPage.lastIn.text()
        username = self.registrationPage.userIn.text()
        password = self.registrationPage.passwordInput.text()
        conPass = self.registrationPage.passwordConInput.text()
        address = self.registrationPage.addressInput.toPlainText() + " " + self.registrationPage.zipIn.text()
        day,month,year = self.registrationPage.dateofbirthin.text().split("-")
        dateofbirth = Date(day,month,year)
        for aUser in self.userList:
            if username == aUser.username:
                self.idAlreadyExist()
                return
        age = 2018 - int(year)
        if conPass == password:
            if age <= 22:
                self.userList.append(StudentUser(firstname,lastname,age,dateofbirth,address,username,password))
            else:
                self.userList.append(DefaultUser(firstname, lastname, age, dateofbirth, address, username, password))
            self.messageBox("Register Successful","Registration Completed",1)
            self.saveAll()
            self.regisWindow.close()
        else:
            self.messageBox("Password not matched","Password and Confirm Password aren't matched",2)

    def login(self):
        id = self.loginPage.userInput.text()
        pw = self.loginPage.passInput.text()
        try:
            for aUser in self.userList:
                if id == aUser.username:
                    self.currentUser = aUser
                    break

            if pw == self.currentUser.password:
                self.loggedIn()
                if type(self.currentUser) == Admin:
                    self.startAdminUI()
                else:
                    self.startUserUI()
            else:
                self.wrongIDorPassword()
        except SyntaxError:
            self.wrongIDorPassword()

    def messageBox(self,title,text,icon):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(icon)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.exec()

    def wrongIDorPassword(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(2)
        msg.setText("Sorry, Either ID or Password is wrong.")
        msg.setWindowTitle("User not found")
        msg.exec()

    def idAlreadyExist(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(2)
        msg.setText("Sorry, This username is already exist.")
        msg.setWindowTitle("Username Already Exist")
        msg.exec()

    def loggedIn(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(1)
        msg.setText("LOGGED IN AS ADMIN.")
        msg.setWindowTitle("Successfully Logged In")
        if type(self.currentUser) == Admin:
            msg.setText("LOGGED IN AS ADMIN.")
        else:
            msg.setText("LOGGED IN")
        msg.exec()


    def startAdminUI(self):
        print("AdminUI")
        self.adminInterface.setupUi(self.adminWindow)
        self.adminWindow.show()
        self.adminWindow.setWindowTitle("Minor Admin")
        self.adminInterface.regisButton.clicked.connect(self.startRegPage)
        self.adminInterface.movieButton.clicked.connect(self.movieSetting)
        self.adminInterface.topupButton.clicked.connect(self.topupPage)
        self.adminInterface.showtimeButton.clicked.connect(self.cinemaeditchoice)
        self.adminInterface.logoutButton.clicked.connect(self.logout)
        self.hide()

    def topupPage(self):
        from topupUI import Ui_topup
        self.topupUI = QtWidgets.QMainWindow()
        self.topupInterface = Ui_topup()
        self.topupInterface.setupUi(self.topupUI)
        self.topupInterface.topupButtop.clicked.connect(self.topup)
        self.topupUI.show()

    def topup(self):
        for user in self.userList:
            if user.username == self.topupInterface.idInput.text():
                user.cash += int(self.topupInterface.lineEdit_2.text())
                self.messageBox("SUCCESS","TOPUP SUCCESSFUL",0)
                self.topupUI.close()
        self.saveUserFile()
        self.messageBox("ERROR","ID NOT FOUND",4)

    def movieSetting(self):
        self.movieSetUI = QtWidgets.QMainWindow()
        self.movieSettingInterface.setupUi(self.movieSetUI)
        self.movieSettingInterface.saveButton.clicked.connect(self.saveMovie)
        self.movieSetUI.show()

    def saveMovie(self):
        self.movieList = []
        if self.movieSettingInterface.mname1.text()!= "" and self.movieSettingInterface.photo1.text() != "":
            self.movieList.append(Movie(self.movieSettingInterface.mname1.text(),self.movieSettingInterface.photo1.text()))
        if self.movieSettingInterface.mname2.text() != "" and self.movieSettingInterface.photo2.text() != "":
            self.movieList.append(Movie(self.movieSettingInterface.mname2.text(), self.movieSettingInterface.photo2.text()))
        if self.movieSettingInterface.mname3.text() != "" and self.movieSettingInterface.photo3.text() != "":
            self.movieList.append(Movie(self.movieSettingInterface.mname3.text(), self.movieSettingInterface.photo3.text()))
        if self.movieSettingInterface.mname4.text() != "" and self.movieSettingInterface.photo4.text() != "":
            self.movieList.append(Movie(self.movieSettingInterface.mname4.text(), self.movieSettingInterface.photo4.text()))
        if self.movieSettingInterface.mname5.text() != "" and self.movieSettingInterface.photo5.text() != "":
            self.movieList.append(Movie(self.movieSettingInterface.mname5.text(), self.movieSettingInterface.photo5.text()))
        self.messageBox("Movie Saved","Movie List Saved!", 1)
        self.saveMovieFile()
        self.movieSetUI.close()

    def cinemaeditchoice(self):
        from cinemaEditSelection import  Ui_CinemaEdit
        CinemaEditUI = Ui_CinemaEdit()
        self.cinemaEdit = QtWidgets.QMainWindow()
        CinemaEditUI.setupUi(self.cinemaEdit)
        CinemaEditUI.twodthai.clicked.connect(lambda:self.showtimeSetting(0))
        CinemaEditUI.twodst.clicked.connect(lambda: self.showtimeSetting(1))
        CinemaEditUI.threedthai.clicked.connect(lambda: self.showtimeSetting(2))
        CinemaEditUI.threedst.clicked.connect(lambda: self.showtimeSetting(3))
        CinemaEditUI.imaxthai.clicked.connect(lambda: self.showtimeSetting(4))
        CinemaEditUI.imaxst.clicked.connect(lambda: self.showtimeSetting(5))
        self.cinemaEdit.show()

    def showtimeSetting(self,selectedCinema):
        from playtimeEdit import Ui_playtimeEdit
        self.timeSetUI= Ui_playtimeEdit()
        self.showTimeSetUI = QtWidgets.QMainWindow()
        self.timeSetUI.setupUi(self.showTimeSetUI)
        self.showTimeSetUI.show()
        self.timeSetUI.pushButton.clicked.connect(lambda: self.savetime(selectedCinema))

    def savetime(self, selectedCinema):
        self.cinemas[selectedCinema].rounds[0].time = self.timeSetUI.time1.text()
        self.cinemas[selectedCinema].rounds[1].time = self.timeSetUI.time2.text()
        self.cinemas[selectedCinema].rounds[2].time = self.timeSetUI.time3.text()
        self.cinemas[selectedCinema].rounds[3].time = self.timeSetUI.time4.text()
        self.cinemas[selectedCinema].rounds[4].time = self.timeSetUI.time5.text()
        self.cinemas[selectedCinema].rounds[5].time = self.timeSetUI.time6.text()
        self.cinemas[selectedCinema].rounds[0].movie = self.timeSetUI.name1.text()
        self.cinemas[selectedCinema].rounds[1].movie = self.timeSetUI.name2.text()
        self.cinemas[selectedCinema].rounds[2].movie = self.timeSetUI.name3.text()
        self.cinemas[selectedCinema].rounds[3].movie = self.timeSetUI.name4.text()
        self.cinemas[selectedCinema].rounds[4].movie = self.timeSetUI.name5.text()
        self.cinemas[selectedCinema].rounds[5].movie = self.timeSetUI.name6.text()
        self.messageBox("SAVED","TIMETABLE SAVED!",1)
        self.showTimeSetUI.close()



    def startUserUI(self):
        print("UserUI")
        self.userInterface.setupUi(self.userWindow,self.currentUser,self.movieList)
        self.userWindow.show()
        self.userInterface.background.setPixmap(QPixmap("userBG.jpg"))
        self.userInterface.quitButton.clicked.connect(self.logout)
        if len(self.movieList) >= 1:
            self.userInterface.movie1Button.clicked.connect(lambda: self.selectMovie(0))
        if len(self.movieList) >= 2:
            self.userInterface.movie2Button.clicked.connect(lambda: self.selectMovie(1))
        if len(self.movieList) >= 3:
            self.userInterface.movie3Button.clicked.connect(lambda: self.selectMovie(2))
        if len(self.movieList) >= 4:
            self.userInterface.movie4Button.clicked.connect(lambda: self.selectMovie(3))
        if len(self.movieList) >= 5:
            self.userInterface.movie5Button.clicked.connect(lambda: self.selectMovie(4))
        self.hide()


    def selectMovie(self,number):
        self.selectedMovie = self.movieList[number]
        self.startCinemaSelection(self.selectedMovie)

    def startCinemaSelection(self,movie):
        self.cinemaChoosingPage = QtWidgets.QMainWindow()
        self.cinemaSelectionUi.setupUi(self.cinemaChoosingPage,movie,self.selectedMovie)
        self.roundlist = []
        buttonline = []
        cinemanumber = 0
        for cinema in self.cinemas:
            buttons = []
            buttonnumber = 0
            for round in cinema.rounds:
                if movie.name == round.movie:
                    button = QtWidgets.QPushButton(self.cinemaChoosingPage)
                    buttons.append(button)
                    buttons[buttonnumber].setGeometry(QtCore.QRect(110+(buttonnumber*60), 130+(cinemanumber*40), 51, 23))
                    buttons[buttonnumber].setText(round.time)
                    gotoround = partial(self.seatSelection,cinema,self.cinemas[buttonnumber].rounds[cinemanumber])
                    buttons[buttonnumber].clicked.connect(gotoround)
                    print(self.cinemas[cinemanumber].rounds[buttonnumber].time)
                    buttonnumber += 1
            buttonline.append(buttons)
            cinemanumber += 1
        self.cinemaChoosingPage.show()



    def logout(self):
        self.adminWindow.close()
        self.userWindow.close()
        self.currentUser = False
        self.show()
        self.loginPage.passInput.clear()
        self.loginPage.userInput.clear()

    def seatSelection(self,cinema,round):
        normalE = QtGui.QIcon()
        normalO = QtGui.QIcon()
        honeyE = QtGui.QIcon()
        honeyO = QtGui.QIcon()
        normalE.addPixmap(QtGui.QPixmap("nseat0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        normalO.addPixmap(QtGui.QPixmap("nseat1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        honeyE.addPixmap(QtGui.QPixmap("hseat0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        honeyO.addPixmap(QtGui.QPixmap("hseat1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.seatSelectionWindow = QtWidgets.QMainWindow()
        print(round.rows)
        print(round.column)
        print(len(round.seat))
        print(len(round.seat[1]))

        self.seatList = []
        for row in range(round.rows):
            rowlist = []
            for column in range(round.column):
                rowlist.append(QtWidgets.QPushButton(self.seatSelectionWindow))
                if row >= round.rows - round.hrows:
                    if round.seat[row][column].owned:
                        rowlist[column].setIcon(honeyO)
                        rowlist[column].setEnabled(False)
                    else:
                        rowlist[column].setIcon(honeyE)
                else:
                    if round.seat[row][column].owned:
                        rowlist[column].setIcon(normalO)
                        rowlist[column].setEnabled(False)
                    else:
                        rowlist[column].setIcon(normalE)

                self.seatSelectionWindow.resize(150 + 30*column,245 + 35*row)
                rowlist[column].setGeometry(QtCore.QRect(45 + (30 * column), 150 + (35 * row), 30, 35))
                rowlist[column].setIconSize(QtCore.QSize(30,35))
                buyticket = partial(self.selectSeat,row,column,cinema, round)
                rowlist[column].clicked.connect(buyticket)
            self.seatList.append(rowlist)
            print(len(rowlist))
        self.seatSelectionWindow.show()
        print(len(rowlist))

    def selectSeat(self,row,column,cinema,round):
        if row <= round.rows - round.hrows:
            price = cinema.normalcost
        else:
            price = cinema.honeymooncost
        if self.currentUser.cash - price < 0:
            self.messageBox("NO MONEY","not enough money to buy the seat.",4)
        else:
            self.currentUser.cash-=price
            self.messageBox("Bought","You bought the seat " + chr(65+row)+str(column) + " For " + str(price) + '฿',1)
            round.seat[row][column].owned = True
            self.currentUser.ownedSeat.append(Ticket(round.time,round.movie,chr(65+row)+str(column)))
            self.seatSelectionWindow.close()
            self.saveAll()

    def saveUserFile(self):
        userfile = open("users.bin", "wb")
        pickle.dump(self.userList, userfile)
        userfile.close()

    def saveMovieFile(self):
        moviefile = open("movies.bin", "wb")
        pickle.dump(self.movieList, moviefile)
        moviefile.close()

    def saveCinemasFile(self):
        cinemasifile = open("cinemas.bin", "wb")
        pickle.dump(self.cinemas, cinemasifile)
        cinemasifile.close()

    def saveAll(self):
        userfile = open("users.bin","wb")
        pickle.dump(self.userList,userfile)
        userfile.close()

        moviefile = open("movies.bin", "wb")
        pickle.dump(self.movieList, moviefile)
        moviefile.close()

        cinemasifile = open("cinemas.bin", "wb")
        pickle.dump(self.cinemas,cinemasifile)
        cinemasifile.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainApp()
    sys.exit(app.exec_())