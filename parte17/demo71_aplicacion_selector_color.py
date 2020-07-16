import sys

from PyQt5.QtWidgets import QApplication, QColorDialog, QDialog
from demo71_selector_color import Ui_SelectorColor

class AplicacionSelectorColor(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()

    def inicializar_gui(self):
        self.ui = Ui_SelectorColor()
        self.ui.setupUi(self)

        self.ui.btn_seleccionar_color.clicked.connect(self.cambiar_color)

        self.show()
    
    def cambiar_color(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.ui.frm_color_selecciondo.setStyleSheet("QWidget {background-color: %s}" % color.name())
            self.ui.lbl_color_seleccionado.setText(str(color.name()))

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionSelectorColor()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
