from PyQt5 import QtWidgets
from otchet_ui import Ui_Otchet
import sys
from PyQt5.QtGui import QPixmap
import openpyxl
from openpyxl.worksheet import worksheet

class Otchetwindow(QtWidgets.QMainWindow):
        def __init__(self, parent=None):
                super(Otchetwindow, self).__init__(parent)
                self.ui = Ui_Otchet()
                self.ui.setupUi(self)
                self.result()
                self.ui.SortButton.clicked.connect(self.result)
        
        def result(self):
            book = openpyxl.open("baza.xlsx")
            sheet = book.worksheets[1]
            prodag=0
            vozvrat=0
            brak=0
            sum=0
            dateot=self.ui.dateEdit.date().toString("yyyy,M,d")
            datedo=self.ui.dateEdit_2.date().toString("yyyy,M,d")
            for i in range(2,sheet.max_row+1):
                date= sheet['H'+str(i)].value
                if dateot<=date and datedo>=date:
                    if sheet['K'+str(i)].value=="В":
                        vozvrat+=1
                    if sheet['K'+str(i)].value=="П":
                        prodag+=1
                    if sheet['K'+str(i)].value=="Б":
                        brak+=1
                    sum+=int(sheet['F'+str(i)].value)

            self.ui.SellNumber.setText(str(prodag))
            self.ui.VozvratNumber.setText(str(vozvrat))
            self.ui.BrakNumber.setText(str(brak))
            self.ui.SummNumber.setText(str(sum))

      


                


            
        
       


def showOtchet(app):
    application = Otchetwindow(app)
    application.show()