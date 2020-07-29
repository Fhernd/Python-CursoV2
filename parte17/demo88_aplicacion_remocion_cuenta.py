import sys
import sqlite3
import re

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
            pass
        else:
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.setText('El campo Correo electrónico es obligatorio.')
            self.mensaje.exec_()

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionRemocionCuenta()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
