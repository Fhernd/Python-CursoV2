import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from demo57_comidas_favoritas import Ui_ComidaFavorita

class AplicacionComidasFavoritas(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_ComidaFavorita()
        self.ui.setupUi(self)

        self.ui.btn_agregar.clicked.connect(self.agregar_comida)

        self.show()
    
    def agregar_comida(self):
        nombre_comida = self.ui.txt_nombre_comida_favorita.text().strip()

        if len(nombre_comida):
            self.ui.lst_comidas_favoritas.addItem(nombre_comida)
        else:
            mensaje = QMessageBox(self)
            mensaje.setWindowTitle('Mensaje')
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setText('El campo Nombre comida favorita es obligatorio.')
            mensaje.exec_()

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionComidasFavoritas()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
