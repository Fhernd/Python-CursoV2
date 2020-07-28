import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QDialog
from demo85_navegacion_registros import Ui_NavegacionRegistros

class AplicacionNavegacionRegistros(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_NavegacionRegistros()
        self.ui.setupUi(self)

        self.ui.btn_primero.clicked.connect(self.primero)
        self.ui.btn_anterior.clicked.connect(self.anterior)
        self.ui.btn_siguiente.clicked.connect(self.siguiente)
        self.ui.btn_ultimo.clicked.connect(self.ultimo)

        self.ui.btn_primero.setEnabled(False)
        self.ui.btn_anterior.setEnabled(False)
        self.ui.btn_siguiente.setEnabled(False)
        self.ui.btn_ultimo.setEnabled(False)

        self.conexion = None
        self.total_registros = 0
        self.registro = 1

        self.conectar_bd()
        self.primero()

        self.show()
    
    def conectar_bd(self):
        pass

    def primero(self):
        pass

    def anterior(self):
        pass

    def siguiente(self):
        pass
    
    def ultimo(self):
        pass

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionNavegacionRegistros()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
