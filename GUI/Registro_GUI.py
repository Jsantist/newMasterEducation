import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from Datos import Archivos

import pandas as pd

class Registrar(QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("Registro.ui",self)

        self.butRegistro.clicked.connect(self.newData)
        self.butSalir.clicked.connect(self.close)

    def newData(self):
        global RegistrosPo, estad
        user = self.User.text()
        correo = self.correo.text()
        nombre = self.nombre.text()
        apellido = self.apellido.text()
        ID = self.ID.text()
        grado = self.grado.text()
        contra = self.contra.text()
        tipo= self.comboBox.currentText()

        arch = Archivos()

        try:
            RegistrosPo = pd.read_csv('CSV_PROYECTO.csv', encoding= 'windows-1252')
            RegistrosP = RegistrosPo.set_index("Correo")
            estad_o = pd.read_csv('ESTADISTICAS.csv', encoding = 'windows-1252')
            estad = estad_o.set_index('Correo')

        except Exception as e:
            print("error en archivos:  ", e)


        if not arch.insert(correo, user, contra, nombre, apellido, ID, grado, tipo, estad, RegistrosP, RegistrosPo):
            self.veri.setText("El correo ingresado ya existe, por favor intente con uno nuevo")
        else:
            self.close()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = Registrar()
    GUI.show()
    sys.exit(app.exec_())