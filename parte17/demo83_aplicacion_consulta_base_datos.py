import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem
from demo83_consulta_base_datos import Ui_ConsultaDatos

class AplicacionConsultaBaseDatos(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_ConsultaDatos()
        self.ui.setupUi(self)

        self.ui.btn_consultar.clicked.connect(self.consultar)

        self.show()
    
    def consultar(self):
        archivo_base_datos = 'parte17/demo83.db'

        try:
            conexion = sqlite3.connect(archivo_base_datos)

            cursor = conexion.cursor()

            sql = 'SELECT * FROM personas'

            personas = cursor.execute(sql).fetchall()

            for i, p in enumerate(personas):
                columna = 0

                self.ui.tbl_datos.insertRow(self.ui.tbl_datos.rowCount())

                for c in p:
                    celda = QTableWidgetItem(str(c))
                    self.ui.tbl_datos.setItem(i, columna, celda)
                    columna += 1

        except sqlite3.Error as e:
            mensaje = QMessageBox(self)
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setWindowTitle('Mensaje')
            mensaje.setText('Se ha producido un error a la hora de efectuar la conexión a la base de datos.')

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionConsultaBaseDatos()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
