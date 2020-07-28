import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from demo86_inicio_sesion import Ui_InicioSesion

class AplicacionInicioSesion(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_InicioSesion()
        self.ui.setupUi(self)

        self.show()

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionInicioSesion()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
