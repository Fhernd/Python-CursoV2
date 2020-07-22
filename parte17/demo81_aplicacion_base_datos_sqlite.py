import sys

from collections import namedtuple
import re

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from demo81_base_datos_sqlite import Ui_CreacionBaseDatosTabla

Columna = namedtuple('Columna', ['nombre', 'tipo'])

class AplicacionBaseDatosSqlite(QDialog):

    def __init__(self):
        super().__init__()

        self.columnas = []
        patron = '[a-zA-Z]+'
        self.regex = re.compile(patron)

        self.mensaje = QMessageBox(self)

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_CreacionBaseDatosTabla()
        self.ui.setupUi(self)

        self.ui.btn_agregar_columna.clicked.connect(self.agregar_columna)
        self.ui.btn_crear_base_datos.clicked.connect(self.crear_base_datos)

        self.show()
    
    def agregar_columna(self):
        pass

    def crear_base_datos(self):
        pass

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionBaseDatosSqlite()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
