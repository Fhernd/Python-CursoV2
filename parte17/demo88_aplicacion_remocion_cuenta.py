import sys
import sqlite3
import re
import hashlib
import binascii

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from demo88_remocion_cuenta import Ui_RemocionCuentaUsuario

class AplicacionRemocionCuenta(QDialog):
    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_RemocionCuentaUsuario()
        self.ui.setupUi(self)

        self.ui.btn_remover.clicked.connect(self.remover_usuario)

        self.mensaje = QMessageBox(self)
        self.mensaje.setWindowTitle('Mensaje')

        patron = r'^[a-z]+@[a-z]+\.[a-z]{3}$'
        self.regex = re.compile(patron)

        self.show()
    
    def remover_usuario(self):
        correo_electronico = self.ui.txt_correo_electronico.text().strip()

        if len(correo_electronico):
            if self.regex.match(correo_electronico):
                clave = self.ui.txt_clave.text().strip()

                if len(clave):
                    
                    resultado = self.validar_credenciales(correo_electronico, clave)

                    if resultado:
                        self.remover_usuario_bd(correo_electronico)

                        self.mensaje.setIcon(QMessageBox.Information)
                        self.mensaje.setText('El usuario se removió de forma satisfactoria.')
                        self.mensaje.exec_()
                    else:
                        self.mensaje.setIcon(QMessageBox.Warning)
                        self.mensaje.setText('Las credenciales son inválidas.')
                        self.mensaje.exec_()
                else:
                    self.mensaje.setIcon(QMessageBox.Warning)
                    self.mensaje.setText('El campo Contraseña es obligatorio.')
                    self.mensaje.exec_()
            else:
                self.mensaje.setIcon(QMessageBox.Warning)
                self.mensaje.setText('El campo Correo electrónico no es válido.')
                self.mensaje.exec_()
        else:
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.setText('El campo Correo electrónico es obligatorio.')
            self.mensaje.exec_()

    def validar_credenciales(self, correo_electronico, clave):
        try:
            conexion = sqlite3.connect('parte17/demo88.db')

            cursor = conexion.cursor()

            sql = 'SELECT * FROM usuario WHERE email = ?'

            usuario = cursor.execute(sql, (correo_electronico,)).fetchone()

            if usuario and len(usuario):
                clave_almacenada = usuario[1]

                if self.verify_password(clave_almacenada, clave):
                    return True
                else:
                    return False
            else:
                self.mensaje.setIcon(QMessageBox.Warning)
                self.mensaje.setText('No existe un usuario con el correo electrónico especificado.')
                self.mensaje.exec_()

                return False
        except sqlite3.Error:
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.setText('Hay problemas con la conexión de la base de datos. Valide que el archivo de base de datos exista.')
            self.mensaje.exec_()

            return False
    
    def remover_usuario_bd(self, correo_electronico):
        try:
            conexion = sqlite3.connect('parte17/demo88.db')

            cursor = conexion.cursor()

            sql = 'DELETE FROM usuario WHERE email = ?'

            usuario = cursor.execute(sql, (correo_electronico,))

            conexion.commit()
        except sqlite3.Error:
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.setText('Hay problemas con la conexión de la base de datos. Valide que el archivo de base de datos exista.')
            self.mensaje.exec_()
    
    # Fuente: https://www.vitoshacademy.com/hashing-passwords-in-python/
    def verify_password(self, stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                    provided_password.encode('utf-8'), 
                                    salt.encode('ascii'), 
                                    100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')

        return pwdhash == stored_password

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionRemocionCuenta()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
