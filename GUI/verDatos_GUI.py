import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
import pandas as pd


class Dat(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("verDatos.ui", self)
        self.butSalir.clicked.connect(self.close)
        self.butBuscar.clicked.connect(self.verData)
    def verData(self):
        correo = self.textBuscar.text()
        try:
            RegistrosPo = pd.read_csv('CSV_PROYECTO.csv', encoding= 'windows-1252')
            RegistrosP = RegistrosPo.set_index("Correo")

        except Exception as e:
            print("error en archivos:  ", e)

        user = str(RegistrosP.loc[correo]['Usuario'])
        nombre = str(RegistrosP.loc[correo]['Nombre'])
        apellido = str(RegistrosP.loc[correo]['Apellido'])
        id = str(RegistrosP.loc[correo]['ID'])
        puntos = str(RegistrosP.loc[correo]['puntE'])
        tokens = str(RegistrosP.loc[correo]['Tokens'])
        estadoE = str(RegistrosP.loc[correo]['Estado'])

        try:
            self.laCorreo.setText(correo)
            self.laUser.setText(user)
            self.laNombre.setText(nombre)
            self.laAp.setText(apellido)
            self.laId.setText(id)
            self.laPE.setText(puntos)
            self.laTokens.setText(tokens)
            self.laEstado.setText(estadoE)
        except Exception as e:
            print("error en labels ",e)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = Dat()
    GUI.show()
    sys.exit(app.exec_())