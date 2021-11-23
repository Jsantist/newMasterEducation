import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog

class Registrar(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("Registro.ui",self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = Registrar()
    GUI.show()
    sys.exit(app.exec_())
