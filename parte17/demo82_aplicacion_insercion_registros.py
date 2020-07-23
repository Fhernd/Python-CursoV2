import sys

import sqlite3
import re
import os

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from demo82_insercion_registros import Ui_InsercionRegistros

class AplicacionInsercionRegistros(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_InsercionRegistros()
        self.ui.setupUi(self)

        self.patron_nombre_tabla = '^[a-zA-Z]+$'
        self.regex_nombre_tabla = re.compile(self.patron_nombre_tabla)

        self.patron_nombre_base_datos = '^[a-zA-Z0-9]+$'
        self.regex_nombre_base_datos = re.compile(self.patron_nombre_base_datos)

        self.ui.btn_conectar.clicked.connect(self.conectar)
        self.ui.btn_insertar.clicked.connect(self.insertar)

        self.ui.txt_documento.setValidator(QIntValidator(1000, 9999))
        self.ui.txt_ahorros.setValidator(QDoubleValidator(0, 10000000, 2))

        self.mensaje = QMessageBox(self)
        self.mensaje.setWindowTitle('Mensajes')

        self.conexion = None

        self.show()
    
    def conectar(self):
        nombre_base_datos = self.ui.txt_nombre_base_datos.text().strip()

        if self.regex_nombre_base_datos.match(nombre_base_datos):
            archivo_bd = f'parte17/{nombre_base_datos}.db'

            if os.path.exists(archivo_bd):
                try:
                    self.conexion = sqlite3.connect(archivo_bd)

                    self.mensaje.setIcon(QMessageBox.Information)
                    self.mensaje.setText('Se ha establecido la conexión con la base de datos.')
                    self.mensaje.exec_()

                    self.ui.txt_nombre_tabla.setReadOnly(False)
                    self.ui.txt_documento.setReadOnly(False)
                    self.ui.txt_nombre_completo.setReadOnly(False)
                    self.ui.txt_ahorros.setReadOnly(False)

                    self.ui.btn_insertar.setEnabled(True)
                except sqlite3.Error as e:
                    self.mensaje.setIcon(QMessageBox.Critical)
                    self.mensaje.setText('No se pudo establecer la conexión con la base de datos.')

                    self.mensaje.exec_()
            else:
                self.mensaje.setIcon(QMessageBox.WarRning)
                self.mensaje.setText('El archivo de base de datos no existe.')

                self.mensaje.exec_()
        else:
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.setText('Debe escribir un nombre válido para la base de datos (caracteres a-z, A-Z, 0-9).')

            self.mensaje.exec_()

    def insertar(self):
        if self.conexion is None:
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.setText('Aún no hay una conexión con la base de datos.')

            self.mensaje.exec_()
            return
        
        nombre_tabla = self.ui.txt_nombre_tabla.text().strip()

        if self.regex_nombre_tabla.match(nombre_tabla):
            documento = self.ui.txt_documento.text().strip()

            if len(documento):
                nombre_completo = self.ui.txt_nombre_completo.text().strip()

                if len(nombre_completo):
                    ahorros = self.ui.txt_ahorros.text().strip()

                    if len(ahorros):
                        sql = '''INSERT INTO {} VALUES ({}, '{}', {})'''.format(nombre_tabla, documento, nombre_completo, ahorros)

                        cursor = self.conexion.cursor()
                        cursor.execute(sql)
                        self.conexion.commit()

                        self.mensaje.setIcon(QMessageBox.Information)
                        self.mensaje.setText('El registro se insertó de forma satisfactoria.')

                        self.mensaje.exec_()

                        self.ui.txt_nombre_completo.setText('')
                        self.ui.txt_documento.setText('')
                        self.ui.txt_ahorros.setText('')
                    else:
                        self.mensaje.setIcon(QMessageBox.Warning)
                        self.mensaje.setText('El campo Ahorros es obligatorio.')

                        self.mensaje.exec_()
                else:
                    self.mensaje.setIcon(QMessageBox.Warning)
                    self.mensaje.setText('El campo Nombre Completo es obligatorio.')

                    self.mensaje.exec_()
            else:
                self.mensaje.setIcon(QMessageBox.Warning)
                self.mensaje.setText('El campo Documento es obligatorio.')

                self.mensaje.exec_()
        else:
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.setText('Debe escribir un nombre válido para la tabla (caracteres a-z, A-Z).')

            self.mensaje.exec_()

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionInsercionRegistros()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
