import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
from PyQt5 import uic

class Aplicacion(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        uic.loadUi('parte17/demo38_saludo_qt_designer.ui', self)

        self.btn_saludar = self.findChild(QPushButton, 'btn_saludar')
        self.btn_saludar.clicked.connect(self.saludar)

        self.show()
    
    def saludar(self):
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle('Mensaje')
        mensaje.setIcon(QMessageBox.Information)
        mensaje.setText('¡Hola usuario!')
        mensaje.exec_()

def main():
    app = QApplication(sys.argv)
    ventana = Aplicacion()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
