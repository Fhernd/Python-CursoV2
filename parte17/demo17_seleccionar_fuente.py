import sys

from PyQt5.QtWidgets import QApplication, QFontDialog, QLabel, QMainWindow, QPushButton

class SeleccionFuenteVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('Selección Fuente')
        self.setFixedSize(400, 250)

        self.btn_seleccionar_fuente = QPushButton('Seleccionar fuente...', self)
        self.btn_seleccionar_fuente.move(100, 30)
        self.btn_seleccionar_fuente.setFixedWidth(200)
        self.btn_seleccionar_fuente.clicked.connect(self.seleccionar_fuente)

        self.lbl_resultado_seleccion = QLabel('', self)
        self.lbl_resultado_seleccion.move(30, 150)
        self.lbl_resultado_seleccion.setFixedWidth(250)

    def seleccionar_fuente(self):
        fuente, ok = QFontDialog.getFont()

        if ok:
            self.lbl_resultado_seleccion.setText(fuente.toString())
            self.lbl_resultado_seleccion.setFont(fuente)

def main():
    app = QApplication(sys.argv)
    ventana = SeleccionFuenteVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
