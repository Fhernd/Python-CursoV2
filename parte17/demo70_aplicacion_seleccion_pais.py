import sys

from PyQt5.QtWidgets import QApplication, QDialog, QInputDialog
from demo70_seleccion_pais import Ui_SeleccionPais

class AplicacionSeleccionPais(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_SeleccionPais()
        self.ui.setupUi(self)

        self.paises = ('Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Ecuador', 'Paraguay', 'Perú', 'Uruguay', 'Venezuela')

        self.ui.btn_seleccion_pais.clicked.connect(self.seleccionar_pais)

        self.show()
    
    def seleccionar_pais(self):
        pais, estado = QInputDialog.getItem(self, 'Selección País', 'Seleccione su país:', self.paises, 4, False)

        if estado and pais:
            self.ui.txt_pais_seleccionado.setText(pais)

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionSeleccionPais()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
