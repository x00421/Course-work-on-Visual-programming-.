# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'otchet.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Otchet(object):
    def setupUi(self, Otchet):
        Otchet.setObjectName("Otchet")
        Otchet.resize(720, 480)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        Otchet.setFont(font)
        self.label = QtWidgets.QLabel(Otchet)
        self.label.setGeometry(QtCore.QRect(100, 100, 171, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Otchet)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 171, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Otchet)
        self.label_3.setGeometry(QtCore.QRect(100, 210, 191, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Otchet)
        self.label_4.setGeometry(QtCore.QRect(270, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Otchet)
        self.label_5.setGeometry(QtCore.QRect(280, 330, 171, 21))
        self.label_5.setObjectName("label_5")
        self.dateEdit = QtWidgets.QDateEdit(Otchet)
        self.dateEdit.setGeometry(QtCore.QRect(190, 390, 110, 22))
        self.dateEdit.setDate(QtCore.QDate(2021, 12, 27))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(Otchet)
        self.dateEdit_2.setGeometry(QtCore.QRect(360, 390, 110, 22))
        self.dateEdit_2.setDate(QtCore.QDate(2021, 12, 27))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.SellNumber = QtWidgets.QLabel(Otchet)
        self.SellNumber.setGeometry(QtCore.QRect(280, 110, 151, 16))
        self.SellNumber.setText("")
        self.SellNumber.setObjectName("SellNumber")
        self.VozvratNumber = QtWidgets.QLabel(Otchet)
        self.VozvratNumber.setGeometry(QtCore.QRect(280, 150, 151, 16))
        self.VozvratNumber.setText("")
        self.VozvratNumber.setObjectName("VozvratNumber")
        self.BrakNumber = QtWidgets.QLabel(Otchet)
        self.BrakNumber.setGeometry(QtCore.QRect(300, 210, 151, 16))
        self.BrakNumber.setText("")
        self.BrakNumber.setObjectName("BrakNumber")
        self.label_6 = QtWidgets.QLabel(Otchet)
        self.label_6.setGeometry(QtCore.QRect(250, 280, 101, 21))
        self.label_6.setObjectName("label_6")
        self.SummNumber = QtWidgets.QLabel(Otchet)
        self.SummNumber.setGeometry(QtCore.QRect(330, 280, 121, 16))
        self.SummNumber.setText("")
        self.SummNumber.setObjectName("SummNumber")
        self.SortButton = QtWidgets.QPushButton(Otchet)
        self.SortButton.setGeometry(QtCore.QRect(260, 430, 131, 41))
        self.SortButton.setObjectName("SortButton")

        self.retranslateUi(Otchet)
        QtCore.QMetaObject.connectSlotsByName(Otchet)

    def retranslateUi(self, Otchet):
        _translate = QtCore.QCoreApplication.translate
        Otchet.setWindowTitle(_translate("Otchet", "Form"))
        self.label.setText(_translate("Otchet", "Продано:"))
        self.label_2.setText(_translate("Otchet", "Вернули:"))
        self.label_3.setText(_translate("Otchet", "Количество брака:"))
        self.label_4.setText(_translate("Otchet", "Отчёт"))
        self.label_5.setText(_translate("Otchet", "Период отчета:"))
        self.label_6.setText(_translate("Otchet", "Итог:"))
        self.SortButton.setText(_translate("Otchet", "Применить"))
