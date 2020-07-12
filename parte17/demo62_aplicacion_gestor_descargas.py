import sys

from PyQt5.QtWidgets import QApplication, QDialog
from demo62_gestor_descargas import Ui_GestorDescargas

class AplicacionGestorDescargas(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_GestorDescargas()
        self.ui.setupUi(self)

        self.ui.btn_iniciar_descarga.clicked.connect(self.iniciar_descarga)

        self.show()

    def iniciar_descarga(self):
        contador = 0

        while contador < 100:
            contador += 0.0001
            self.ui.pbr_descarga.setValue(contador)

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionGestorDescargas()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
