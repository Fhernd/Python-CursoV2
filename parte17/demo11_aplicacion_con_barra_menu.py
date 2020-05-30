import sys

from PyQt5.QtWidgets import QAction, QApplication, QMainWindow, QMessageBox

class AplicacionVentana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('Aplicación Principal')
        self.setFixedSize(500, 400)


def main():
    app = QApplication(sys.argv)
    ventana = AplicacionVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
