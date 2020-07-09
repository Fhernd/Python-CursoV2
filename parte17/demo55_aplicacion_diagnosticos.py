import sys

from PyQt5.QtWidgets import QApplication, QDialog
from demo55_diagnosticos import Ui_Diagnosticos

class AplicacionDiagnosticos(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializarGui()

    def inicializarGui(self):
        self.ui = Ui_Diagnosticos()
        self.ui.setupUi(self)

        self.ui.lst_diagnosticos.itemClicked.connect(self.mostrar_diagnostico_seleccionado)

        self.show()

    def mostrar_diagnostico_seleccionado(self, diagnostico):
        self.ui.lbl_diagnostico_seleccionado.setText(diagnostico.text())

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionDiagnosticos()
    dialogo.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
