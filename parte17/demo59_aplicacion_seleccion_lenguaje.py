import sys

from PyQt5.QtWidgets import QApplication, QDialog
from demo59_seleccion_lenguaje import Ui_Lenguajes

class AplicacionSeleccionLenguaje(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_Lenguajes()
        self.ui.setupUi(self)

        self.ui.cbx_lenguajes.currentIndexChanged.connect(self.seleccionar_lenguaje)

        self.show()
    
    def seleccionar_lenguaje(self):
        indice = self.ui.cbx_lenguajes.currentIndex()
        seleccion = self.ui.cbx_lenguajes.itemText(indice)

        self.ui.lbl_seleccion.setText(f'El lenguaje seleccionado es: {seleccion}')

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionSeleccionLenguaje()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
