# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\jared\OneDrive\Documentos\OBEJETOS\PharmacyProject\createsale.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(772, 480)
        Dialog.setStyleSheet("background-color: rgb(23, 136, 211);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 80, 261, 41))
        self.label.setStyleSheet("font: 75 24pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 220, 211, 41))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 170, 251, 41))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.soldinput = QtWidgets.QLineEdit(Dialog)
        self.soldinput.setGeometry(QtCore.QRect(410, 180, 231, 31))
        self.soldinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.soldinput.setObjectName("soldinput")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(100, 270, 261, 41))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.amountinput = QtWidgets.QLineEdit(Dialog)
        self.amountinput.setGeometry(QtCore.QRect(410, 230, 231, 31))
        self.amountinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.amountinput.setObjectName("amountinput")
        self.methodinput = QtWidgets.QLineEdit(Dialog)
        self.methodinput.setGeometry(QtCore.QRect(410, 330, 81, 31))
        self.methodinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.methodinput.setObjectName("methodinput")
        self.billedinput = QtWidgets.QLineEdit(Dialog)
        self.billedinput.setGeometry(QtCore.QRect(410, 280, 81, 31))
        self.billedinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.billedinput.setObjectName("billedinput")
        self.backbutton = QtWidgets.QPushButton(Dialog)
        self.backbutton.setGeometry(QtCore.QRect(500, 407, 101, 41))
        self.backbutton.setStyleSheet("background-color: rgb(167, 168, 167);\n"
"background-color: rgb(156, 208, 93);\n"
"color: rgb(255, 255, 255);")
        self.backbutton.setObjectName("backbutton")
        self.donebutton = QtWidgets.QPushButton(Dialog)
        self.donebutton.setGeometry(QtCore.QRect(260, 407, 111, 41))
        self.donebutton.setStyleSheet("background-color: rgb(156, 208, 93);\n"
"color: rgb(255, 255, 255);")
        self.donebutton.setObjectName("donebutton")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(100, 320, 281, 41))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Add a Sale</p></body></html>"))
        self.label_3.setText(_translate("Dialog", "Amount:"))
        self.label_4.setText(_translate("Dialog", "Sold products: "))
        self.label_6.setText(_translate("Dialog", "Was it billed?"))
        self.backbutton.setText(_translate("Dialog", "Back to Menu"))
        self.donebutton.setText(_translate("Dialog", "Done"))
        self.label_7.setText(_translate("Dialog", "Payment Method:"))