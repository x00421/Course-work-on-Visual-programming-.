from prodaga_ui import Ui_Prodaga
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui
import sys
from PyQt5.QtGui import QPixmap
from openpyxl.worksheet import worksheet
import openpyxl

class Prodaga(QtWidgets.QMainWindow):
        def __init__(self, parent=None):
                super(Prodaga, self).__init__(parent)
                self.ui = Ui_Prodaga()
                self.ui.setupUi(self)

        

def showprodaga(app):
    application = Prodaga(app)
    application.show()