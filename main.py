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
        #Функция отображения таблицы
        self.mainloaddata()

    def mainloaddata(self):
        clouses = [
            {"name": "Синяя футболка", "size": "S",
                "price": "New York", "number": "10"},
            {"name": "Красная футболка", "size": "S",
                "price": "New York", "number": "10"},
            {"name": "Синяя футболка", "size": "S",
                "price": "New York", "number": "10"},
            {"name": "Красная футболка", "size": "S",
                "price": "New York", "number": "10"},
            {"name": "Синяя футболка", "size": "S",
                "price": "New York", "number": "10"},
            {"name": "Красная футболка", "size": "S",
                "price": "New York", "number": "10"},
            {"name": "Синяя футболка", "size": "S",
                "price": "New York", "number": "10"},
            {"name": "Красная футболка", "size": "S",
                "price": "New York", "number": "10"},
            {"name": "Синяя футболка", "size": "S",
                "price": "New York", "number": "10"},
            {"name": "Красная футболка", "size": "S",
                "price": "New York", "number": "10"},
            {"name": "Синяя футболка", "size": "S",
                "price": "New York", "number": "10"},
            {"name": "Красная футболка", "size": "S",
                "price": "New York", "number": "10"},
            {"name": "Синяя футболка", "size": "S",
                "price": "New York", "number": "10"},
            {"name": "Красная футболка", "size": "S",
                "price": "New York", "number": "10"},

        ]
        row = 0
        self.ui.MaintableWidget.setRowCount(len(clouses))

        for person in clouses:
            self.ui.MaintableWidget.setItem(
                row, 0, QtWidgets.QTableWidgetItem(person["name"]))
            self.ui.MaintableWidget.setItem(
                row, 1, QtWidgets.QTableWidgetItem(person["size"]))
            self.ui.MaintableWidget.setItem(
                row, 2, QtWidgets.QTableWidgetItem(person["price"]))
            self.ui.MaintableWidget.setItem(
                row, 3, QtWidgets.QTableWidgetItem(person["number"]))
            row = row+1


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
