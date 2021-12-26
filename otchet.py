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
        
       


def showOtchet(app):
    application = Otchetwindow(app)
    application.show()