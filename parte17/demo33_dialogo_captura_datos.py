import sys

from PyQt5.QtWidgets import QApplication, QComboBox, QDialog, QDialogButtonBox, QFormLayout, QGroupBox, QLabel, QLineEdit, QMessageBox, QSpinBox, QVBoxLayout

class RegistroDialogo(QDialog):
    def __init__(self):
        super().__init__()

        self.inicializarGui()

    def inicializarGui(self):
        self.setWindowTitle('Registro Datos')
        self.setFixedSize(400, 150)

        self.crearFormularioRegistro()

        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.accepted.connect(self.registrar)
        botones.rejected.connect(self.cancelar)

        layout = QVBoxLayout()
        layout.addWidget(self.gbx_controles)
        layout.addWidget(botones)

        self.setLayout(layout)
    
    def registrar(self):
        mensaje = QMessageBox(self)
        mensaje.setIcon(QMessageBox.Information)
        mensaje.setWindowTitle('Mensaje')
        mensaje.setText('Los datos se registraron de forma satisfactoria.')
        mensaje.exec_()

    def cancelar(self):
        mensaje = QMessageBox(self)
        mensaje.setIcon(QMessageBox.Warning)
        mensaje.setWindowTitle('Advertencia')
        mensaje.setText('Los datos no se han registrado.')
        mensaje.exec_()
    
    def crearFormularioRegistro(self):
        self.gbx_controles = QGroupBox('Datos Básicos')

        layout = QFormLayout()
        layout.addRow(QLabel('Nombre:'), QLineEdit())
        
        paises = QComboBox()
        paises.addItem('Colombia')
        paises.addItem('Estados Unidos')
        paises.addItem('Alemania')
        paises.addItem('Perú')
        paises.addItem('Argentina')
        paises.addItem('China')
        paises.addItem('Rusia')
        layout.addRow(QLabel('País:'), paises)

        layout.addRow(QLabel('Edad:'), QSpinBox())

        self.gbx_controles.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    dialogo = RegistroDialogo()
    sys.exit(dialogo.exec_())

if __name__ == '__main__':
    main()
