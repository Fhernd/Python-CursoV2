import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle('¡Hola, PyQt5!')

        self.setFixedSize(500, 400)


def main():
    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
