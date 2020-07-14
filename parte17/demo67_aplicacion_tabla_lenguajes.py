import sys

from PyQt5.QtWidgets import QApplication, QDialog
from demo67_tabla_lenguajes import Ui_TablaLenguajes

class AplicacionTablaLenguajes(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_TablaLenguajes()
        self.ui.setupUi(self)

        self.show()

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionTablaLenguajes()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
506