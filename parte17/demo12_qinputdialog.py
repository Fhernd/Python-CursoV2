import sys

from PyQt5.QtWidgets import QApplication, QInputDialog, QLabel, QLineEdit, QMainWindow, QPushButton

class CapturaDatosVentana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('Captura de Datos - QInputDialog')
        self.setFixedSize(400, 500)

        


def main():
    app = QApplication(sys.argv)
    ventana = CapturaDatosVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
