import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
import pandas as pd
from Datos import Estadisticas


class Est(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("DatEstudiante.ui", self)
        self.butBuscar.clicked.connect(self.viewData)
        self.butSalir.clicked.connect(self.close)
    def viewData(self):
        correo = self.textBuscar.text()
        try:
            estad_o = pd.read_csv('ESTADISTICAS.csv', encoding = 'windows-1252')
            estad = estad_o.set_index('Correo')

        except Exception as e:
            print("error en archivos:  ", e)
        fun = Estadisticas()
        try:
            lista = fun.exUsuario(estad,correo)
            Er= str(lista[0])
            Ea= str(lista[1])
            ER= str(lista[2])
        except Exception as e:
            print("error en exUsuario",e)
        try:
            puntos = str(fun.puntUsuario(estad,correo))
        except Exception as e :
            print("error en puntUsuario ", e)

        try:
            self.laExRe.setText(Er)
            self.laExA.setText(Ea)
            self.laExR.setText(ER)
            self.laPA.setText(puntos)
        except Exception as e:
            print("error en labels", e)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = Est()
    GUI.show()
    sys.exit(app.exec_())