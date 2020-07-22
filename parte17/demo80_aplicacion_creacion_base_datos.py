import sys

import sqlite3

from PyQt5.QtWidgets import QApplication, QDialog
from demo80_creacion_base_datos import Ui_CreacionBaseDatos

class AplicacionCreacionBaseDatos(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()

    def inicializar_gui(self):
        self.ui = Ui_CreacionBaseDatos()
        self.ui.setupUi(self)

        self.ui.btn_crear_base_datos.clicked.connect(self.crear_base_datos)

        self.show()
    
    def crear_base_datos(self):
        nombre_base_datos = self.ui.txt_nombre_base_datos.text().strip()

        if len(nombre_base_datos):
            try:
                conexion = sqlite3.connect(f'parte17/{nombre_base_datos}.db')
                self.ui.lbl_resultado.setText('Resultado: La base de datos se creó correctamente.')
            except sqlite3.Error as e:
                self.ui.lbl_resultado.setText('Resultado: Hay problemas con la creación de la base de datos.')
            finally:
                if conexion:
                    conexion.close()
        else:
            self.ui.lbl_resultado.setText('Resultado: Debe escribir un nombre válido para la base de datos.')

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionCreacionBaseDatos()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
