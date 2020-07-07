import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from demo48_pizzeria import Ui_Pizzeria

class AplicacionPizzeria(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_Pizzeria()
        self.ui.setupUi(self)

        self.ui.chk_queso.stateChanged.connect(self.calcular_precio)
        self.ui.chk_aceitunas.stateChanged.connect(self.calcular_precio)
        self.ui.chk_salsas.stateChanged.connect(self.calcular_precio)

        self.show()
    
    def calcular_precio(self):
        precio = 15

        if self.ui.chk_queso.isChecked():
            precio += 1
        
        if self.ui.chk_aceitunas.isChecked():
            precio += 2
        
        if self.ui.chk_salsas.isChecked():
            precio += 1
        
        self.ui.lbl_precio_final.setText(f'Precio final: ${precio}')

def main():
    app = QApplication(sys.argv)
    ventana = AplicacionPizzeria()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
