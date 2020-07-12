import sys

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QFont
from demo60_editor_texto import Ui_EditorTexto

class AplicacionEditorTexto(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_EditorTexto()
        self.ui.setupUi(self)

        self.ui.cbx_fuentes.currentIndexChanged.connect(self.cambiar_fuente)

        self.show()
    
    def cambiar_fuente(self):
        indice = self.ui.cbx_fuentes.currentIndex()
        fuente = QFont(self.ui.cbx_fuentes.itemText(indice), 15)
        self.ui.txt_editor.setFont(fuente)
    
def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionEditorTexto()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
