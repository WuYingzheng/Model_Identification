# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiLib/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 748)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.SpectrumLayout = QtWidgets.QVBoxLayout()
        self.SpectrumLayout.setObjectName("SpectrumLayout")
        self.gridLayout.addLayout(self.SpectrumLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 648, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_AboutAuthor = QtWidgets.QAction(MainWindow)
        self.action_AboutAuthor.setObjectName("action_AboutAuthor")
        self.action_AboutSystem = QtWidgets.QAction(MainWindow)
        self.action_AboutSystem.setObjectName("action_AboutSystem")
        self.action_SignalSample = QtWidgets.QAction(MainWindow)
        self.action_SignalSample.setObjectName("action_SignalSample")
        self.action_SignalGen = QtWidgets.QAction(MainWindow)
        self.action_SignalGen.setObjectName("action_SignalGen")
        self.actionModel_Design = QtWidgets.QAction(MainWindow)
        self.actionModel_Design.setObjectName("actionModel_Design")
        self.menuFile.addAction(self.action_SignalSample)
        self.menuFile.addAction(self.action_SignalGen)
        self.menuSetting.addAction(self.actionModel_Design)
        self.menuAbout.addAction(self.action_AboutAuthor)
        self.menuAbout.addAction(self.action_AboutSystem)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.action_AboutAuthor.setText(_translate("MainWindow", "About Author"))
        self.action_AboutSystem.setText(_translate("MainWindow", "About System"))
        self.action_SignalSample.setText(_translate("MainWindow", "Signal Sampling"))
        self.action_SignalGen.setText(_translate("MainWindow", "Signal Generation"))
        self.actionModel_Design.setText(_translate("MainWindow", "Model Design"))
