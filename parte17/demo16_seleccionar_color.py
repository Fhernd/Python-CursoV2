import sys

from PyQt5.QtWidgets import QApplication, QColorDialog, QLabel, QMainWindow, QPushButton
from PyQt5.QtGui import QColor

class SeleccionColorVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()

    def inicializarGui(self):
        self.setWindowTitle('Selección Color')
        self.setFixedSize(400, 300)


def main():
    app = QApplication(sys.argv)
    ventana = SeleccionColorVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
