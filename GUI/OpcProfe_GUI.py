import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from Datos import Estadisticas
from DatEst_GUI import Est
import pandas as pd


class Oprofe(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("OpcionesProfe.ui", self)
        self.butVd.clicked.connect(self.verDatos)
        self.butVm.clicked.connect(self.mediA)
        self.butVc.clicked.connect(self.cantEst)
        self.butGraf1.clicked.connect(self.grafEx)
        self.butGraf2.clicked.connect(self.grafPt)
        self.butonSalir.clicked.connect(self.close)

    def verDatos(self):
        self.est=Est()
        self.est.show()

    def mediA(self):
        global RegistrosPo
        try:
            RegistrosPo = pd.read_csv('CSV_PROYECTO.csv', encoding= 'windows-1252')
            RegistrosP = RegistrosPo.set_index("Correo")
            estad_o = pd.read_csv('ESTADISTICAS.csv', encoding = 'windows-1252')
            estad = estad_o.set_index('Correo')

        except Exception as e:
            print("error en archivos:  ", e)
        fun = Estadisticas()
        try:
            media = str(fun.media(RegistrosPo))

            self.revisar.setText("la media de punts totales obtenidos es : ")
            self.revisar_2.setText(media)
        except Exception as e:
            print("error en media: ", e)

    def cantEst(self):
        try:
            RegistrosPo = pd.read_csv('CSV_PROYECTO.csv', encoding= 'windows-1252')
            RegistrosP = RegistrosPo.set_index("Correo")
            estad_o = pd.read_csv('ESTADISTICAS.csv', encoding = 'windows-1252')
            estad = estad_o.set_index('Correo')

        except Exception as e:
            print("error en archivos:  ", e)
        fun = Estadisticas()
        try:
            suma = str(fun.contar(RegistrosPo))

            self.revisar.setText("la cantidad de usuarios registrados es : ")
            self.revisar_2.setText(suma)
        except Exception as e:
            print("error en media: ",e)

    def grafEx(self):
        try:
            RegistrosPo = pd.read_csv('CSV_PROYECTO.csv', encoding= 'windows-1252')
            RegistrosP = RegistrosPo.set_index("Correo")
            estad_o = pd.read_csv('ESTADISTICAS.csv', encoding = 'windows-1252')
            estad = estad_o.set_index('Correo')

        except Exception as e:
            print("error en archivos:  ", e)
        fun = Estadisticas()
        try:
            fun.graficaEx(estad_o)
        except Exception as e:
            print("error en grafica 1 :",e)

    def grafPt(self):
        try:
            RegistrosPo = pd.read_csv('CSV_PROYECTO.csv', encoding= 'windows-1252')
            RegistrosP = RegistrosPo.set_index("Correo")
            estad_o = pd.read_csv('ESTADISTICAS.csv', encoding = 'windows-1252')
            estad = estad_o.set_index('Correo')

        except Exception as e:
            print("error en archivos:  ", e)
        fun = Estadisticas()
        try:
            fun.graficaP(RegistrosPo)
        except Exception as e:
            print("error en grafica 1 :", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = Oprofe()
    GUI.show()
    sys.exit(app.exec_())