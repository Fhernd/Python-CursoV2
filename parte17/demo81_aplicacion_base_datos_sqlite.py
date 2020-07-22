import sys

from collections import namedtuple
import re
import sqlite3

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from demo81_base_datos_sqlite import Ui_CreacionBaseDatosTabla

Columna = namedtuple('Columna', ['nombre', 'tipo'])

class AplicacionBaseDatosSqlite(QDialog):

    def __init__(self):
        super().__init__()

        self.columnas = []
        patron = '^[a-zA-Z]+$'
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
        nombre_columna = self.ui.txt_nombre_columna.text().strip()

        if self.regex.match(nombre_columna):
            tipo_dato = str(self.ui.cbx_tipo_dato.currentText())

            self.columnas.append(Columna(nombre_columna, tipo_dato))

            self.ui.txt_nombre_columna.setText('')
        else:
            self.mensaje.setWindowTitle('Mensaje')
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.setText('Debe escribir un nombre columna válido (sólo caracteres alfabéticos).')

            self.mensaje.exec_()

    def crear_base_datos(self):
        nombre_base_datos = self.ui.txt_nombre_base_datos.text().strip()
        nombre_tabla = self.ui.txt_nombre_tabla.text().strip()

        if self.regex.match(nombre_base_datos):
            if self.regex.match(nombre_tabla):
                if len(self.columnas):
                    sql = f'CREATE TABLE {nombre_tabla} ('
                    plantilla_columnas = '{} {}'
                    columnas_tabla = []

                    for c in self.columnas:
                        columnas_tabla.append(plantilla_columnas.format(c.nombre, c.tipo))
                    
                    columnas_sql = ', '.join(columnas_tabla)

                    sql += columnas_sql + ')'

                    try:
                        conexion = sqlite3.connect(f'parte17/{nombre_base_datos}.db')
                        cursor = conexion.cursor()

                        cursor.execute(sql)

                        self.mensaje.setWindowTitle('Mensaje')
                        self.mensaje.setIcon(QMessageBox.Information)
                        self.mensaje.setText('La base de datos y la tabla se crearon de forma satisfactoria.')

                        self.mensaje.exec_()
                    except sqlite3.Error as e:
                        self.mensaje.setWindowTitle('Mensaje')
                        self.mensaje.setIcon(QMessageBox.Critical)
                        self.mensaje.setText('La base de datos y la tabla se crearon de forma satisfactoria.')

                        self.mensaje.exec_()
                    finally:
                        if conexion:
                            conexion.close()
                else:
                    self.mensaje.setWindowTitle('Mensaje')
                    self.mensaje.setIcon(QMessageBox.Warning)
                    self.mensaje.setText('Debe especificar al menos una columna para la tabla.')

                    self.mensaje.exec_()
            else:
                self.mensaje.setWindowTitle('Mensaje')
                self.mensaje.setIcon(QMessageBox.Warning)
                self.mensaje.setText('Debe escribir un nombre de tabla válido (sólo caracteres alfabéticos).')

                self.mensaje.exec_()
        else:
            self.mensaje.setWindowTitle('Mensaje')
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.setText('Debe escribir un nombre de base datos válido (sólo caracteres alfabéticos).')

            self.mensaje.exec_()

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionBaseDatosSqlite()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
