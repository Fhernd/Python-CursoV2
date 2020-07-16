import sys

from PyQt5.QtWidgets import QApplication, QDialog, QFontDialog
from demo72_selector_fuente import Ui_SelectorFuente

class AplicacionSelectorFuente(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_SelectorFuente()
        self.ui.setupUi(self)

        self.ui.txt_contenido.setText('PyQt5')

        self.ui.btn_seleccionar_fuente.clicked.connect(self.seleccionar_fuente)

        self.show()
    
    def seleccionar_fuente(self):
        fuente, ok = QFontDialog.getFont()

        if ok:
            self.ui.txt_contenido.setFont(fuente)

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionSelectorFuente()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
