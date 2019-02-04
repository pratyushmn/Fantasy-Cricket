# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newteam.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from evaluate import Ui_EvaluateWindow
import sqlite3

# class to pop-up an error message when object is created
class popup(QtWidgets.QErrorMessage):
    def __init__(self, text):
        super().__init__()
        self.showMessage(text)
        
# main UI class
class Ui_NewTeamWindow(object):
    
    # method to create error message with whatever error it is called with
    def issue(self, text):
        self.popup = popup(text)
        self.popup.show()

    # method to open the EVALUATE team window
    def openEvaluate(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EvaluateWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def setupUi(self, NewTeamWindow):
        NewTeamWindow.setObjectName("NewTeamWindow")
        NewTeamWindow.resize(1495, 917)
        self.centralwidget = QtWidgets.QWidget(NewTeamWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.batCount = QtWidgets.QLabel(self.centralwidget)
        self.batCount.setObjectName("batCount")
        self.horizontalLayout.addWidget(self.batCount)
        self.bowCount = QtWidgets.QLabel(self.centralwidget)
        self.bowCount.setObjectName("bowCount")
        self.horizontalLayout.addWidget(self.bowCount)
        self.ARCount = QtWidgets.QLabel(self.centralwidget)
        self.ARCount.setObjectName("ARCount")
        self.horizontalLayout.addWidget(self.ARCount)
        self.wkCount = QtWidgets.QLabel(self.centralwidget)
        self.wkCount.setObjectName("wkCount")
        self.horizontalLayout.addWidget(self.wkCount)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pointsAvail = QtWidgets.QLabel(self.centralwidget)
        self.pointsAvail.setObjectName("pointsAvail")
        self.horizontalLayout_5.addWidget(self.pointsAvail)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pointsUsed = QtWidgets.QLabel(self.centralwidget)
        self.pointsUsed.setObjectName("pointsUsed")
        self.horizontalLayout_5.addWidget(self.pointsUsed)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.batRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.batRadio.setObjectName("batRadio")
        self.horizontalLayout_9.addWidget(self.batRadio)
        self.bowlRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.bowlRadio.setObjectName("bowlRadio")
        self.horizontalLayout_9.addWidget(self.bowlRadio)
        self.arRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.arRadio.setObjectName("arRadio")
        self.horizontalLayout_9.addWidget(self.arRadio)
        self.wkRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.wkRadio.setObjectName("wkRadio")
        self.horizontalLayout_9.addWidget(self.wkRadio)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_9.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fullPlayerList = QtWidgets.QListWidget(self.centralwidget)
        self.fullPlayerList.setObjectName("fullPlayerList")
        self.horizontalLayout_2.addWidget(self.fullPlayerList)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.selectedPlayerList = QtWidgets.QListWidget(self.centralwidget)
        self.selectedPlayerList.setObjectName("selectedPlayerList")
        self.horizontalLayout_2.addWidget(self.selectedPlayerList)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        NewTeamWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NewTeamWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1495, 43))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        NewTeamWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NewTeamWindow)
        self.statusbar.setObjectName("statusbar")
        NewTeamWindow.setStatusBar(self.statusbar)
        self.actionSAVE_Team = QtWidgets.QAction(NewTeamWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionOPEN_Team = QtWidgets.QAction(NewTeamWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(NewTeamWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.actionNEW_Team = QtWidgets.QAction(NewTeamWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        # connecting the menu action buttons to relevant methods
        self.actionEVALUATE_Team.triggered.connect(self.openEvaluate)
        self.actionSAVE_Team.triggered.connect(self.saveTeam)
        self.actionOPEN_Team.triggered.connect(self.openTeam)
        self.actionNEW_Team.triggered.connect(self.createNewTeam)

        self.retranslateUi(NewTeamWindow)
        QtCore.QMetaObject.connectSlotsByName(NewTeamWindow)

        # connecting the radio buttons to relevant methods
        self.wkRadio.toggled.connect(self.populateListWK)
        self.batRadio.toggled.connect(self.populateListBat)
        self.arRadio.toggled.connect(self.populateListAR)
        self.bowlRadio.toggled.connect(self.populateListBowl)

        # defining the behavior of moving a player between lists when his name is clicked
        self.fullPlayerList.itemDoubleClicked.connect(self.selectPlayer)
        self.selectedPlayerList.itemDoubleClicked.connect(self.dropPlayer)

        # variables to store important message
        self.totalPlayers = 0
        self.batsmen = 0
        self.bowlers = 0
        self.ar = 0
        self.wk = 0
        self.points = 1000
        self.pointsSpent = 0
        
    def retranslateUi(self, NewTeamWindow):
        _translate = QtCore.QCoreApplication.translate
        NewTeamWindow.setWindowTitle(_translate("NewTeamWindow", "MainWindow"))
        self.label.setText(_translate("NewTeamWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Your Selections:</span></p></body></html>"))
        self.batCount.setText(_translate("NewTeamWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Batsmen (BAT): " + '<span style=" font-weight:600; color:#0000ff;">' + str(0) + '</span>' + "</span></p></body></html>"))
        self.bowCount.setText(_translate("NewTeamWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Bowlers (BOW): " + '<span style=" font-weight:600; color:#0000ff;">' + str(0) + '</span>' + "</span></p></body></html>"))
        self.ARCount.setText(_translate("NewTeamWindow", "<html><head/><body><p><span style=\" font-weight:600;\">All-Rounders (AR): " + '<span style=" font-weight:600; color:#0000ff;">' + str(0) + '</span>' + "</span></p></body></html>"))
        self.wkCount.setText(_translate("NewTeamWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Wicket-Keeper (WK): " + '<span style=" font-weight:600; color:#0000ff;">' + str(0) + '</span>' + "</span></p></body></html>"))
        self.pointsAvail.setText(_translate("NewTeamWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Points Available: </span>" + '<span style=" color:#0000ff;">' + str(1000) + '</span></p></body></html>'))
        self.pointsUsed.setText(_translate("NewTeamWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Points Used: </span>"  + '<span style=" color:#0000ff;">' + str(0) + '</span></p></body></html>'))
        self.batRadio.setText(_translate("NewTeamWindow", "BAT"))
        self.bowlRadio.setText(_translate("NewTeamWindow", "BOW"))
        self.arRadio.setText(_translate("NewTeamWindow", "AR"))
        self.wkRadio.setText(_translate("NewTeamWindow", "WK"))
        self.label_2.setText(_translate("NewTeamWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Team Name:</span></p></body></html>"))
        self.menuManage_Teams.setTitle(_translate("NewTeamWindow", "Manage Teams"))
        self.actionSAVE_Team.setText(_translate("NewTeamWindow", "SAVE Team"))
        self.actionOPEN_Team.setText(_translate("NewTeamWindow", "OPEN Team"))
        self.actionEVALUATE_Team.setText(_translate("NewTeamWindow", "EVALUATE Team"))
        self.actionNEW_Team.setText(_translate("NewTeamWindow", "NEW Team"))

    # method to populate List 1 with wicket-keeper players
    def populateListWK(self):
        # clearing it of its current contents and finding which players were already selected
        self.fullPlayerList.clear()
        selected = []
        for index in range(self.selectedPlayerList.count()):
            selected.append((self.selectedPlayerList.item(index)).text())

        # connecting to the database and fetching all players
        myCricket = sqlite3.connect('cricket.db')
        cricketCursor = myCricket.cursor()
        cricketCursor.execute('''SELECT Player FROM match;''')
        namesCollection = cricketCursor.fetchall()

        # only add name from the database if it has the relevant role attribute and was not selected
        for name in namesCollection:
            name = name[0]
            cricketCursor.execute('''SELECT ctg FROM stats WHERE player=?;''', (name,))
            role = cricketCursor.fetchone()
            role = role[0]
            if role == "WK":
                if name not in selected:
                    self.fullPlayerList.addItem(name)
                    
        myCricket.close()

    def populateListBat(self):
        # clearing it of its current contents and finding which players were already selected
        self.fullPlayerList.clear()
        selected = []
        for index in range(self.selectedPlayerList.count()):
            selected.append((self.selectedPlayerList.item(index)).text())
            
        # connecting to the database and fetching all players   
        myCricket = sqlite3.connect('cricket.db')
        cricketCursor = myCricket.cursor()
        cricketCursor.execute('''SELECT Player FROM match;''')
        namesCollection = cricketCursor.fetchall()
        
        # only add name from the database if it has the relevant role attribute and was not selected        
        for name in namesCollection:
            name = name[0]
            cricketCursor.execute('''SELECT ctg FROM stats WHERE player=?;''', (name,))
            role = cricketCursor.fetchone()
            role = role[0]
            if role == "BAT":
               if name not in selected:
                   self.fullPlayerList.addItem(name)
                   
        myCricket.close()

    def populateListAR(self):
        # clearing it of its current contents and finding which players were already selected        
        self.fullPlayerList.clear()
        selected = []
        for index in range(self.selectedPlayerList.count()):
            selected.append((self.selectedPlayerList.item(index)).text())
            
        # connecting to the database and fetching all players               
        myCricket = sqlite3.connect('cricket.db')
        cricketCursor = myCricket.cursor()
        cricketCursor.execute('''SELECT Player FROM match;''')
        namesCollection = cricketCursor.fetchall()
        
        # only add name from the database if it has the relevant role attribute and was not selected        
        for name in namesCollection:
            name = name[0]
            cricketCursor.execute('''SELECT ctg FROM stats WHERE player=?;''', (name,))
            role = cricketCursor.fetchone()
            role = role[0]
            if role == "AR":
                if name not in selected:
                    self.fullPlayerList.addItem(name)
                    
        myCricket.close()

    def populateListBowl(self):
        # clearing it of its current contents and finding which players were already selected
        self.fullPlayerList.clear()
        selected = []
        for index in range(self.selectedPlayerList.count()):
            selected.append((self.selectedPlayerList.item(index)).text())
            
        # connecting to the database and fetching all players                           
        myCricket = sqlite3.connect('cricket.db')
        cricketCursor = myCricket.cursor()
        cricketCursor.execute('''SELECT Player FROM match;''')
        namesCollection = cricketCursor.fetchall()
        
        # only add name from the database if it has the relevant role attribute and was not selected        
        for name in namesCollection:
            name = name[0]
            cricketCursor.execute('''SELECT ctg FROM stats WHERE player=?;''', (name,))
            role = cricketCursor.fetchone()
            role = role[0]
            if role == "BWL":
               if name not in selected:
                    self.fullPlayerList.addItem(name)
                    
        myCricket.close()

    # function to call when user selects a player for their team
    def selectPlayer(self, item):
        player = item.text()

        # finding the value and role of the selected player from the database
        myCricket = sqlite3.connect('cricket.db')
        cricketCursor = myCricket.cursor()
        cricketCursor.execute('''SELECT ctg FROM stats WHERE player=?;''', (player,))
        role = cricketCursor.fetchone()
        role = role[0]
        cricketCursor.execute('''SELECT value FROM stats WHERE player=?;''', (player,))
        value = cricketCursor.fetchone()
        value = int(value[0])

        # checking for logic errors; add the player if none of the logic errors are raised
        # update the relevant information storing variables
        if self.totalPlayers == 11 or self.pointsSpent + value > 1000:
            if self.totalPlayers == 11:
                self.issue("You have picked too many players.")
            elif (self.pointsSpent + value) > 1000:
                self.issue("You can't afford " + player)
        elif role == "BAT":
            if self.batsmen >= 4:
                self.issue("You can't select more than 4 batsmen.")
            else:
                self.fullPlayerList.takeItem(self.fullPlayerList.row(item))
                self.selectedPlayerList.addItem(item.text())
                self.totalPlayers = self.totalPlayers + 1
                self.batsmen = self.batsmen + 1
                self.pointsSpent = self.pointsSpent + value
                self.points = self.points - value
        elif role == "BWL":
            if self.bowlers >= 3:
                self.issue("You can't select more than 3 bowlers.")
            else:
                self.fullPlayerList.takeItem(self.fullPlayerList.row(item))
                self.selectedPlayerList.addItem(item.text())
                self.totalPlayers = self.totalPlayers + 1
                self.bowlers = self.bowlers + 1
                self.pointsSpent = self.pointsSpent + value
                self.points = self.points - value
        elif role == "AR":
            if self.ar >= 3:
                self.issue("You can't select more than 3 all rounders.")
            else:
                self.fullPlayerList.takeItem(self.fullPlayerList.row(item))
                self.selectedPlayerList.addItem(item.text())
                self.totalPlayers = self.totalPlayers + 1
                self.ar = self.ar + 1
                self.pointsSpent = self.pointsSpent + value
                self.points = self.points - value
        elif role == "WK":
            if self.wk >= 1:
                self.issue("You can't select more than 1 wicket keeper.")
            else:
                self.fullPlayerList.takeItem(self.fullPlayerList.row(item))
                self.selectedPlayerList.addItem(item.text())
                self.totalPlayers = self.totalPlayers + 1
                self.wk = self.wk + 1
                self.pointsSpent = self.pointsSpent + value
                self.points = self.points - value
                
        self.updateText()
        myCricket.close()

    # function to call when user removes a player from their team
    def dropPlayer(self, item):
        # adding and removing the player from the respective lists
        self.selectedPlayerList.takeItem(self.selectedPlayerList.row(item))
        self.fullPlayerList.addItem(item.text())
        player = item.text()

        # connecting to the database to find the player's role and value
        myCricket = sqlite3.connect('cricket.db')
        cricketCursor = myCricket.cursor()
        cricketCursor.execute('''SELECT ctg FROM stats WHERE player=?;''', (player,))
        role = cricketCursor.fetchone()
        role = role[0]
        cricketCursor.execute('''SELECT value FROM stats WHERE player=?;''', (player,))
        value = cricketCursor.fetchone()
        value = int(value[0])

        # updating the information storing variables based on information gathered from database
        if role == "BAT":
            self.fullPlayerList.takeItem(self.fullPlayerList.row(item))
            self.selectedPlayerList.addItem(item.text())
            self.totalPlayers = self.totalPlayers - 1
            self.batsmen = self.batsmen - 1
            self.pointsSpent = self.pointsSpent - value
            self.points = self.points + value
        elif role == "BWL":
            self.fullPlayerList.takeItem(self.fullPlayerList.row(item))
            self.selectedPlayerList.addItem(item.text())
            self.totalPlayers = self.totalPlayers - 1
            self.bowlers = self.bowlers - 1
            self.pointsSpent = self.pointsSpent - value
            self.points = self.points + value
        elif role == "AR":
            self.fullPlayerList.takeItem(self.fullPlayerList.row(item))
            self.selectedPlayerList.addItem(item.text())
            self.totalPlayers = self.totalPlayers - 1
            self.ar = self.ar - 1
            self.pointsSpent = self.pointsSpent - value
            self.points = self.points + value
        elif role == "WK":
            self.fullPlayerList.takeItem(self.fullPlayerList.row(item))
            self.selectedPlayerList.addItem(item.text())
            self.totalPlayers = self.totalPlayers - 1
            self.wk = self.wk - 1
            self.pointsSpent = self.pointsSpent - value
            self.points = self.points + value
            
        self.updateText()        
        myCricket.close()

    # function to call when user wants to save their team
    def saveTeam(self):
        # gathering the team name from the input
        teamName = self.lineEdit.text()

        # checking for errors
        if teamName == "":
            self.issue("Enter a Team Name before saving.")
        elif self.totalPlayers < 11:
            self.issue("Your team does not have enough players.")
        elif self.wk < 1:
            self.issue("Your team does not have enough wicket-keepers.")
        elif self.batsmen < 1:
            self.issue("Your team does not have enough batsmen.")
        elif self.bowlers < 1:
            self.issue("Your team does not have enough bowlers.")
        else:
            # if no errors, store the team in the database
            myCricket = sqlite3.connect('cricket.db')
            cricketCursor = myCricket.cursor()
            score = 0

            # create a string with all team player names
            teamPlayers = ""
            for index in range(self.selectedPlayerList.count()):
                teamPlayers = teamPlayers + " " + str(self.selectedPlayerList.item(index).text())

            # checking if the team name exists already  
            try:
                cricketCursor.execute('''INSERT INTO teams (name, players, value) VALUES (?,?,?);''', (teamName, teamPlayers, score))
                myCricket.commit()
                myCricket.close()
            except:
                myCricket.rollback()
                self.issue("Error: Team name already taken. Choose a new name.")

    # function to call when user wants to open a pre-created team
    def openTeam(self):
        # reset all info variables
        self.totalPlayers = 0
        self.points = 0
        self.pointsSpent = 0
        self.wk = 0
        self.batsmen = 0
        self.bowlers = 0
        self.ar = 0

        # get the team name from user input
        teamName = self.getInput()

        # checking the database for the team entered, and then updating all information variables with what's found, as well as adding each name to the lists
        if teamName == "":
            self.issue("Empty Team Name. Please enter a name in the field and try again")
        else:
            myCricket = sqlite3.connect('cricket.db')
            cricketCursor = myCricket.cursor()
            try:
                cricketCursor.execute("SELECT players FROM teams WHERE name = ?;", (teamName,))
                team = cricketCursor.fetchone()
                team = team[0]
                players = team.split()
                for player in players:
                    cricketCursor.execute("SELECT ctg FROM stats WHERE player=?;", (player,))
                    role = cricketCursor.fetchone()
                    role = role[0]
                    if role == "WK":
                        self.wk += 1
                    elif role == "BAT":
                        self.batsmen += 1
                    elif role == "BWL":
                        self.bowlers += 1
                    elif role == "AR":
                        self.ar += 1
                    cricketCursor.execute("SELECT value FROM stats WHERE player=?;", (player,))
                    value = cricketCursor.fetchone()
                    value = value[0]
                    self.pointsSpent += value
                    self.points = 1000 - self.pointsSpent
                    self.selectedPlayerList.addItem(player)
                self.totalPlayers = 11
                self.updateText()
            except:
                self.issue("Name not found. Try again.")
                
            myCricket.close()

    # function to update the text of QLabel objects while keeping formatting
    def updateText(self):
        self.wkCount.setText("<html><head/><body><p><span style=\" font-weight:600;\">Wicket-Keeper (WK): " + '<span style=" font-weight:600; color:#0000ff;">' + str(self.wk) + '</span>' + "</span></p></body></html>")
        self.ARCount.setText("<html><head/><body><p><span style=\" font-weight:600;\">All-Rounders (AR): " +  '<span style=" font-weight:600; color:#0000ff;">' + str(self.ar) + '</span>' + "</span></p></body></html>")
        self.bowCount.setText("<html><head/><body><p><span style=\" font-weight:600;\">Bowlers (BWL): " + '<span style=" font-weight:600; color:#0000ff;">' + str(self.bowlers) + '</span>' + "</span></p></body></html>")
        self.batCount.setText("<html><head/><body><p><span style=\" font-weight:600;\">Batsmen (BAT): " +  '<span style=" font-weight:600; color:#0000ff;">' + str(self.batsmen) + '</span>' + "</span></p></body></html>")
        self.pointsAvail.setText("<html><head/><body><p><span style=\" font-weight:600;\">Points Available: </span>" +  '<span style=" color:#0000ff;">' + str(self.points) + '</span>' + "</p></body></html>")
        self.pointsUsed.setText("<html><head/><body><p><span style=\" font-weight:600;\">Points Spent: </span>" +  '<span style=" color:#0000ff;">' + str(self.pointsSpent) + '</span>' + "</p></body></html>")

    # function to reset all variables and lists when player wants a new team
    def createNewTeam(self):
        self.totalPlayers = 0
        self.points = 1000
        self.pointsSpent = 0
        self.wk = 0
        self.batsmen = 0
        self.bowlers = 0
        self.ar = 0
        self.fullPlayerList.clear()
        self.selectedPlayerList.clear()
        self.updateText()

    # function to open a new window to get text input from user
    def getInput(self):
        text, okPressed = QtWidgets.QInputDialog.getText(None, "Open Team", "Team Name:", QtWidgets.QLineEdit.Normal, "")
        if okPressed and text != "":
            return text

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewTeamWindow = QtWidgets.QMainWindow()
    ui = Ui_NewTeamWindow()
    ui.setupUi(NewTeamWindow)
    NewTeamWindow.show()
    sys.exit(app.exec_())

