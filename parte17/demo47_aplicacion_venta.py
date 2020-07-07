import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from demo47_venta import Ui_VentaVentana

class AplicacionVentaVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_VentaVentana()
        self.ui.setupUi(self)

        self.ui.rbn_m.toggled.connect(self.mostrar_resultado)
        self.ui.rbn_l.toggled.connect(self.mostrar_resultado)
        self.ui.rbn_xl.toggled.connect(self.mostrar_resultado)
        self.ui.rbn_xll.toggled.connect(self.mostrar_resultado)

        self.ui.rbn_tarjeta_credito_debito.toggled.connect(self.mostrar_resultado)
        self.ui.rbn_pago_contraentrega.toggled.connect(self.mostrar_resultado)
        self.ui.rbn_consignacion_bancaria.toggled.connect(self.mostrar_resultado)
        self.ui.rbn_efectivo.toggled.connect(self.mostrar_resultado)

        self.show()
    
    def mostrar_resultado(self):
        talla = ''
        metodo_pago = 'Efectivo'

        if self.ui.rbn_m.isChecked():
            talla = 'M'
        if self.ui.rbn_l.isChecked():
            talla = 'L'
        if self.ui.rbn_xl.isChecked():
            talla = 'XL'
        if self.ui.rbn_xll.isChecked():
            talla = 'XLL'
        
        if self.ui.rbn_tarjeta_credito_debito.isChecked():
            metodo_pago = 'Tarjeta crédito/débito'

        if self.ui.rbn_pago_contraentrega.isChecked():
            metodo_pago = 'Pago contraentrega'
        
        if self.ui.rbn_consignacion_bancaria.isChecked():
            metodo_pago = 'Consignación bancaria'
        
        if self.ui.rbn_efectivo.isChecked():
            metodo_pago = 'Efectivo'
        

        self.ui.lbl_resultado_seleccion.setText(f'La talla seleccionada es {talla}, y el método de pago {metodo_pago}.')

def main():
    app = QApplication(sys.argv)
    ventana = AplicacionVentaVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
