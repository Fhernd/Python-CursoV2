import sys

from PyQt5.QtWidgets import QApplication, QFontDialog, QLabel, QMainWindow, QPushButton

class SeleccionFuenteVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('Selección Fuente')
        self.setFixedSize(400, 250)

def main():
    app = QApplication(sys.argv)
    ventana = SeleccionFuenteVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
