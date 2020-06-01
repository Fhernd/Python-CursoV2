import sys

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QRadioButton

class SeleccionClaseVueloVentana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('Selección Clase Vuelo')
        self.setFixedSize(350, 300)


def main():
    app = QApplication(sys.argv)
    ventana = SeleccionClaseVueloVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
