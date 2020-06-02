import sys

from PyQt5.QtWidgets import QApplication, QComboBox, QLabel, QMainWindow

class SeleccionLenguajeVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('Selección Lenguaje de Programación')
        self.setFixedSize(370, 250)

        self.cbx_lenguajes = QComboBox(self)
        self.cbx_lenguajes.move(30, 20)
        self.cbx_lenguajes.setFixedWidth(310)
        self.cbx_lenguajes.addItem('Python')
        self.cbx_lenguajes.addItem('Java')
        self.cbx_lenguajes.addItem('C#')
        self.cbx_lenguajes.addItems(['JavaScript', 'PHP', 'C', 'C++'])
        
        self.cbx_lenguajes.currentIndexChanged.connect(self.cambiar_seleccion_lenguaje)

        self.lbl_seleccion = QLabel('', self)
        self.lbl_seleccion.move(30, 70)
        self.lbl_seleccion.setFixedWidth(310)

    def cambiar_seleccion_lenguaje(self):
        lenguaje = self.cbx_lenguajes.currentText()

        self.lbl_seleccion.setText(f'Su lenguaje favorito es: {lenguaje}')

def main():
    app = QApplication(sys.argv)
    ventana = SeleccionLenguajeVentana()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
