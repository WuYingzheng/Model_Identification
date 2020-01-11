# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiLib/AboutAuthor.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About_Author_Dialog(object):
    def setupUi(self, About_Author_Dialog):
        About_Author_Dialog.setObjectName("About_Author_Dialog")
        About_Author_Dialog.resize(413, 409)
        self.gridLayout = QtWidgets.QGridLayout(About_Author_Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.perspIdxlineEdit_4 = QtWidgets.QLineEdit(About_Author_Dialog)
        self.perspIdxlineEdit_4.setReadOnly(True)
        self.perspIdxlineEdit_4.setObjectName("perspIdxlineEdit_4")
        self.gridLayout.addWidget(self.perspIdxlineEdit_4, 5, 3, 1, 1)
        self.label = QtWidgets.QLabel(About_Author_Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 6, 2)
        self.label_9 = QtWidgets.QLabel(About_Author_Dialog)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 2, 1, 1)
        self.perspIdxlineEdit = QtWidgets.QLineEdit(About_Author_Dialog)
        self.perspIdxlineEdit.setReadOnly(True)
        self.perspIdxlineEdit.setObjectName("perspIdxlineEdit")
        self.gridLayout.addWidget(self.perspIdxlineEdit, 0, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(About_Author_Dialog)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 2, 1, 1)
        self.perspIdxlineEdit_5 = QtWidgets.QLineEdit(About_Author_Dialog)
        self.perspIdxlineEdit_5.setReadOnly(True)
        self.perspIdxlineEdit_5.setObjectName("perspIdxlineEdit_5")
        self.gridLayout.addWidget(self.perspIdxlineEdit_5, 1, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(About_Author_Dialog)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 2, 1, 1)
        self.perspIdxlineEdit_2 = QtWidgets.QLineEdit(About_Author_Dialog)
        self.perspIdxlineEdit_2.setReadOnly(True)
        self.perspIdxlineEdit_2.setObjectName("perspIdxlineEdit_2")
        self.gridLayout.addWidget(self.perspIdxlineEdit_2, 2, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(About_Author_Dialog)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 2, 1, 1)
        self.perspIdxlineEdit_3 = QtWidgets.QLineEdit(About_Author_Dialog)
        self.perspIdxlineEdit_3.setReadOnly(True)
        self.perspIdxlineEdit_3.setObjectName("perspIdxlineEdit_3")
        self.gridLayout.addWidget(self.perspIdxlineEdit_3, 3, 3, 1, 1)
        self.label_15 = QtWidgets.QLabel(About_Author_Dialog)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 4, 2, 1, 1)
        self.perspIdxlineEdit_7 = QtWidgets.QLineEdit(About_Author_Dialog)
        self.perspIdxlineEdit_7.setReadOnly(True)
        self.perspIdxlineEdit_7.setObjectName("perspIdxlineEdit_7")
        self.gridLayout.addWidget(self.perspIdxlineEdit_7, 4, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(About_Author_Dialog)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(About_Author_Dialog)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 6, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 44, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(About_Author_Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 3)

        self.retranslateUi(About_Author_Dialog)
        QtCore.QMetaObject.connectSlotsByName(About_Author_Dialog)

    def retranslateUi(self, About_Author_Dialog):
        _translate = QtCore.QCoreApplication.translate
        About_Author_Dialog.setWindowTitle(_translate("About_Author_Dialog", "关于作者"))
        self.perspIdxlineEdit_4.setText(_translate("About_Author_Dialog", "1014759254@qq.com"))
        self.label.setText(_translate("About_Author_Dialog", "<html><head/><body><p><img src=\":/resource/auther.png\"/></p></body></html>"))
        self.label_9.setText(_translate("About_Author_Dialog", "姓     名"))
        self.perspIdxlineEdit.setText(_translate("About_Author_Dialog", "黄超"))
        self.label_14.setText(_translate("About_Author_Dialog", "最高学历"))
        self.perspIdxlineEdit_5.setText(_translate("About_Author_Dialog", "硕士"))
        self.label_10.setText(_translate("About_Author_Dialog", "就读学校"))
        self.perspIdxlineEdit_2.setText(_translate("About_Author_Dialog", "上海工程技术大学"))
        self.label_11.setText(_translate("About_Author_Dialog", "导    师"))
        self.perspIdxlineEdit_3.setText(_translate("About_Author_Dialog", "王安斌"))
        self.label_15.setText(_translate("About_Author_Dialog", "导师职称"))
        self.perspIdxlineEdit_7.setText(_translate("About_Author_Dialog", "博士生导师　千人计划"))
        self.label_12.setText(_translate("About_Author_Dialog", "作者邮件"))
        self.label_13.setText(_translate("About_Author_Dialog", "获奖经历"))
        self.label_2.setText(_translate("About_Author_Dialog", "<html><head/><body><p>1. 全国研究生数学建模大赛二等奖 </p><p>2. 上海工程技术大学数学建模大赛一等奖 </p><p>3. 上海市长三角地区智慧城市三等奖 </p><p>4. 国家励志奖学金</p></body></html>"))
import csb_rc
