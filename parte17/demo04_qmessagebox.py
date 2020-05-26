import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initUi()
    
    def initUi(self):
        self.setWindowTitle('Demostración de QMessageBox')
        self.setFixedSize(500, 400)

        self.btn_mostrar_mensaje = QPushButton('Mostrar mensaje', self)
        self.btn_mostrar_mensaje.move(100, 50)
        self.btn_mostrar_mensaje.clicked.connect(self.mostrar_mensaje)
    
    def mostrar_mensaje(self):
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Information)
        mensaje.setText('Ha hecho click sobre el botón Mostrar mensaje')
        mensaje.setWindowTitle('Información')

        mensaje.exec_()


def main():
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
