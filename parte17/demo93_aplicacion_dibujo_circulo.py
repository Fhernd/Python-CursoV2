import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.Qt import Qt
from PyQt5.QtCore import QRect
from demo93_dibujo_circulo import Ui_DibujoCirculo

class AplicacionDibujoCirculo(QMainWindow):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_DibujoCirculo()
        self.ui.setupUi(self)

        self.show()

def main():
    app = QApplication(sys.argv)
    ventana = AplicacionDibujoCirculo()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
