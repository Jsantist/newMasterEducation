import sys
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from Registro_GUI import Registrar
from Inicio_GUI import Inicio
from Info_GUI import Info

class Ingreso(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("Inicio.ui",self)
        self.registro.clicked.connect(self.butReg)
        self.inicioSesion.clicked.connect(self.butIn)
        self.info.clicked.connect(self.butInfo)

    def butReg(self):
        self.reg= Registrar()
        self.reg.show()



    def butIn(self):
        self.ini= Inicio()
        self.ini.show()



    def butInfo(self):
        self.info=Info()
        self.info.show()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = Ingreso()
    GUI.show()
    sys.exit(app.exec_())