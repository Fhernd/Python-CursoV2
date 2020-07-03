import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtCore import Qt

class ColoresVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('Colores')
        self.setFixedSize(440, 280)

        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(paleta)

        self.dibujo = DibujoWidget(self)
        self.dibujo.move(0, 0)
        self.dibujo.resize(440, 280)

class DibujoWidget(QWidget):
    def paintEvent(self, evento):
        painter = QPainter(self)
        painter.setPen(Qt.black)

        painter.setBrush(QColor(200, 0, 0))
        painter.drawRect(0, 0, 100, 100)

        painter.setBrush(QColor(0, 200, 0))
        painter.drawRect(100, 0, 100, 100)

        painter.setBrush(QColor(0, 0, 200))
        painter.drawRect(200, 0, 100, 100)

        for i in range(100):
            painter.setBrush(QColor(10*i, 0, 0))
            painter.drawRect(10*i, 100, 10, 32)

            painter.setBrush(QColor(10*i, 10*i, 0))
            painter.drawRect(10*i, 100+32, 10, 32)

            painter.setBrush(QColor(2*i, 10*i, i))
            painter.drawRect(10*i, 100+64, 10, 32)

def main():
    app = QApplication(sys.argv)
    ventana = ColoresVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
