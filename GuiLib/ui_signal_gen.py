# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiLib/SignalGen.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SignalGenDialog(object):
    def setupUi(self, SignalGenDialog):
        SignalGenDialog.setObjectName("SignalGenDialog")
        SignalGenDialog.resize(640, 480)
        self.gridLayout_2 = QtWidgets.QGridLayout(SignalGenDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget_Response = QtWidgets.QTabWidget(SignalGenDialog)
        self.tabWidget_Response.setObjectName("tabWidget_Response")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_ImportFile = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_ImportFile.setObjectName("lineEdit_ImportFile")
        self.gridLayout.addWidget(self.lineEdit_ImportFile, 0, 0, 1, 1)
        self.pushButton_ImportSignal = QtWidgets.QPushButton(self.tab)
        self.pushButton_ImportSignal.setObjectName("pushButton_ImportSignal")
        self.gridLayout.addWidget(self.pushButton_ImportSignal, 0, 1, 1, 1)
        self.MplWidget_ImportSignal = MplWidget(self.tab)
        self.MplWidget_ImportSignal.setObjectName("MplWidget_ImportSignal")
        self.gridLayout.addWidget(self.MplWidget_ImportSignal, 1, 0, 1, 2)
        self.tabWidget_Response.addTab(self.tab, "")
        self.widget_2 = QtWidgets.QWidget()
        self.widget_2.setObjectName("widget_2")
        self.layoutWidget = QtWidgets.QWidget(self.widget_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 591, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Stimulate = QtWidgets.QLabel(self.layoutWidget)
        self.label_Stimulate.setObjectName("label_Stimulate")
        self.verticalLayout.addWidget(self.label_Stimulate)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_Stimulate = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_Stimulate.setObjectName("lineEdit_Stimulate")
        self.horizontalLayout_2.addWidget(self.lineEdit_Stimulate)
        self.pushButton_Stimulate = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_Stimulate.setObjectName("pushButton_Stimulate")
        self.horizontalLayout_2.addWidget(self.pushButton_Stimulate)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget_Stimulate = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget_Stimulate.setObjectName("listWidget_Stimulate")
        self.horizontalLayout.addWidget(self.listWidget_Stimulate)
        self.MplWidget_Stimulate = MplWidget(self.layoutWidget)
        self.MplWidget_Stimulate.setObjectName("MplWidget_Stimulate")
        self.horizontalLayout.addWidget(self.MplWidget_Stimulate)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 12)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget_Response.addTab(self.widget_2, "")
        self.widget_3 = QtWidgets.QWidget()
        self.widget_3.setObjectName("widget_3")
        self.layoutWidget_2 = QtWidgets.QWidget(self.widget_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 591, 381))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_Response = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_Response.setObjectName("label_Response")
        self.verticalLayout_3.addWidget(self.label_Response)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_Response = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_Response.setObjectName("lineEdit_Response")
        self.horizontalLayout_5.addWidget(self.lineEdit_Response)
        self.pushButton_Response = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_Response.setObjectName("pushButton_Response")
        self.horizontalLayout_5.addWidget(self.pushButton_Response)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.listWidget_Response = QtWidgets.QListWidget(self.layoutWidget_2)
        self.listWidget_Response.setObjectName("listWidget_Response")
        self.horizontalLayout_6.addWidget(self.listWidget_Response)
        self.MplWidget_Response = MplWidget(self.layoutWidget_2)
        self.MplWidget_Response.setObjectName("MplWidget_Response")
        self.horizontalLayout_6.addWidget(self.MplWidget_Response)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.tabWidget_Response.addTab(self.widget_3, "")
        self.gridLayout_2.addWidget(self.tabWidget_Response, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(SignalGenDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(SignalGenDialog)
        self.tabWidget_Response.setCurrentIndex(0)
        self.buttonBox.accepted.connect(SignalGenDialog.accept)
        self.buttonBox.rejected.connect(SignalGenDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SignalGenDialog)

    def retranslateUi(self, SignalGenDialog):
        _translate = QtCore.QCoreApplication.translate
        SignalGenDialog.setWindowTitle(_translate("SignalGenDialog", "Signal Generator"))
        self.pushButton_ImportSignal.setText(_translate("SignalGenDialog", "Open File"))
        self.tabWidget_Response.setTabText(self.tabWidget_Response.indexOf(self.tab), _translate("SignalGenDialog", "Improt Signal"))
        self.label_Stimulate.setText(_translate("SignalGenDialog", "Stimulate Signal"))
        self.pushButton_Stimulate.setText(_translate("SignalGenDialog", "Open File"))
        self.tabWidget_Response.setTabText(self.tabWidget_Response.indexOf(self.widget_2), _translate("SignalGenDialog", "Analytic Signal"))
        self.label_Response.setText(_translate("SignalGenDialog", "Response Signal"))
        self.pushButton_Response.setText(_translate("SignalGenDialog", "Open File"))
        self.tabWidget_Response.setTabText(self.tabWidget_Response.indexOf(self.widget_3), _translate("SignalGenDialog", "Random Signal"))

from mplwidget import MplWidget