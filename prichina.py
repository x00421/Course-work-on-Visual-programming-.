from PyQt5 import QtWidgets
from prichina_ui import Ui_Prichina
import sys
from PyQt5.QtGui import QPixmap
import openpyxl
from openpyxl.worksheet import worksheet


class Prichinatwindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
                super(Prichinatwindow, self).__init__(parent)
                self.ui = Ui_Prichina()
                self.ui.setupUi(self)
                
def showPrichina(app):
    application = Prichinatwindow(app)
    application.show()