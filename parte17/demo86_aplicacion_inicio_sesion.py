import sys
import sqlite3
import re

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from demo86_inicio_sesion import Ui_InicioSesion

class AplicacionInicioSesion(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_InicioSesion()
        self.ui.setupUi(self)

        self.ui.btn_iniciar_sesion.clicked.connect(self.iniciar_sesion)

        self.mensaje = QMessageBox(self)
        self.mensaje.setWindowTitle('Mensaje')

        patron = '^[a-z]+@[a-z]+\.[a-z]{3}$'
        self.regex = re.compile(patron)

        self.show()
    
    def iniciar_sesion(self):
        correo_electronico = self.ui.txt_correo_electronico.text().strip()

        if len(correo_electronico):
            if self.regex.match(correo_electronico):
                clave = self.ui.txt_clave.text().strip()

                if len(clave):
                    
                    resultado = self.validar_credenciales(correo_electronico, clave)

                else:
                    self.mensaje.setIcon(QMessageBox.Warning)
                    self.mensaje.setText('El campo Clave es obligatorio.')
                    self.mensaje.exec_()
            else:
                self.mensaje.setIcon(QMessageBox.Warning)
                self.mensaje.setText('El campo Correo electrónico es obligatorio.')
                self.mensaje.exec_()
        else:
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.setText('El campo Correo electrónico es obligatorio.')
            self.mensaje.exec_()
    
    def validar_credenciales(self, correo_electronico, clave):
        try:
            conexion = sqlite3.connect('parte17/demo86.db')

            
        except sqlite3.Error:
            self.mensaje.setIcon(QMessageBox.Critical)
            self.mensaje.setText('No se ha podido realizar la conexión a la base de datos. Comprueba que el archivo de base de datos exista.')
            self.mensaje.exec_()

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionInicioSesion()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
