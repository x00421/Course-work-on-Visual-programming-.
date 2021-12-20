from PyQt5 import QtWidgets
from main_ui import Ui_Main  # импорт нашего сгенерированного файла
import sys
import openpyxl



class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        # Отвечает за выбор размера в поиске
        self.ui.SizecomboBox.addItem("XS")
        self.ui.SizecomboBox.addItem("S")
        self.ui.SizecomboBox.addItem("M")
        self.ui.SizecomboBox.addItem("L")
        self.ui.SizecomboBox.addItem("XL")

        # Отвечает за Отображение колонок
        self.ui.MaintableWidget.setColumnCount(4)
        self.ui.MaintableWidget.setColumnWidth(0, 450)
        self.ui.MaintableWidget.setColumnWidth(1, 60)
        self.ui.MaintableWidget.setColumnWidth(2, 130)
        self.ui.MaintableWidget.setColumnWidth(3, 100)
        self.ui.MaintableWidget.setHorizontalHeaderLabels(
            ('Название', 'Размер', 'Цена', 'Остаток')
        )
        #Функция отображения таблицы без фильтра
        self.mainloaddata()
        self.ui.AllButton.clicked.connect(self.mainloaddata)
        #Функция отображения таблицы для мужчин
        self.ui.MenButton.clicked.connect(self.mainloaddata_man)
        #Функция отображения таблицы для женщин
        self.ui.WomenButton.clicked.connect(self.mainloaddata_women)
        

    def mainloaddata(self):#Функция отображения таблицы без фильтра
        book=openpyxl.open("baza.xlsx")
        sheet=book.worksheets[0]
       
        row = 0
        self.ui.MaintableWidget.setRowCount(sheet.max_row-1)

        for i in range(2,sheet.max_row+1):
            name=sheet['A'+str(i)].value
            size=sheet["C"+str(i)].value
            price=sheet["F"+str(i)].value
            number=sheet["G"+str(i)].value
            self.ui.MaintableWidget.setItem(
                row, 0, QtWidgets.QTableWidgetItem(str(name)))
            self.ui.MaintableWidget.setItem(
                row, 1, QtWidgets.QTableWidgetItem(str(size)))
            self.ui.MaintableWidget.setItem(
                row, 2, QtWidgets.QTableWidgetItem(str(price)))
            self.ui.MaintableWidget.setItem(
                row, 3, QtWidgets.QTableWidgetItem(str(number)))
            row = row+1
    

    def mainloaddata_man(self):#Функция отображения таблицы для мужчин
        book=openpyxl.open("baza.xlsx")
        sheet=book.worksheets[1]
       
        row = 0
        self.ui.MaintableWidget.setRowCount(sheet.max_row-1)

        for i in range(2,sheet.max_row+1):
            name=sheet['A'+str(i)].value
            size=sheet["C"+str(i)].value
            price=sheet["F"+str(i)].value
            number=sheet["G"+str(i)].value
            self.ui.MaintableWidget.setItem(
                row, 0, QtWidgets.QTableWidgetItem(str(name)))
            self.ui.MaintableWidget.setItem(
                row, 1, QtWidgets.QTableWidgetItem(str(size)))
            self.ui.MaintableWidget.setItem(
                row, 2, QtWidgets.QTableWidgetItem(str(price)))
            self.ui.MaintableWidget.setItem(
                row, 3, QtWidgets.QTableWidgetItem(str(number)))
            row = row+1
    

    def mainloaddata_women(self):#Функция отображения таблицы для Женщин
        book=openpyxl.open("baza.xlsx")
        sheet=book.worksheets[2]
       
        row = 0
        self.ui.MaintableWidget.setRowCount(sheet.max_row-1)

        for i in range(2,sheet.max_row+1):
            name=sheet['A'+str(i)].value
            size=sheet["C"+str(i)].value
            price=sheet["F"+str(i)].value
            number=sheet["G"+str(i)].value
            self.ui.MaintableWidget.setItem(
                row, 0, QtWidgets.QTableWidgetItem(str(name)))
            self.ui.MaintableWidget.setItem(
                row, 1, QtWidgets.QTableWidgetItem(str(size)))
            self.ui.MaintableWidget.setItem(
                row, 2, QtWidgets.QTableWidgetItem(str(price)))
            self.ui.MaintableWidget.setItem(
                row, 3, QtWidgets.QTableWidgetItem(str(number)))
            row = row+1

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
