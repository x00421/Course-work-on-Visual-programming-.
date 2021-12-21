from PyQt5 import QtWidgets
from katalog_ui import Ui_katalog
import sys
class katalogwindow(QtWidgets.QWidget):
     def __init__(self):
        super(katalogwindow, self).__init__()
        self.ui = Ui_katalog()
        self.ui.setupUi(self)

app = QtWidgets.QApplication([])
application = katalogwindow()
application.show()

sys.exit(app.exec())