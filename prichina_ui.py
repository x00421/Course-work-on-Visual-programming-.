# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prichina.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Prichina(object):
    def setupUi(self, Prichina):
        Prichina.setObjectName("Prichina")
        Prichina.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        Prichina.setFont(font)
        self.label = QtWidgets.QLabel(Prichina)
        self.label.setGeometry(QtCore.QRect(30, 20, 341, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Prichina)
        self.textEdit.setGeometry(QtCore.QRect(30, 60, 341, 181))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Prichina)
        self.pushButton.setGeometry(QtCore.QRect(160, 250, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Prichina)
        QtCore.QMetaObject.connectSlotsByName(Prichina)

    def retranslateUi(self, Prichina):
        _translate = QtCore.QCoreApplication.translate
        Prichina.setWindowTitle(_translate("Prichina", "Form"))
        self.label.setText(_translate("Prichina", "Причина брака"))
        self.pushButton.setText(_translate("Prichina", "Сохранить"))