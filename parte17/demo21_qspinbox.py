import sys

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QSpinBox

class SeleccionNumericaVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('Selección Numérica')
        self.setFixedSize(300, 250)

        self.spb_selector_numerico = QSpinBox(self)
        self.spb_selector_numerico.move(30, 20)
        self.spb_selector_numerico.setFixedWidth(240)
        self.spb_selector_numerico.setMinimum(18)
        self.spb_selector_numerico.setMaximum(80)
        self.spb_selector_numerico.setValue(23)
        self.spb_selector_numerico.valueChanged.connect(self.cambiar_valor)

        self.lbl_valor_numerico_seleccionado = QLabel(self)
        self.lbl_valor_numerico_seleccionado.move(30, 70)
        self.lbl_valor_numerico_seleccionado.setFixedWidth(240)
    
    def cambiar_valor(self):
        self.lbl_valor_numerico_seleccionado.setText(f'Valor seleccionado: {self.spb_selector_numerico.value()}')


def main():
    app = QApplication(sys.argv)
    ventana = SeleccionNumericaVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
