import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from demo45_saludo import Ui_SaludoVentana

class AplicacionSaludoVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()

    def inicializarGui(self):
        self.ui = Ui_SaludoVentana()
        self.ui.setupUi(self)

        self.ui.btn_saludar.clicked.connect(self.saludar)

        self.show()
    
    def saludar(self):
        nombre = self.ui.txt_nombre.text().strip()

        mensaje = QMessageBox(self)
        mensaje.setWindowTitle('Mensaje')

        if len(nombre):
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setText(f'¡Hola, {nombre}!')
        else:
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setText('Debe escribir un nombre.')
        
        mensaje.exec_()

def main():
    app = QApplication(sys.argv)
    ventana = AplicacionSaludoVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
