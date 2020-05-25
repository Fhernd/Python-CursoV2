import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initUi()

    def initUi(self):
        self.setWindowTitle('Demostración de QPushButton')
        self.setFixedSize(500, 400)

        self.btn_mostrar_mensaje = QPushButton('Mostrar mensaje', self)
        self.btn_mostrar_mensaje.move(100, 50)
        self.btn_mostrar_mensaje.clicked.connect(self.mostrar_mensaje)
    
    def mostrar_mensaje(self):
        print('El usuario ha presionado el botón `Mostrar mensaje`.')


def main():
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
