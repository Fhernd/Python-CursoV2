import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.QtGui import QIntValidator
from demo69_registro_profesor_emerito import Ui_RegistroProfesorEmerito

class AplicacionRegistro(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_RegistroProfesorEmerito()
        self.ui.setupUi(self)

        self.ui.txt_identidad.setValidator(QIntValidator(1000, 10000))
        self.ui.txt_telefono.setValidator(QIntValidator(1000000, 9999999))

        self.ui.btn_registrar.clicked.connect(self.registrar_profesor)

        self.show()
    
    def registrar_profesor(self):
        identidad = self.ui.txt_identidad.text()
        nombre_completo = self.ui.txt_nombre_completo.text().strip()
        telefono = self.ui.txt_telefono.text()
        reconocimiento = self.ui.txt_reconocimiento.text()

        mensaje = QMessageBox(self)
        mensaje.setWindowTitle('Mensaje')

        if len(identidad) and len(nombre_completo) and len(telefono) and len(reconocimiento):
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setText('El registro se realizó de forma satisfactoria.')
        else:
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setText('Todos los campos son obligatorios.')
        
        mensaje.exec_()

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionRegistro()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
