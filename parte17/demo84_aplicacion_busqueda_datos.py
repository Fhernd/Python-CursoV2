import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.QtGui import QIntValidator
from demo84_busqueda_datos import Ui_BusquedaDatos

class AplicacionBusquedaDatos(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_BusquedaDatos()
        self.ui.setupUi(self)

        self.ui.btn_buscar.clicked.connect(self.buscar)

        self.ui.txt_documento.setValidator(QIntValidator(1000, 9999))

        self.mensaje = QMessageBox(self)
        self.mensaje.setWindowTitle('Mensaje')

        self.show()
    
    def buscar(self):
        documento = self.ui.txt_documento.text().strip()

        if len(documento):
            nombre_archivo = 'parte17/demo84.db'

            try:
                conexion = sqlite3.connect(nombre_archivo)

                cursor = conexion.cursor()

                sql = 'SELECT * FROM personas WHERE documento = ?'

                cursor.execute(sql, (documento,))

                resultados = cursor.fetchall()

                if len(resultados):
                    persona = resultados[0]

                    self.ui.txt_nombre_completo.setText(persona[1])
                    self.ui.txt_ahorros.setText(str(persona[2]))
                else:
                    self.ui.txt_nombre_completo.setText('')
                    self.ui.txt_ahorros.setText('')
                    self.mensaje.setIcon(QMessageBox.Warning)
                    self.mensaje.setText('No existe una persona con el documento especificado.')
                    self.mensaje.exec_()
            except sqlite3.Error:
                self.mensaje.setIcon(QMessageBox.Warning)
                self.mensaje.setText('Hay problemas con la conexión de la base de datos.')
                self.mensaje.exec_()
        else:
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.setText('El campo Documento es obligatorio.')
            self.mensaje.exec_()

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionBusquedaDatos()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
