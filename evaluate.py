# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import calc

# class to pop-up an error message when object is created
class popup(QtWidgets.QErrorMessage):
    def __init__(self, text):
        super().__init__()
        self.showMessage(text)

# main UI class
class Ui_EvaluateWindow(object):
    
    # method to create error message with whatever error it is called with    
    def issue(self, text):
        self.popup = popup(text)
        self.popup.show()
        
    def setupUi(self, EvaluateWindow):
        EvaluateWindow.setObjectName("EvaluateWindow")
        EvaluateWindow.resize(1160, 830)
        self.centralwidget = QtWidgets.QWidget(EvaluateWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.teamSelectBox = QtWidgets.QComboBox(self.centralwidget)
        self.teamSelectBox.setObjectName("teamSelectBox")
        self.teamSelectBox.addItem("")
        self.horizontalLayout_2.addWidget(self.teamSelectBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.matchSelectBox = QtWidgets.QComboBox(self.centralwidget)
        self.matchSelectBox.setObjectName("matchSelectBox")
        self.matchSelectBox.addItem("")
        self.horizontalLayout_2.addWidget(self.matchSelectBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(275, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.pointsVal = QtWidgets.QLabel(self.centralwidget)
        self.pointsVal.setText("")
        self.pointsVal.setObjectName("pointsVal")
        self.horizontalLayout_4.addWidget(self.pointsVal)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.playerList = QtWidgets.QListWidget(self.centralwidget)
        self.playerList.setObjectName("playerList")
        self.horizontalLayout_5.addWidget(self.playerList)
        self.pointsList = QtWidgets.QListWidget(self.centralwidget)
        self.pointsList.setObjectName("pointsList")
        self.horizontalLayout_5.addWidget(self.pointsList)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.calculateScore = QtWidgets.QPushButton(self.centralwidget)
        self.calculateScore.setObjectName("calculateScore")
        self.horizontalLayout_7.addWidget(self.calculateScore)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        EvaluateWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EvaluateWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1160, 43))
        self.menubar.setObjectName("menubar")
        EvaluateWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EvaluateWindow)
        self.statusbar.setObjectName("statusbar")
        EvaluateWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EvaluateWindow)
        QtCore.QMetaObject.connectSlotsByName(EvaluateWindow)

        # connecting all signals to slots/methods which perform tasks
        self.teamSelectBox.highlighted.connect(self.populateTeams)
        self.matchSelectBox.highlighted.connect(self.populateTeams)
        self.teamSelectBox.activated.connect(self.populatePlayers)
        self.matchSelectBox.activated.connect(self.setMatch)
        self.calculateScore.clicked.connect(self.calculatePoints)

        # information storing variables
        self.match = ""
        self.team =  ""
        self.points = 0

    def retranslateUi(self, EvaluateWindow):
        _translate = QtCore.QCoreApplication.translate
        EvaluateWindow.setWindowTitle(_translate("EvaluateWindow", "MainWindow"))
        self.label.setText(_translate("EvaluateWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Evaluate the Performance of Your Fantasy Team</span></p></body></html>"))
        self.teamSelectBox.setCurrentText(_translate("EvaluateWindow", "Select Team"))
        self.teamSelectBox.setItemText(0, _translate("EvaluateWindow", "Select Team"))
        self.matchSelectBox.setItemText(0, _translate("EvaluateWindow", "Select Match"))
        self.label_3.setText(_translate("EvaluateWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Players</span></p></body></html>"))
        self.label_2.setText(_translate("EvaluateWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Points</span></p></body></html>"))
        self.calculateScore.setText(_translate("EvaluateWindow", "Calculate Score"))

    # function to populate the combo box with all teams from the database
    def populateTeams(self):       
        # connect to the database and select all team names
        myCricket = sqlite3.connect('cricket.db')
        cricketCursor = myCricket.cursor()
        cricketCursor.execute("SELECT name FROM teams;")
        teamList = cricketCursor.fetchall()

        # add all teams to the combo box
        for team in teamList:
            exists = False
            for i in range(self.teamSelectBox.count()):
                if self.teamSelectBox.itemText(i) == team[0]:
                    exists = True
            if exists == False:
                self.teamSelectBox.addItem(team[0])
                
        myCricket.close()

        # make sure the match select box has the item "Match 1"
        if self.matchSelectBox.count() < 2:
            self.matchSelectBox.addItem("Match 1")

    # function to populate the list with all players in whatever team has been selected
    def populatePlayers(self, index):
        # clear the list of whatever is there already and then connect to the database to select players from whatever team has been selected
        self.playerList.clear()
        self.pointsList.clear()
        self.team = self.teamSelectBox.itemText(index)
        myCricket = sqlite3.connect('cricket.db')
        cricketCursor = myCricket.cursor()
        try:
            cricketCursor.execute("SELECT players FROM teams WHERE name = ?;", (self.team,))
            team = cricketCursor.fetchone()
            team = team[0]
            players = team.split()
            self.playerList.addItems(players)
        except:
            self.issue("Invalid Team")
        myCricket.close()

    # function to calculate points scored by each player, and then total points
    def calculatePoints(self):
        # if valid team and valid match
        if self.match == "Match 1" and self.team != "" and self.team != "Select Match":
            # reset the points
            self.pointsList.clear()
            self.points = 0
            # connect to the database and select all players from that team
            myCricket = sqlite3.connect('cricket.db')
            cricketCursor = myCricket.cursor()
            try:
                cricketCursor.execute("SELECT players FROM teams WHERE name = ?;", (self.team,))
                team = cricketCursor.fetchone()
                team = team[0]
                players = team.split()
                for player in players:
                    # go through each player and then call function to calculate points scored by the player
                    scored = calc.totalPoints(player)
                    self.pointsList.addItem(str(scored))
                    self.points += scored
                self.pointsVal.setText('<html><head/><body><p><span style=" color:#0000ff;">' + str(self.points) + '</span></p></body></html>')
                # update the value of points scored by the team
                cricketCursor.execute("UPDATE teams SET value = ? WHERE name = ?;", (self.points, self.team))
                myCricket.close()
            except:
               self.issue("Invalid Team")
        else:
            if self.team == "" or self.team == "Select Team":
                self.issue("Invalid Team")
            else:
                self.issue("Invalid Match")
                
    # set the current match info variable
    def setMatch(self):
        if (self.matchSelectBox.currentIndex() == 1):
            self.match = "Match 1"

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EvaluateWindow = QtWidgets.QMainWindow()
    ui = Ui_EvaluateWindow()
    ui.setupUi(EvaluateWindow)
    EvaluateWindow.show()
    sys.exit(app.exec_())

