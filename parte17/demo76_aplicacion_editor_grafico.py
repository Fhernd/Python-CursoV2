import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter
from demo76_editor_grafico import Ui_EditorGrafico

class AplicacionEditorGrafico(QMainWindow):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_EditorGrafico()
        self.ui.setupUi(self)

        self.ui.mni_circulo.triggered.connect(self.dibujar_circulo)
        self.ui.mni_rectangulo.triggered.connect(self.dibujar_rectangulo)
        self.ui.mni_linea.triggered.connect(self.dibujar_linea)

        self.ui.mni_acerca_de.triggered.connect(self.mostrar_acerca_de)

        self.posicion_1 = [0, 0]
        self.posicion_2 = [0, 0]
        self.tipo_dibujo = ''

        self.show()
    
    def dibujar_circulo(self):
        self.tipo_dibujo = 'círculo'

    def dibujar_rectangulo(self):
        self.tipo_dibujo = 'rectángulo'

    def dibujar_linea(self):
        self.tipo_dibujo = 'línea'
    
    def mostrar_acerca_de(self):
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle('Acerca de...')
        mensaje.setIcon(QMessageBox.Information)
        mensaje.setText('Versión: 1.0.0\nDesarrollador: John Ortiz Ordoñez')
        mensaje.exec_()
    
    def mousePressEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.posicion_1[0], self.posicion_1[1] = event.pos().x(), event.pos().y()
    
    def mouseReleaseEvent(self, event):
        self.posicion_2[0], self.posicion_2[1] = event.pos().x(), event.pos().y()
        self.update()
    
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        if self.tipo_dibujo == 'círculo':
            ancho = self.posicion_1[0] - self.posicion_2[0]
            alto = self.posicion_1[1] - self.posicion_2[1]

            rectangulo = QRect(self.posicion_1[0], self.posicion_1[1], ancho, alto)
            angulo_inicio = 0
            longitud_arco = 360 * 16
            painter.drawArc(rectangulo, angulo_inicio, longitud_arco)
        
        if self.tipo_dibujo == 'rectángulo':
            ancho = self.posicion_2[0] - self.posicion_1[0]
            alto = self.posicion_2[1] - self.posicion_1[1]

            painter.drawRect(self.posicion_1[0], self.posicion_1[1], ancho, alto)
        
        if self.tipo_dibujo == 'línea':
            painter.drawLine(self.posicion_1[0], self.posicion_1[1], self.posicion_2[0], self.posicion_2[1])
        
        painter.end()

def main():
    app = QApplication(sys.argv)
    ventana = AplicacionEditorGrafico()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
