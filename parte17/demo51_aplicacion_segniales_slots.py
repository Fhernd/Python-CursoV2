import sys

from PyQt5.QtWidgets import QApplication, QDialog
from demo51_segniales_slots import Ui_SegnialesSlots

class Aplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_SegnialesSlots()
        self.ui.setupUi(self)

        self.show()

def main():
    app = QApplication(sys.argv)
    ventana = Aplicacion()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
