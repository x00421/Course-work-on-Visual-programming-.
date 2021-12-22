from PyQt5 import QtWidgets
from main_ui import Ui_Main  # импорт нашего сгенерированного файла
from katalog import show
import sys
import openpyxl
import time

exellist = 0


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        # Отвечает за выбор размера в поиске
        self.ui.SizecomboBox.addItem("*")
        self.ui.SizecomboBox.addItem("XS")
        self.ui.SizecomboBox.addItem("S")
        self.ui.SizecomboBox.addItem("M")
        self.ui.SizecomboBox.addItem("L")
        self.ui.SizecomboBox.addItem("XL")
        self.ui.SizecomboBox.addItem("XXL")

        # Отвечает за Отображение колонок
        self.ui.MaintableWidget.setColumnCount(5)
        self.ui.MaintableWidget.setColumnWidth(0, 450)
        self.ui.MaintableWidget.setColumnWidth(1, 60)
        self.ui.MaintableWidget.setColumnWidth(2, 100)
        self.ui.MaintableWidget.setColumnWidth(3, 80)
        self.ui.MaintableWidget.setColumnWidth(4, 45)
        self.ui.MaintableWidget.setHorizontalHeaderLabels(
            ('Название', 'Размер', 'Цена', 'Остаток',"*")
        )
        # Функция отображения таблицы без фильтра
        self.mainloaddata()
        self.ui.AllButton.clicked.connect(self.mainloaddata)
        # Функция отображения таблицы для мужчин
        self.ui.MenButton.clicked.connect(self.mainloaddata_man)
        # Функция отображения таблицы для женщин
        self.ui.WomenButton.clicked.connect(self.mainloaddata_women)
        # Функция поиска
        self.ui.PoiskButton.clicked.connect(self.poisk)


        self.ui.KatalogButton.clicked.connect(lambda: show(self))

        self.ui.TovarButton.clicked.connect(self.getData)#Получение данных из таблицы приложения
        
        

        
        
    
        

    def mainloaddata(self):  # Функция отображения таблицы без фильтра
        global exellist
        exellist = 0
        book = openpyxl.open("baza.xlsx")
        sheet = book.worksheets[0]

        row = 0
        self.ui.MaintableWidget.setRowCount(sheet.max_row-2)

        for i in range(2, sheet.max_row+1):
            name = sheet['A'+str(i)].value
            size = sheet["C"+str(i)].value
            price = sheet["F"+str(i)].value
            number = sheet["G"+str(i)].value
            self.ui.MaintableWidget.setItem(
                row, 0, QtWidgets.QTableWidgetItem(str(name)))
            self.ui.MaintableWidget.setItem(
                row, 1, QtWidgets.QTableWidgetItem(str(size)))
            self.ui.MaintableWidget.setItem(
                row, 2, QtWidgets.QTableWidgetItem(str(price)))
            self.ui.MaintableWidget.setItem(
                row, 3, QtWidgets.QTableWidgetItem(str(number)))
                
            row += 1

    def mainloaddata_man(self):  # Функция отображения таблицы для мужчин
        global exellist
        exellist = 1
        book = openpyxl.open("baza.xlsx")
        sheet = book.worksheets[1]

        row = 0
        self.ui.MaintableWidget.setRowCount(sheet.max_row-1)

        for i in range(2, sheet.max_row+1):
            name = sheet['A'+str(i)].value
            size = sheet["C"+str(i)].value
            price = sheet["F"+str(i)].value
            number = sheet["G"+str(i)].value
            self.ui.MaintableWidget.setItem(
                row, 0, QtWidgets.QTableWidgetItem(str(name)))
            self.ui.MaintableWidget.setItem(
                row, 1, QtWidgets.QTableWidgetItem(str(size)))
            self.ui.MaintableWidget.setItem(
                row, 2, QtWidgets.QTableWidgetItem(str(price)))
            self.ui.MaintableWidget.setItem(
                row, 3, QtWidgets.QTableWidgetItem(str(number)))
            row = row+1

    def mainloaddata_women(self):  # Функция отображения таблицы для Женщин
        book = openpyxl.open("baza.xlsx")
        sheet = book.worksheets[2]
        global exellist
        exellist = 2

        row = 0
        self.ui.MaintableWidget.setRowCount(sheet.max_row-1)

        for i in range(2, sheet.max_row+1):
            name = sheet['A'+str(i)].value
            size = sheet["C"+str(i)].value
            price = sheet["F"+str(i)].value
            number = sheet["G"+str(i)].value
            self.ui.MaintableWidget.setItem(
                row, 0, QtWidgets.QTableWidgetItem(str(name)))
            self.ui.MaintableWidget.setItem(
                row, 1, QtWidgets.QTableWidgetItem(str(size)))
            self.ui.MaintableWidget.setItem(
                row, 2, QtWidgets.QTableWidgetItem(str(price)))
            self.ui.MaintableWidget.setItem(
                row, 3, QtWidgets.QTableWidgetItem(str(number)))
            row = row+1

    def poisk(self):
        name_p = self.ui.NameEdit.toPlainText()  # Получаем текст из строкиввода
        size_p = self.ui.SizecomboBox.currentText()  # Получаем текст из комбобокса
        minprice = self.ui.OtpriceTextEdit.toPlainText()
        maxprice = self.ui.DopriceTextEdit.toPlainText()

        if name_p == "":
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Ошибка!")
            msg.setText("Введите название!")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.exec_()
        else:
            if size_p == "*" and minprice == "" and maxprice == "":
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Ошибка!")
                msg.setText("Введите стоимость или размер!")
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.exec_()

            else:
                book = openpyxl.open("baza.xlsx")
                sheet = book.worksheets[exellist]
                row = 0
                self.ui.MaintableWidget.setRowCount(sheet.max_row-1)
                self.ui.MaintableWidget.clear()
                self.ui.MaintableWidget.setHorizontalHeaderLabels(
                    ('Название', 'Размер', 'Цена', 'Остаток')
                )
                for i in range(2, sheet.max_row):
                    name = sheet['A'+str(i)].value
                    size = sheet["C"+str(i)].value
                    price = sheet["F"+str(i)].value
                    number = sheet["G"+str(i)].value

                    if size_p == "*":#Если пустое поле размера
                        if maxprice == "":
                            maxprice = 100000000
                        if minprice == "":
                            minprice = 0
                        if (name_p in name) and (int(minprice) <= int(price) and int(maxprice) >= int(price)):
                            self.ui.MaintableWidget.setItem(
                                row, 0, QtWidgets.QTableWidgetItem(str(name)))
                            self.ui.MaintableWidget.setItem(
                                row, 1, QtWidgets.QTableWidgetItem(str(size)))
                            self.ui.MaintableWidget.setItem(
                                row, 2, QtWidgets.QTableWidgetItem(str(price)))
                            self.ui.MaintableWidget.setItem(
                                row, 3, QtWidgets.QTableWidgetItem(str(number)))
                            row = row+1
                    else:#Если поле размера не пустое 
                        if maxprice == "" and minprice == "":#Если поле размера не пустое а цены пустые
                            if (name_p in name) and size == size_p:
                                self.ui.MaintableWidget.setItem(
                                    row, 0, QtWidgets.QTableWidgetItem(str(name)))
                                self.ui.MaintableWidget.setItem(
                                    row, 1, QtWidgets.QTableWidgetItem(str(size)))
                                self.ui.MaintableWidget.setItem(
                                    row, 2, QtWidgets.QTableWidgetItem(str(price)))
                                self.ui.MaintableWidget.setItem(
                                    row, 3, QtWidgets.QTableWidgetItem(str(number)))
                                row = row+1
                        else:
                            if maxprice == "":
                                maxprice = 100000000
                            if minprice == "":
                                minprice = 0
                            if (name_p in name) and (size == size_p) and (int(minprice) <= int(price) and int(maxprice) >= int(price)):
                                self.ui.MaintableWidget.setItem(
                                    row, 0, QtWidgets.QTableWidgetItem(str(name)))
                                self.ui.MaintableWidget.setItem(
                                    row, 1, QtWidgets.QTableWidgetItem(str(size)))
                                self.ui.MaintableWidget.setItem(
                                    row, 2, QtWidgets.QTableWidgetItem(str(price)))
                                self.ui.MaintableWidget.setItem(
                                    row, 3, QtWidgets.QTableWidgetItem(str(number)))
                                row = row+1

    def getData(self):#Функция получения информации из таблицы
        rows = self.ui.MaintableWidget.rowCount()
        cols = self.ui.MaintableWidget.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                try:
                    tmp.append(self.ui.MaintableWidget.item(row,col).text())
                except:
                    tmp.append('No data')
            data.append(tmp)
        for i in data: print(i)
                        


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
