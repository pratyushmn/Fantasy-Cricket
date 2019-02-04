# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startscreen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from newteam import Ui_NewTeamWindow
from evaluate import Ui_EvaluateWindow

class Ui_MainWindow(object):

    # function to open the new team window
    def openNewTeam(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_NewTeamWindow()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    # function to open the evaluate team window
    def openEvaluate(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EvaluateWindow()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1019, 651)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newButton = QtWidgets.QPushButton(self.centralwidget)
        self.newButton.setAutoDefault(False)
        self.newButton.setDefault(False)
        self.newButton.setFlat(False)
        self.newButton.setObjectName("newButton")
        self.horizontalLayout.addWidget(self.newButton)
        self.evaluateButton = QtWidgets.QPushButton(self.centralwidget)
        self.evaluateButton.setObjectName("evaluateButton")
        self.horizontalLayout.addWidget(self.evaluateButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # connecting signals sent by clicked buttons to relevant functions
        self.newButton.clicked.connect(self.openNewTeam)
        self.evaluateButton.clicked.connect(self.openEvaluate)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#0000ff;\">Fantasy Cricket Game</span></p></body></html>"))
        self.newButton.setText(_translate("MainWindow", "Create/Open Team"))
        self.evaluateButton.setText(_translate("MainWindow", "Evaluate Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

