import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from demo97_datos_ubicacion import Ui_DatosUbicacion

class AplicacionDatosUbicacion(QMainWindow):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_DatosUbicacion()
        self.ui.setupUi(self)

        self.mensaje = QMessageBox(self)
        self.mensaje.setWindowTitle('Mensaje')

        self.ui.btn_buscar.clicked.connect(self.buscar)

        self.show()
    
    def buscar(self):
        pass

def main():
    app = QApplication(sys.argv)
    ventana = AplicacionDatosUbicacion()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
