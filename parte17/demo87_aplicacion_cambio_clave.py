import sys
import re
import sqlite3

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from demo87_cambio_clave import Ui_CambioClave

class AplicacionCambioClave(QDialog):
    
    def __init__(self):
        super().__init__()

        self.inicialiar_gui()
    
    def inicialiar_gui(self):
        self.ui = Ui_CambioClave()
        self.ui.setupUi(self)

        patron = r'^[a-z]+@[a-z]\.[a-z]{3}$'
        self.regex = re.compile(patron)

        self.mensaje = QMessageBox(self)
        self.mensaje.setWindowTitle('Mensaje')

        self.ui.btn_cambiar_clave.clicked.connect(self.cambiar_clave)

        self.show()
    
    def cambiar_clave(self):
        pass

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionCambioClave()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
