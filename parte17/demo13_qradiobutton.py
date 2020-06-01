import sys

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QRadioButton

class SeleccionClaseVueloVentana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('Selección Clase Vuelo')
        self.setFixedSize(350, 300)

        lbl_seleccion_clase_vuelo = QLabel('Seleccione la clase de su vuelo:', self)
        lbl_seleccion_clase_vuelo.move(30, 30)
        lbl_seleccion_clase_vuelo.setFixedWidth(200)

        self.rbn_clase_primera = QRadioButton('Primera clase', self)
        self.rbn_clase_primera.move(30, 80)
        self.rbn_clase_primera.toggled.connect(self.seleccionar_clase)

        self.rbn_clase_negocios = QRadioButton('Clase negocios', self)
        self.rbn_clase_negocios.move(30, 110)
        self.rbn_clase_negocios.toggled.connect(self.seleccionar_clase)

        self.rbn_clase_economica = QRadioButton('Clase económica', self)
        self.rbn_clase_economica.move(30, 140)
        self.rbn_clase_economica.toggled.connect(self.seleccionar_clase)

        self.lbl_resultado_seleccion = QLabel('', self)
        self.lbl_resultado_seleccion.move(30, 180)
        self.lbl_resultado_seleccion.setFixedWidth(200)

    def seleccionar_clase(self):

        costo_vuelo = 0

        if self.rbn_clase_primera.isChecked():
            costo_vuelo = 2000
        if self.rbn_clase_negocios.isChecked():
            costo_vuelo = 1500
        if self.rbn_clase_economica.isChecked():
            costo_vuelo = 1000
        
        self.lbl_resultado_seleccion.setText(f'Costo del tiquete: {costo_vuelo}')


def main():
    app = QApplication(sys.argv)
    ventana = SeleccionClaseVueloVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
