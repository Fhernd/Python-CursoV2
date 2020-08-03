import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from googlemaps import Client
from demo99_distancia_ubicaciones import Ui_DistanciaUbicaciones

class AplicacionDistancia(QMainWindow):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_DistanciaUbicaciones()
        self.ui.setupUi(self)

        self.ui.btn_calcular.clicked.connect(self.calcular_distancia)

        self.mensaje = QMessageBox(self)
        self.setWindowTitle('Mensaje')

        self.show()
    
    def calcular_distancia(self):
        primera_ubicacion = self.ui.txt_primera_ubicacion.text().strip()

        if len(primera_ubicacion):
            segunda_ubicacion = self.ui.txt_segunda_ubicacion.text().strip()

            if len(segunda_ubicacion):
                cliente = Client(key='AIzaSyDCugQUG_8vYlrXz2URJEUgYKuOF4miIcU')

                resultado = cliente.distance_matrix(primera_ubicacion, segunda_ubicacion)

                distancia = resultado['rows'][0]['elements'][0]['distance']['text']

                self.ui.txt_distancia.setText(distancia)
            else:
                self.mensaje.setIcon(QMessageBox.Warning)
                self.mensaje.setText('El campo Segunda ubicación es obligatorio.')
                self.mensaje.exec_()
        else:
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.setText('El campo Primera ubicación es obligatorio.')
            self.mensaje.exec_()

def main():
    app = QApplication(sys.argv)
    ventana = AplicacionDistancia()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
