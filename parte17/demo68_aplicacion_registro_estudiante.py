import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.QtGui import QIntValidator
from demo68_registro_estudiante import Ui_RegistroEstudiante

class AplicacionRegistroEstudiante(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_RegistroEstudiante()
        self.ui.setupUi(self)

        self.ui.txt_identidad.setValidator(QIntValidator(1000, 2000000000))
        self.ui.txt_telefono.setValidator(QIntValidator(1000000, 9999999))
        self.ui.txt_carnet.setValidator(QIntValidator(10000, 1000000))

        self.ui.btn_registrar.clicked.connect(self.registrar_estudiante)

        self.show()
    
    def registrar_estudiante(self):
        identidad = self.ui.txt_identidad.text()
        nombre_completo = self.ui.txt_nombre_completo.text().strip()
        telefono = self.ui.txt_telefono.text()
        carnet = self.ui.txt_carnet.text()

        mensaje = QMessageBox(self)
        mensaje.setWindowTitle('Mensaje')

        if len(identidad) and len(nombre_completo) and len(telefono) and len(carnet):
            indice = self.ui.cbx_carreras.currentIndex()
            carrera = self.ui.cbx_carreras.itemText(indice)

            mensaje.setIcon(QMessageBox.Information)
            mensaje.setText('El registro se ha realizado de forma satisfactoria.')
        else:
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setText('Todos los campos son obligatorios.')
        
        mensaje.exec_()

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionRegistroEstudiante()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
