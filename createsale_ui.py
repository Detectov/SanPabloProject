# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\User\Documents\PharmacyFinal\PharmacyProjectFF\createsale.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(772, 481)
        Dialog.setStyleSheet("background-color: rgb(23, 136, 211);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 50, 391, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 24pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(170, 180, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.soldinput = QtWidgets.QLineEdit(Dialog)
        self.soldinput.setGeometry(QtCore.QRect(330, 180, 231, 31))
        self.soldinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.soldinput.setObjectName("soldinput")
        self.amountinput = QtWidgets.QLineEdit(Dialog)
        self.amountinput.setGeometry(QtCore.QRect(330, 220, 61, 31))
        self.amountinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.amountinput.setObjectName("amountinput")
        self.billedinput = QtWidgets.QLineEdit(Dialog)
        self.billedinput.setGeometry(QtCore.QRect(330, 260, 111, 31))
        self.billedinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.billedinput.setObjectName("billedinput")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(230, 210, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";")
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(170, 250, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";")
        self.label_10.setObjectName("label_10")
        self.backbutton = QtWidgets.QPushButton(Dialog)
        self.backbutton.setGeometry(QtCore.QRect(470, 410, 91, 21))
        self.backbutton.setStyleSheet("background-color: rgb(167, 168, 167);\n"
"background-color: rgb(156, 208, 93);\n"
"color: rgb(255, 255, 255);")
        self.backbutton.setObjectName("backbutton")
        self.donebutton = QtWidgets.QPushButton(Dialog)
        self.donebutton.setGeometry(QtCore.QRect(250, 410, 91, 21))
        self.donebutton.setStyleSheet("background-color: rgb(156, 208, 93);\n"
"color: rgb(255, 255, 255);")
        self.donebutton.setObjectName("donebutton")
        self.methodinput = QtWidgets.QLineEdit(Dialog)
        self.methodinput.setGeometry(QtCore.QRect(330, 300, 111, 31))
        self.methodinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.methodinput.setObjectName("methodinput")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(230, 290, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";")
        self.label_11.setObjectName("label_11")
        self.addbutton = QtWidgets.QPushButton(Dialog)
        self.addbutton.setGeometry(QtCore.QRect(470, 260, 61, 31))
        self.addbutton.setStyleSheet("background-color: rgb(156, 208, 93);\n"
"color: rgb(255, 255, 255);")
        self.addbutton.setObjectName("addbutton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(400, 220, 61, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(470, 290, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_11.raise_()
        self.label_10.raise_()
        self.label_7.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.soldinput.raise_()
        self.amountinput.raise_()
        self.billedinput.raise_()
        self.backbutton.raise_()
        self.donebutton.raise_()
        self.methodinput.raise_()
        self.addbutton.raise_()
        self.label_2.raise_()
        self.label_3.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setToolTip(_translate("Dialog", "<html><head/><body><p>gtgtg</p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">Add a Sale</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p>Sold Product:</p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p>Amount:</p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p>Was it billed?:</p></body></html>"))
        self.backbutton.setText(_translate("Dialog", "Back to Menu"))
        self.donebutton.setText(_translate("Dialog", "Done"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p>Method:</p></body></html>"))
        self.addbutton.setText(_translate("Dialog", "+"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">$</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "ENTER MORE "))
