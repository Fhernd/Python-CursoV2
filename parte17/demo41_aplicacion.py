import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from demo40_traduccion_gui import Ui_MainWindow

class Aplicacion(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_saludar.clicked.connect(self.saludar)
    
    def saludar(self):
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle('Mensaje')
        mensaje.setIcon(QMessageBox.Information)
        mensaje.setText('¡Hola, usuario!')

        mensaje.exec_()

def main():
    app = QApplication(sys.argv)
    ventana = Aplicacion()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
