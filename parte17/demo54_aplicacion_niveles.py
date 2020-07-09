import sys

from PyQt5.QtWidgets import QApplication, QDialog
from demo54_niveles import Ui_Niveles

class AplicacionNiveles(QDialog):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_Niveles()
        self.ui.setupUi(self)

        self.ui.hsb_nivel_azucar.valueChanged.connect(self.mostrar_nivel_azucar)
        self.ui.hsd_presion_arterial.valueChanged.connect(self.mostrar_presion_arterial)
        self.ui.vsb_pulso.valueChanged.connect(self.mostrar_pulso)
        self.ui.vsd_nivel_colesterol.valueChanged.connect(self.mostrar_nivel_colesterol)

        self.show()
    
    def mostrar_nivel_azucar(self, valor):
        self.ui.txt_resultado.setText(f'Nivel de azúcar: {valor}')
    
    def mostrar_presion_arterial(self, valor):
        self.ui.txt_resultado.setText(f'Presión arterial: {valor}')
    
    def mostrar_pulso(self, valor):
        self.ui.txt_resultado.setText(f'Pulso: {valor}')
    
    def mostrar_nivel_colesterol(self, valor):
        self.ui.txt_resultado.setText(f'Nivel colesterol: {valor}')

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionNiveles()
    dialogo.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
