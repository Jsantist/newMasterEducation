import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog


class Canj(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("canjeoTok.ui", self)

    #def canjeo(self):



if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = Canj()
    GUI.show()
    sys.exit(app.exec_())