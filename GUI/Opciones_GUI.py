import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from verDatos_GUI import Dat
from Datos import Examenes
import pandas as pd

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
        self.revisar.setText("por favor ver consola de comandos para realizar examenes")
        try:
            RegistrosPo = pd.read_csv('CSV_PROYECTO.csv', encoding='windows-1252')
            RegistrosP = RegistrosPo.set_index("Correo")
            estad_o = pd.read_csv('ESTADISTICAS.csv', encoding='windows-1252')
            estad = estad_o.set_index('Correo')

        except Exception as e:
            print("error en archivos:  ", e)
        correo = self.textBuscar.text()
        ex = Examenes()
        try:
            ex.PenT(correo,estad,RegistrosP)
        except Exception as e:
            print("error en examenes ", e)

    def rE(self):
        self.revisar.setText("por favor ver consola de comandos para realizar examenes")
        try:
            RegistrosPo = pd.read_csv('CSV_PROYECTO.csv', encoding= 'windows-1252')
            RegistrosP = RegistrosPo.set_index("Correo")
            estad_o = pd.read_csv('ESTADISTICAS.csv', encoding = 'windows-1252')
            estad = estad_o.set_index('Correo')

        except Exception as e:
            print("error en archivos:  ", e)
        correo = self.textBuscar.text()
        ex= Examenes()
        try:
            ex.obTok(correo,estad,RegistrosP)
        except Exception as e:
            print("error en examenes ", e)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = Opc()
    GUI.show()
    sys.exit(app.exec_())