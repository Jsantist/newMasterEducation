import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from verDatos_GUI import Dat

class Opc(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("Opciones.ui",self)
    def Vd(self):
        self.verD= Dat()
        self.verD.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = Opc()
    GUI.show()
    sys.exit(app.exec_())