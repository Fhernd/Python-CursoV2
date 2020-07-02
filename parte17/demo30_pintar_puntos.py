import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtCore import Qt

class LienzoDibujoVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('Lienzo Puntos Aleatorios')
        self.setFixedSize(400, 400)

        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(paleta)

class DibujoWidget(QWidget):
    def paintEvent(self, evento):
        painter = QPainter(self)
        painter.setPen(Qt.black)

        tamagnio = self.size()
        

def main():
    app = QApplication(sys.argv)
    ventana = LienzoDibujoVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
