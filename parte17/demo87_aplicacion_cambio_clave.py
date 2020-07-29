import sys
import re
import sqlite3
import os
import hashlib
import binascii

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from demo87_cambio_clave import Ui_CambioClave

class AplicacionCambioClave(QDialog):
    
    def __init__(self):
        super().__init__()

        self.inicialiar_gui()
    
    def inicialiar_gui(self):
        self.ui = Ui_CambioClave()
        self.ui.setupUi(self)

        patron = r'^[a-z]+@[a-z]+\.[a-z]{3}$'
        self.regex = re.compile(patron)

        self.mensaje = QMessageBox(self)
        self.mensaje.setWindowTitle('Mensaje')

        self.ui.btn_cambiar_clave.clicked.connect(self.cambiar_clave)

        self.show()
    
    def cambiar_clave(self):
        correo_electronico = self.ui.txt_correo_electronico.text().strip()

        if len(correo_electronico):
            if self.regex.match(correo_electronico):
                clave_actual = self.ui.txt_clave_actual.text().strip()

                if len(clave_actual):
                    nueva_clave = self.ui.txt_nueva_clave.text().strip()

                    if len(nueva_clave):
                        nueva_clave_repetir = self.ui.txt_nueva_clave_repetir.text().strip()

                        if len(nueva_clave_repetir):
                            if nueva_clave == nueva_clave_repetir:
                                
                                resultado = self.validar_credenciales(correo_electronico, clave_actual)

                                if resultado:
                                    if self.cambiar_clave_nueva(correo_electronico, nueva_clave):
                                        self.mensaje.setIcon(QMessageBox.Information)
                                        self.mensaje.setText('La contraseña se cambió de forma satisfactoria.')
                                        self.mensaje.exec_()
                                    else:
                                        self.mensaje.setIcon(QMessageBox.Warning)
                                        self.mensaje.setText('No se ha podido cambiar la contraseña.')
                                        self.mensaje.exec_()
                                else:
                                    self.mensaje.setIcon(QMessageBox.Warning)
                                    self.mensaje.setText('Las credenciales no son válidas. Intente nuevamente.')
                                    self.mensaje.exec_()
                            else:
                                self.mensaje.setIcon(QMessageBox.Warning)
                                self.mensaje.setText('Asegúrese que las contraseñas nuevas sean iguales.')
                                self.mensaje.exec_()
                        else:
                            self.mensaje.setIcon(QMessageBox.Warning)
                            self.mensaje.setText('El campo Nueva contraseña (repetir) es obligatorio.')
                            self.mensaje.exec_()
                    else:
                        self.mensaje.setIcon(QMessageBox.Warning)
                        self.mensaje.setText('El campo Nueva contraseña es obligatorio.')
                        self.mensaje.exec_()
                else:
                    self.mensaje.setIcon(QMessageBox.Warning)
                    self.mensaje.setText('El campo Contraseña actual es obligatorio.')
                    self.mensaje.exec_()
            else:
                self.mensaje.setIcon(QMessageBox.Warning)
                self.mensaje.setText('Se ha escrito un correo electrónico inválido.')
                self.mensaje.exec_()
        else:
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.setText('El campo Correo electrónico es obligatorio.')
            self.mensaje.exec_()
    
    def cambiar_clave_nueva(self, correo_electronico, nueva_clave):
        try:
            conexion = sqlite3.connect('parte17/demo87.db')

            cursor = conexion.cursor()
            sql = 'UPDATE usuario SET clave = ? WHERE email = ?'

            hash_nueva_clave = self.hash_password(nueva_clave)

            cursor.execute(sql, (hash_nueva_clave, correo_electronico))

            conexion.commit()

            return cursor.rowcount > 0
        except sqlite3.Error:
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.setText('Hay problemas con la conexión con la base de datos. Verifique que exista el archivo de base de datos.')
            self.mensaje.exec_()
            return False

    def validar_credenciales(self, correo_electronico, clave):
        try:
            conexion = sqlite3.connect('parte17/demo87.db')

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
            self.mensaje.setText('Hay problemas con la conexión con la base de datos. Verifique que exista el archivo de base de datos.')
            self.mensaje.exec_()

            return False
    # Fuente: https://www.vitoshacademy.com/hashing-passwords-in-python/
    def hash_password(self, password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                    salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')
    
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
    dialogo = AplicacionCambioClave()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
