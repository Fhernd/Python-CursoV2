import sys

from PyQt5.QtWidgets import QApplication, QDialog, QLCDNumber
from demo63_visor import Ui_Visor

class AplicacionVisor(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializarGui()

    def inicializarGui(self):
        self.ui = Ui_Visor()
        self.ui.setupUi(self)

        self.ui.lcd_numero.display(43)
        self.ui.lcd_numero.setDigitCount(7)

        self.ui.btn_decimal.clicked.connect(self.mostrar_decimal)
        self.ui.btn_binario.clicked.connect(self.mostrar_binario)
        self.ui.btn_octal.clicked.connect(self.mostrar_octal)
        self.ui.btn_hexadecimal.clicked.connect(self.mostrar_hexadecimal)

        self.show()
    
    def mostrar_decimal(self):
        self.ui.lcd_numero.setMode(QLCDNumber.Dec)
    
    def mostrar_binario(self):
        self.ui.lcd_numero.setMode(QLCDNumber.Bin)

    def mostrar_octal(self):
        self.ui.lcd_numero.setMode(QLCDNumber.Oct)
    
    def mostrar_hexadecimal(self):
        self.ui.lcd_numero.setMode(QLCDNumber.Hex)

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionVisor()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
