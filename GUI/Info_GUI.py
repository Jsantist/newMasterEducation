import sys
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog

class Info(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("Info.ui",self)
        self.regresar.clicked.connect(self.close)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = Info()
    GUI.show()
    sys.exit(app.exec_())