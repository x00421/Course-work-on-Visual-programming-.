from PyQt5 import QtWidgets
from katalog_ui import Ui_katalog
import sys
from PyQt5.QtGui import QPixmap
import openpyxl


class Katalogwindow(QtWidgets.QMainWindow):
        def __init__(self, parent=None):
                super(Katalogwindow, self).__init__(parent)
                self.ui = Ui_katalog()
                self.ui.setupUi(self)
                
                self.i = 2
                self.c=25
                self.katalog()

                self.ui.PrevButton.clicked.connect(self.next)
                self.ui.NextButton.clicked.connect(self.prev)


        def katalog(self):
                book = openpyxl.open("baza.xlsx")
                sheet = book.worksheets[0]
                self.c=sheet.max_row+1

                name = sheet['A'+str(self.i)].value
                photo = sheet['I'+str(self.i)].value
                price = sheet["F"+str(self.i)].value

                self.ui.textBrowser.setText(name)
                self.ui.label_2.setText("Цена: "+str(price))
                self.ui.Image.setPixmap(
                QPixmap(photo))
                
        def next(self):
                if self.i<self.c:
                        self.i += 1
                        self.katalog()
                else:
                        self.i = 2
                        self.katalog()
        def prev(self):
                if self.i>2:
                        self.i -= 1
                        self.katalog()
                else:
                        self.i = self.c
                        self.katalog()


        
                


def show(app):
    application = Katalogwindow(app)
    application.show()
