import sys

from PyQt5.QtWidgets import QApplication, QComboBox, QDialog, QDialogButtonBox, QFormLayout, QGroupBox, QLabel, QLineEdit, QSpinBox

class RegistroDialogo(QDialog):
    def __init__(self):
        super().__init__()

        self.inicializarGui()

    def inicializarGui(self):
        self.setWindowTitle('Registro Datos')
        self.setFixedSize(400, 400)

        self.crearFormularioRegistro()
    
    def crearFormularioRegistro(self):
        self.gbx_controles = QGroupBox('Datos Básicos')

        layout = QFormLayout()
        layout.addRow(QLabel('Nombre:'), QLineEdit())
        layout.addRow(QLabel('País:'), QComboBox())
        layout.addRow(QLabel('Edad:'), QSpinBox())

        self.gbx_controles.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    dialogo = RegistroDialogo()
    sys.exit(dialogo.exec_())

if __name__ == '__main__':
    main()
