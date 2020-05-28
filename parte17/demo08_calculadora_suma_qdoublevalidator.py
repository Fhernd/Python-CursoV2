import sys

from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QMessageBox, QPushButton
from PyQt5.QtGui import QDoubleValidator

class CalculadoraVentana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initUi()
    
    def initUi(self):
        self.setWindowTitle('Calculadora Básica')
        self.setFixedSize(400, 300)

        self.lbl_primer_numero = QLabel('Primer número:', self)
        self.lbl_primer_numero.move(30, 30)

        self.txt_primer_numero = QLineEdit(self)
        self.txt_primer_numero.move(150, 30)
        self.txt_primer_numero.setFixedWidth(200)
        self.txt_primer_numero.setValidator(QDoubleValidator())

        self.lbl_segundo_numero = QLabel('Segundo número:', self)
        self.lbl_segundo_numero.move(30, 80)

        self.txt_segundo_numero = QLineEdit(self)
        self.txt_segundo_numero.move(150, 80)
        self.txt_segundo_numero.setFixedWidth(200)
        self.txt_segundo_numero.setValidator(QDoubleValidator())

        self.btn_calcular_suma = QPushButton('Sumar', self)
        self.btn_calcular_suma.move(150, 130)
        self.btn_calcular_suma.setFixedWidth(200)
        self.btn_calcular_suma.clicked.connect(self.sumar)

        self.lbl_resultado = QLabel('Resultado:', self)
        self.lbl_resultado.move(30, 200)

        self.txt_resultado = QLineEdit(self)
        self.txt_resultado.move(150, 200)
        self.txt_resultado.setFixedWidth(200)
        self.txt_resultado.setEnabled(False)
    
    def sumar(self):
        primer_numero = float(self.txt_primer_numero.text())
        segundo_numero = float(self.txt_segundo_numero.text())

        suma = primer_numero + segundo_numero

        self.txt_resultado.setText(str(suma))
        

def main():
    app = QApplication(sys.argv)
    calculadora = CalculadoraVentana()
    calculadora.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
