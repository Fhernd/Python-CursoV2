import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QColor, QFont, QPainter
from PyQt5.Qt import Qt
from demo95_dibujo_texto import Ui_DibujoTexto

class AplicacionDibujoTexto(QMainWindow):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_DibujoTexto()
        self.ui.setupUi(self)

        self.mensaje = QMessageBox(self)
        self.mensaje.setWindowTitle('Mensaje')

        self.texto = '';
        self.fuente = 'Times New Roman'
        self.tamagnio_fuente = 8

        self.ui.btn_dibujar_texto.clicked.connect(self.dibujar_texto)

        self.show()
    
    def dibujar_texto(self):
        self.texto = self.ui.txt_texto.toPlainText()
        self.fuente = self.ui.lst_fuentes.currentItem().text()
        indice = self.ui.cbx_tamagnios.currentIndex()
        self.tamagnio_fuente = int(self.ui.cbx_tamagnios.itemText(indice))

        self.update()
    
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        painter.setPen(QColor(0, 0, 0))
        painter.setFont(QFont(self.fuente, self.tamagnio_fuente))

        painter.drawText(event.rect(), Qt.AlignBottom, self.texto)

        painter.end()

def main():
    app = QApplication(sys.argv)
    ventana = AplicacionDibujoTexto()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
