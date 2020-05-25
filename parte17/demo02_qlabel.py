import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initUi()
    
    def initUi(self):
        self.setWindowTitle('Demostración del Componente QLabel')

        self.setFixedSize(500, 400)

        self.lbl_mensaje = QLabel('¡PyQt5 es tremendo!', self)
        self.lbl_mensaje.move(100, 50)

def main():
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
