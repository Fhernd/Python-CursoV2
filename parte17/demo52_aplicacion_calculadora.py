import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QDoubleValidator
from demo52_calculadora import Ui_Calculadora

class AplicacionCalculadora(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_Calculadora()
        self.ui.setupUi(self)

        self.ui.btn_sumar.clicked.connect(self.sumar)
        self.ui.btn_restar.clicked.connect(self.restar)
        self.ui.btn_multiplicar.clicked.connect(self.multiplicar)
        self.ui.btn_dividir.clicked.connect(self.dividir)

        self.ui.txt_primer_numero.setValidator(QDoubleValidator())
        self.ui.txt_segundo_numero.setValidator(QDoubleValidator())

        self.show()
    
    def sumar(self):
        primer_numero = float(self.ui.txt_primer_numero.text())
        segundo_numero = float(self.ui.txt_segundo_numero.text())
        self.ui.lbl_resultado.setText(f'{primer_numero + segundo_numero}')
    
    def restar(self):
        primer_numero = float(self.ui.txt_primer_numero.text())
        segundo_numero = float(self.ui.txt_segundo_numero.text())
        self.ui.lbl_resultado.setText(f'{primer_numero - segundo_numero}')
    
    def multiplicar(self):
        primer_numero = float(self.ui.txt_primer_numero.text())
        segundo_numero = float(self.ui.txt_segundo_numero.text())
        self.ui.lbl_resultado.setText(f'{primer_numero * segundo_numero}')
    
    def dividir(self):
        primer_numero = float(self.ui.txt_primer_numero.text())
        segundo_numero = float(self.ui.txt_segundo_numero.text())

        if segundo_numero != 0:
            self.ui.lbl_resultado.setText(f'{primer_numero / segundo_numero}')
        else:
            self.ui.lbl_resultado.setText('La división entre cero no está definida.')

def main():
    app = QApplication(sys.argv)
    ventana = AplicacionCalculadora()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
