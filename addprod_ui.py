# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\User\Documents\PharmacyFinal\PharmacyProjectFF\addprod.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(620, 480)
        Dialog.setStyleSheet("background-color: rgb(23, 136, 211);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 10, 391, 91))
        self.label.setStyleSheet("font: 75 24pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(48, 100, 141, 41))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.nameinput = QtWidgets.QLineEdit(Dialog)
        self.nameinput.setGeometry(QtCore.QRect(150, 100, 111, 31))
        self.nameinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nameinput.setObjectName("nameinput")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(298, 90, 171, 41))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.stockinput = QtWidgets.QLineEdit(Dialog)
        self.stockinput.setGeometry(QtCore.QRect(150, 140, 111, 31))
        self.stockinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stockinput.setObjectName("stockinput")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(308, 220, 151, 41))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.taxinput = QtWidgets.QLineEdit(Dialog)
        self.taxinput.setGeometry(QtCore.QRect(150, 180, 111, 31))
        self.taxinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.taxinput.setObjectName("taxinput")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(48, 140, 171, 41))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";")
        self.label_7.setObjectName("label_7")
        self.presinput = QtWidgets.QLineEdit(Dialog)
        self.presinput.setGeometry(QtCore.QRect(468, 100, 113, 31))
        self.presinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.presinput.setObjectName("presinput")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(308, 130, 151, 41))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";")
        self.label_8.setObjectName("label_8")
        self.costinput = QtWidgets.QLineEdit(Dialog)
        self.costinput.setGeometry(QtCore.QRect(468, 140, 113, 31))
        self.costinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.costinput.setObjectName("costinput")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(308, 170, 151, 41))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        self.saleinput = QtWidgets.QLineEdit(Dialog)
        self.saleinput.setGeometry(QtCore.QRect(468, 180, 113, 31))
        self.saleinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.saleinput.setObjectName("saleinput")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(48, 180, 141, 41))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";")
        self.label_10.setObjectName("label_10")
        self.labinput = QtWidgets.QLineEdit(Dialog)
        self.labinput.setGeometry(QtCore.QRect(468, 220, 113, 31))
        self.labinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labinput.setObjectName("labinput")
        self.backbutton = QtWidgets.QPushButton(Dialog)
        self.backbutton.setGeometry(QtCore.QRect(480, 350, 93, 28))
        self.backbutton.setStyleSheet("background-color: rgb(167, 168, 167);\n"
"background-color: rgb(156, 208, 93);\n"
"color: rgb(255, 255, 255);")
        self.backbutton.setObjectName("backbutton")
        self.donebutton = QtWidgets.QPushButton(Dialog)
        self.donebutton.setGeometry(QtCore.QRect(480, 300, 93, 28))
        self.donebutton.setStyleSheet("background-color: rgb(156, 208, 93);\n"
"color: rgb(255, 255, 255);")
        self.donebutton.setObjectName("donebutton")
        self.expdate = QtWidgets.QLineEdit(Dialog)
        self.expdate.setGeometry(QtCore.QRect(150, 220, 111, 31))
        self.expdate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.expdate.setObjectName("expdate")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(8, 220, 181, 41))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";")
        self.label_11.setObjectName("label_11")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(110, 280, 341, 181))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_11.raise_()
        self.label_10.raise_()
        self.label_7.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.nameinput.raise_()
        self.label_5.raise_()
        self.stockinput.raise_()
        self.label_6.raise_()
        self.taxinput.raise_()
        self.presinput.raise_()
        self.label_8.raise_()
        self.costinput.raise_()
        self.label_9.raise_()
        self.saleinput.raise_()
        self.labinput.raise_()
        self.backbutton.raise_()
        self.donebutton.raise_()
        self.expdate.raise_()
        self.calendarWidget.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Add a Product</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p>Name:</p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p>Presentation: </p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p>Laboratory:</p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p>Stock:</p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p>Cost Value:</p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p>Sale Value:</p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p>TAX:</p></body></html>"))
        self.backbutton.setText(_translate("Dialog", "Back to Menu"))
        self.donebutton.setText(_translate("Dialog", "Done"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p>Exp Date:</p></body></html>"))
