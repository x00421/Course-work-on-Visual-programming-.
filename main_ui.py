# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):        
        Main.setObjectName("Main")
        Main.resize(960, 540)
        Main.setAutoFillBackground(False)
        self.MenButton = QtWidgets.QPushButton(Main)
        self.MenButton.setGeometry(QtCore.QRect(370, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.MenButton.setFont(font)
        self.MenButton.setObjectName("MenButton")
        self.WomenButton = QtWidgets.QPushButton(Main)
        self.WomenButton.setGeometry(QtCore.QRect(550, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.WomenButton.setFont(font)
        self.WomenButton.setObjectName("WomenButton")
        self.NameEdit = QtWidgets.QTextEdit(Main)
        self.NameEdit.setGeometry(QtCore.QRect(10, 450, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.NameEdit.setFont(font)
        self.NameEdit.setObjectName("NameEdit")
        self.label = QtWidgets.QLabel(Main)
        self.label.setGeometry(QtCore.QRect(10, 420, 371, 21))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.SizecomboBox = QtWidgets.QComboBox(Main)
        self.SizecomboBox.setGeometry(QtCore.QRect(420, 450, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.SizecomboBox.setFont(font)
        self.SizecomboBox.setObjectName("SizecomboBox")
        self.label_2 = QtWidgets.QLabel(Main)
        self.label_2.setGeometry(QtCore.QRect(420, 420, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Main)
        self.label_3.setGeometry(QtCore.QRect(620, 420, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.OtpriceTextEdit = QtWidgets.QPlainTextEdit(Main)
        self.OtpriceTextEdit.setGeometry(QtCore.QRect(550, 450, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.OtpriceTextEdit.setFont(font)
        self.OtpriceTextEdit.setObjectName("OtpriceTextEdit")
        self.DopriceTextEdit = QtWidgets.QPlainTextEdit(Main)
        self.DopriceTextEdit.setGeometry(QtCore.QRect(690, 450, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DopriceTextEdit.setFont(font)
        self.DopriceTextEdit.setObjectName("DopriceTextEdit")
        self.PoiskButton = QtWidgets.QPushButton(Main)
        self.PoiskButton.setGeometry(QtCore.QRect(320, 490, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.PoiskButton.setFont(font)
        self.PoiskButton.setObjectName("PoiskButton")
        self.KatalogButton = QtWidgets.QPushButton(Main)
        self.KatalogButton.setGeometry(QtCore.QRect(830, 60, 111, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.KatalogButton.setFont(font)
        self.KatalogButton.setObjectName("KatalogButton")
        self.TovarButton = QtWidgets.QPushButton(Main)
        self.TovarButton.setGeometry(QtCore.QRect(810, 207, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TovarButton.setFont(font)
        self.TovarButton.setAutoExclusive(False)
        self.TovarButton.setObjectName("TovarButton")
        self.OtchetButton = QtWidgets.QPushButton(Main)
        self.OtchetButton.setGeometry(QtCore.QRect(830, 380, 111, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.OtchetButton.setFont(font)
        self.OtchetButton.setObjectName("OtchetButton")
        self.MaintableWidget = QtWidgets.QTableWidget(Main)
        self.MaintableWidget.setGeometry(QtCore.QRect(15, 61, 780, 350))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.MaintableWidget.setFont(font)
        self.MaintableWidget.setObjectName("MaintableWidget")
        self.MaintableWidget.setColumnCount(0)
        self.MaintableWidget.setRowCount(0)
        self.AllButton = QtWidgets.QPushButton(Main)
        self.AllButton.setGeometry(QtCore.QRect(40, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.AllButton.setFont(font)
        self.AllButton.setObjectName("AllButton")

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Chernololpakov"))
        self.MenButton.setText(_translate("Main", "Мужская"))
        self.WomenButton.setText(_translate("Main", "Женская"))
        self.label.setText(_translate("Main", "Название:"))
        self.label_2.setText(_translate("Main", "Размер:"))
        self.label_3.setText(_translate("Main", "Цена"))
        self.PoiskButton.setText(_translate("Main", "Поиск"))
        self.KatalogButton.setText(_translate("Main", "Каталог"))
        self.TovarButton.setText(_translate("Main", "Реализация"))
        self.OtchetButton.setText(_translate("Main", "Отчет"))
        self.AllButton.setText(_translate("Main", "Вся"))
