import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from verDatos_GUI import Dat
from canjTokens_GUI import Canj

class Opc(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("Opciones.ui",self)
        self.butVd.clicked.connect(self.Vd)
        self.butCt.clicked.connect(self.cT)
        self.butRe.clicked.connect(self.rE)
        self.butonSalir.clicked.connect(self.close)



    def Vd(self):
        self.verD= Dat()
        self.verD.show()
        self.close()
    def cT(self):
        self.cTok= Canj()
        self.Canj.show()
        self.close()
    def rE(self):
        print("pending")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = Opc()
    GUI.show()
    sys.exit(app.exec_())