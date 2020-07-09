import sys

from PyQt5.QtWidgets import QApplication, QDialog
from demo53_punto_venta import Ui_PuntoVenta
from PyQt5.QtGui import QIntValidator

class AplicacionPuntoVenta(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_PuntoVenta()
        self.ui.setupUi(self)

        self.ui.txt_mouse_precio.setValidator(QIntValidator(0, 1000000, self))
        self.ui.txt_teclado_precio.setValidator(QIntValidator(0, 1000000, self))

        self.ui.sbx_mouse_cantidad.valueChanged.connect(self.calcular_total)
        self.ui.sbx_teclado_cantidad.valueChanged.connect(self.calcular_total)

        self.show()
    
    def calcular_total(self):
        precio_mouse = self.ui.txt_mouse_precio.text()
        cantidad_mouse = self.ui.sbx_mouse_cantidad.value()

        precio_teclado = self.ui.txt_teclado_precio.text()
        cantidad_teclado = self.ui.sbx_teclado_cantidad.value()
        total = 0

        if len(precio_mouse):
            total += int(precio_mouse) * cantidad_mouse
            self.ui.txt_mouse_subtotal.setText(str(int(precio_mouse) * cantidad_mouse))
        
        if len(precio_teclado):
            total += int(precio_teclado) * cantidad_teclado
            self.ui.txt_teclado_subtotal.setText(str(int(precio_teclado) * cantidad_teclado))
        
        self.ui.lbl_total.setText(f'${total}')

def main():
    app = QApplication(sys.argv)
    ventana = AplicacionPuntoVenta()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
