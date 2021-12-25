from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui
from AddNewPosition_ui import Ui_AddNewPosition
import sys
from PyQt5.QtGui import QPixmap
import openpyxl
import os
from openpyxl.worksheet import worksheet

photo="*"

class AddNewPosition(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(AddNewPosition, self).__init__(parent)
        self.ui =Ui_AddNewPosition()
        self.ui.setupUi(self)

        self.ui.KodlineEdit.setValidator(QtGui.QIntValidator())
        self.ui.PricelineEdit.setValidator(QtGui.QIntValidator())

        self.ui.ProizvodcomboBox.addItem("*")
        self.ui.ProizvodcomboBox.addItem("Outventure")
        self.ui.ProizvodcomboBox.addItem("Columbia")
        self.ui.ProizvodcomboBox.addItem("Jack Wolfskin")
        self.ui.ProizvodcomboBox.addItem("ASOS DESIGN")
        self.ui.ProizvodcomboBox.addItem("The North Face")
        self.ui.ProizvodcomboBox.addItem("Levi's")

        self.ui.PostavcomboBox.addItem("*")
        self.ui.PostavcomboBox.addItem("Спортмастер")
        self.ui.PostavcomboBox.addItem("ASOS")
        self.ui.PostavcomboBox.addItem("Lamoda")

        self.ui.SizecomboBox.addItem("*")
        self.ui.SizecomboBox.addItem("XS")
        self.ui.SizecomboBox.addItem("S")
        self.ui.SizecomboBox.addItem("M")
        self.ui.SizecomboBox.addItem("L")
        self.ui.SizecomboBox.addItem("XL")
        self.ui.SizecomboBox.addItem("XXL")

        self.ui.PolcomboBox.addItem("*")
        self.ui.PolcomboBox.addItem("М")
        self.ui.PolcomboBox.addItem("Ж")

        self.ui.AddImageButton.clicked.connect(self.openFileNameDialog)
        self.ui.AddButton.clicked.connect(self.add)

        
        
    
    def openFileNameDialog(self):
        global photo
        photo, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Images(*.png *.jpg *.jpeg)")
        file_name, file_extension = os.path.splitext(photo)
        if file_extension == ".png" or file_extension == ".jpg" or file_extension == ".jpeg":
            self.ui.Image.setPixmap(
                    QPixmap(photo))
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Ошибка!")
            msg.setText("Картинка выбрана не верно!")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.exec_()
     
    def add(self):
        if photo=="" or self.ui.SizecomboBox.currentText()=="*" or self.ui.NametextEdit.toPlainText()=="" or self.ui.KodlineEdit.text()=="" or self.ui.PricelineEdit.text()=="":
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Ошибка!")
            msg.setText("Заполните поля под * и добавьте картинку!")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.exec_()
        else:
            filename="baza.xlsx"
            book = openpyxl.load_workbook(filename=filename)
            sheet :worksheet= book.worksheets[0]
            sheet.insert_rows(2)
            sheet["A2"].value=str(self.ui.NametextEdit.toPlainText())
            sheet["B2"].value=str(self.ui.KodlineEdit.text())
            sheet["C2"].value=str(self.ui.SizecomboBox.currentText())
            sheet["D2"].value=str(self.ui.ProizvodcomboBox.currentText())
            sheet["E2"].value=str(self.ui.PostavcomboBox.currentText())
            sheet["F2"].value=str(self.ui.PricelineEdit.text())
            sheet["G2"].value=str(self.ui.NumberspinBox.value())
            sheet["H2"].value=str(self.ui.dateEdit.date())
            sheet["I2"].value=str(photo)
            sheet["J2"].value=str(self.ui.PolcomboBox.currentText())
            book.save(filename)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Успешно")
            msg.setText("Товар успешно добавлен")
            msg.exec_()
            

        
   

def showAddNewPosition(app):
    application = AddNewPosition(app)
    application.show()
    
