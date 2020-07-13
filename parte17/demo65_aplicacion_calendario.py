import sys

from PyQt5.QtWidgets import QApplication, QDialog
from demo65_calendario import Ui_Almanaque

class AplicacionCalendario(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_Almanaque()
        self.ui.setupUi(self)

        self.ui.cal_calendario.selectionChanged.connect(self.cambiar_fecha)

        self.show()
    
    def cambiar_fecha(self):
        self.ui.det_fecha_seleccionada.setDate(self.ui.cal_calendario.selectedDate())

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionCalendario()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
