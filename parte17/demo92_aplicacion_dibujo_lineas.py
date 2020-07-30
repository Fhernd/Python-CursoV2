import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from demo92_dibujo_lineas import Ui_DibujoLineas

class AplicacionDibujoLineas(QMainWindow):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_DibujoLineas()
        self.ui.setupUi(self)

        self.posicion_1 = [0, 0]
        self.posicion_2 = [0, 0]
        self.tipo_linea = None

        self.tipos_lineas = {0: Qt.SolidLine, 1: Qt.DashLine, 2: Qt.DashDotLine, 3: Qt.DotLine, 4: Qt.DashDotDotLine}

        self.show()
    
    def mousePressEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.posicion_1[0] = event.pos().x()
            self.posicion_1[1] = event.pos().y()
    
    def mouseReleaseEvent(self, event):
        self.tipo_linea = self.ui.lst_tipos_lineas.currentRow()

        self.posicion_2[0] = event.pos().x()
        self.posicion_2[1] = event.pos().y()

        self.update()
    
    def paintEvent(self, event):
        if self.tipo_linea is not None:
            painter = QPainter()
            painter.begin(self)

            pincel = QPen(Qt.red, 7)
            pincel.setStyle(self.tipos_lineas[self.tipo_linea])

            painter.setPen(pincel)
            painter.drawLine(self.posicion_1[0], self.posicion_1[1], self.posicion_2[0], self.posicion_2[1])

            painter.end()

def main():
    app = QApplication(sys.argv)
    ventana = AplicacionDibujoLineas()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
