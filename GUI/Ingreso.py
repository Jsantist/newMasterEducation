import sys
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from Registro_GUI import Registrar

class Registrar(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("Registro.ui",self)


class Ingreso(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("Inicio.ui",self)
        self.registro.clicked.connect(self.butReg)

    def butReg(self):
        self.ventana= Registrar()
        self.ventana.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = Ingreso()
    GUI.show()
    sys.exit(app.exec_())