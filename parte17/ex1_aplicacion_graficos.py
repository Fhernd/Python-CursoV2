import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QRect
from ex1_graficos import Ui_Graficos

class GraficosAplicacion(QMainWindow):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_Graficos()
        self.ui.setupUi(self)

        self.ui.mniDibujarCirculo.triggered.connect(self.dibujar_circulo)
        self.ui.mniDibujarRectangulo.triggered.connect(self.dibujar_rectangulo)
        self.ui.mniDibujarLinea.triggered.connect(self.dibujar_linea)

        self.posicion_1 = [0, 0]
        self.posicion_2 = [0, 0]
        self.tipo_figura = None

        self.mensaje = QMessageBox(self)
        self.setWindowTitle('Mensaje')

        self.show()

    def dibujar_circulo(self):
        self.tipo_figura = 'circulo'

    def dibujar_rectangulo(self):
        self.tipo_figura = 'rectangulo'

    def dibujar_linea(self):
        self.tipo_figura = 'linea'
    
    def mousePressEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.posicion_1[0] = event.pos().x()
            self.posicion_1[1] = event.pos().y()
    
    def mouseReleaseEvent(self, event):
        self.posicion_2[0] = event.pos().x()
        self.posicion_2[1] = event.pos().y()

        self.update()

    def paintEvent(self, event):
        if self.tipo_figura:
            painter = QPainter()
            painter.begin(self)

            if self.tipo_figura == 'circulo':
                ancho = self.posicion_2[0] - self.posicion_1[0]
                alto = self.posicion_2[1] - self.posicion_1[1]

                rectangulo = QRect(self.posicion_1[0], self.posicion_1[1], ancho, alto)
                angulo_inicio = 0
                arco = 360 * 16
                painter.drawArc(rectangulo, angulo_inicio, arco)
                painter.end()
            if self.tipo_figura == 'rectangulo':
                ancho = self.posicion_2[0] - self.posicion_1[0]
                alto = self.posicion_2[1] - self.posicion_1[1]

                painter.drawRect(self.posicion_1[0], self.posicion_1[1], ancho, alto)
            if self.tipo_figura == 'linea':
                painter.drawLine(self.posicion_1[0], self.posicion_1[1], self.posicion_2[0], self.posicion_2[1])

def main():
    app = QApplication(sys.argv)
    ventana = GraficosAplicacion()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
