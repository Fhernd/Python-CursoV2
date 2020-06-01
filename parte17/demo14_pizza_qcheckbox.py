import sys

from PyQt5.QtWidgets import QApplication, QCheckBox, QLabel, QMainWindow

class PizzaVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()

    def inicializarGui(self):
        self.setWindowTitle('Pizza & Ingredientes')
        self.setFixedSize(400, 350)

        lbl_pizza = QLabel('Precio base pizza: $15', self)
        lbl_pizza.move(30, 30)
        lbl_pizza.setFixedWidth(200)

        lbl_ingredientes_adicionales = QLabel('Ingredientes adicionales:', self)
        lbl_ingredientes_adicionales.move(30, 80)

        self.chk_queso = QCheckBox('Queso ($1)', self)
        self.chk_queso.move(30, 110)
        self.chk_queso.stateChanged.connect(self.calcular_precio_final)

        self.chk_aceitunas = QCheckBox('Aceitunas ($2)', self)
        self.chk_aceitunas.move(30, 140)
        self.chk_aceitunas.stateChanged.connect(self.calcular_precio_final)

        self.chk_salsas = QCheckBox('Salsas ($1)', self)
        self.chk_salsas.move(30, 170)
        self.chk_salsas.stateChanged.connect(self.calcular_precio_final)

        self.lbl_resultado = QLabel('', self)
        self.lbl_resultado.move(30, 220)
        self.lbl_resultado.setFixedWidth(250)

    def calcular_precio_final(self):
        precio_base = 15

        if self.chk_queso.isChecked():
            precio_base += 1
        if self.chk_aceitunas.isChecked():
            precio_base += 2
        if self.chk_salsas.isChecked():
            precio_base += 1
        
        self.lbl_resultado.setText(f'El precio a pagar es ${precio_base}')

def main():
    app = QApplication(sys.argv)
    ventana = PizzaVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
