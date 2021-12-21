from PyQt5 import QtWidgets
from katalog_ui import Ui_katalog
import sys
class Katalogwindow(QtWidgets.QMainWindow):
       def __init__(self,parent=None):
        super(Katalogwindow, self).__init__(parent)
        self.ui = Ui_katalog()
        self.ui.setupUi(self)

def show(app):
        
        application = Katalogwindow(app)
        application.show()

      