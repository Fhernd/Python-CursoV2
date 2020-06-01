import sys

from PyQt5.QtWidgets import QApplication, QColorDialog, QLabel, QMainWindow, QPushButton
from PyQt5.QtGui import QColor

class SeleccionColorVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()

    def inicializarGui(self):
        self.setWindowTitle('Selección Color')
        self.setFixedSize(400, 200)

        self.btn_seleccionar_color = QPushButton('Seleccionar color...', self)
        self.btn_seleccionar_color.move(100, 30)
        self.btn_seleccionar_color.setFixedWidth(200)
        self.btn_seleccionar_color.clicked.connect(self.seleccionar_color)

        self.lbl_resultado_seleccion = QLabel('', self)
        self.lbl_resultado_seleccion.move(190, 100)
        self.lbl_resultado_seleccion.setFixedWidth(100)
    
    def seleccionar_color(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.lbl_resultado_seleccion.setText(color.name())
            self.lbl_resultado_seleccion.setStyleSheet(f'color: {color.name()}')

def main():
    app = QApplication(sys.argv)
    ventana = SeleccionColorVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
