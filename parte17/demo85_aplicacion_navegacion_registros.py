import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
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

        self.mensaje = QMessageBox(self)
        self.mensaje.setWindowTitle('Mensaje')

        self.show()
    
    def conectar_bd(self):
        try:
            self.conexion = sqlite3.connect('parte17/demo85.db')

            sql = '''SELECT * FROM personas'''
            self.cursor = self.conexion.cursor()
            self.total_registros = len(self.cursor.execute(sql).fetchall())

            self.ui.btn_primero.setEnabled(True)
            self.ui.btn_anterior.setEnabled(True)
            self.ui.btn_siguiente.setEnabled(True)
            self.ui.btn_ultimo.setEnabled(True)
            
        except sqlite3.Error:
            self.mensaje.setIcon(QMessageBox.Critical)
            self.mensaje.setText('Hay problemas al intentar conectar con la base de datos. Revise que el archivo esté disponible.')
            self.mensaje.exec_()

    def primero(self):
        self.registro = 1
        sql = '''SELECT * FROM personas LIMIT 1'''
        persona = self.cursor.execute(sql).fetchone()

        if persona and len(persona):
            self.ui.txt_documento.setText(str(persona[0]))
            self.ui.txt_nombre_completo.setText(persona[1])
            self.ui.txt_ahorros.setText(str(persona[2]))

    def anterior(self):
        if self.registro > 1:
            sql = '''SELECT * FROM personas ORDER BY documento DESC LIMIT 1 OFFSET ?'''
            self.registro -= 1
            persona = self.cursor.execute(sql, (self.total_registros - self.registro,)).fetchone()

            if persona and len(persona):
                self.ui.txt_documento.setText(str(persona[0]))
                self.ui.txt_nombre_completo.setText(persona[1])
                self.ui.txt_ahorros.setText(str(persona[2]))
        else:
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.setText('Ha alcanzado el primer registro.')
            self.mensaje.exec_()

    def siguiente(self):
        if self.registro < self.total_registros:
            sql = '''SELECT * FROM personas LIMIT 1 OFFSET ?'''
            self.registro += 1
            persona = self.cursor.execute(sql, (self.registro,)).fetchone()

            if persona and len(persona):
                self.ui.txt_documento.setText(str(persona[0]))
                self.ui.txt_nombre_completo.setText(persona[1])
                self.ui.txt_ahorros.setText(str(persona[2]))
        else:
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.setText('Ha alcanzado el último registro.')
            self.mensaje.exec_()
    
    def ultimo(self):
        self.registro = self.total_registros
        sql = '''SELECT * FROM personas ORDER BY documento DESC LIMIT 1'''
        persona = self.cursor.execute(sql).fetchone()

        if persona and len(persona):
            self.ui.txt_documento.setText(str(persona[0]))
            self.ui.txt_nombre_completo.setText(persona[1])
            self.ui.txt_ahorros.setText(str(persona[2]))

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionNavegacionRegistros()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
