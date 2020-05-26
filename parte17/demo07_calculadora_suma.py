import sys

from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QMessageBox, QPushButton

class CalculadoraVentana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initUi()
    
    def initUi(self):
        self.setWindowTitle('Calculadora Básica')
        self.setFixedSize(400, 350)


def main():
    app = QApplication(sys.argv)
    calculadora = CalculadoraVentana()
    calculadora.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
