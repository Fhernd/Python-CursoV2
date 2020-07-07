import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from demo46_seleccion_vuelo import Ui_SeleccionVuelo

class AplicacionSeleccionVueloVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_SeleccionVuelo()
        self.ui.setupUi(self)

        self.ui.rbn_primera_clase.toggled.connect(self.seleccionar_vuelo)
        self.ui.rbn_clase_negocios.toggled.connect(self.seleccionar_vuelo)
        self.ui.rbn_clase_economica.toggled.connect(self.seleccionar_vuelo)

        self.show()
    
    def seleccionar_vuelo(self):
        costo_vuelo = 0

        if self.ui.rbn_primera_clase.isChecked():
            costo_vuelo = 190
        
        if self.ui.rbn_clase_negocios.isChecked():
            costo_vuelo = 130
        
        if self.ui.rbn_clase_economica.isChecked():
            costo_vuelo = 99

        self.ui.lbl_resultado_seleccion.setText(f'El costo del vuelo es de ${costo_vuelo}.')

def main():
    app = QApplication(sys.argv)
    ventana = AplicacionSeleccionVueloVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
