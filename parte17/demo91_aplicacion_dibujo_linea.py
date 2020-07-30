import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from demo91_dibujo_linea import Ui_DibujoLinea

class AplicacionDibujoLinea(QMainWindow):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()

    def inicializar_gui(self):
        self.ui = Ui_DibujoLinea()
        self.ui.setupUi(self)

        self.posicion_1 = [0, 0]
        self.posicion_2 = [0, 0]

        self.show()
    
    def mousePressEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.posicion_1[0] = event.pos().x()
            self.posicion_1[1] = event.pos().y()
    
    def mouseReleaseEvent(self, event):
        self.posicion_2[0] = event.pos().x()
        self.posicion_2[1] = event.pos().y()

        self.update()
    
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        painter.drawLine(self.posicion_1[0], self.posicion_1[1], self.posicion_2[0], self.posicion_2[1])

        painter.end()

def main():
    app = QApplication(sys.argv)
    ventana = AplicacionDibujoLinea()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
