import sys

from PyQt5.QtWidgets import QApplication, QCheckBox, QLabel, QMainWindow

class PizzaVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()

    def inicializarGui(self):
        self.setWindowTitle('Pizza & Ingredientes')
        self.setFixedSize(400, 350)


def main():
    app = QApplication(sys.argv)
    ventana = PizzaVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
