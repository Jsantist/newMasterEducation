import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog


class Dat(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("Opciones.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = Dat()
    GUI.show()
    sys.exit(app.exec_())