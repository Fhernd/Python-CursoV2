import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from googlemaps import Client
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
        nombre_ubicacion = self.ui.txt_nombre_ubicacion.text().strip()

        if len(nombre_ubicacion):
            cliente = Client(key='AIzaSyDCugQUG_8vYlrXz2URJEUgYKuOF4miIcU')

            resultado = cliente.geocode(nombre_ubicacion)[0]

            self.ui.txt_ciudad.setText(nombre_ubicacion)
            self.ui.txt_nombre_completo_ubicacion.setText(resultado['formatted_address'])
            self.ui.txt_latitud.setText(str(resultado['geometry']['location']['lat']))
            self.ui.txt_longitud.setText(str(resultado['geometry']['location']['lng']))
        else:
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.setText('El campo Nombre ubicación es obligatorio.')
            self.mensaje.exec_()

def main():
    app = QApplication(sys.argv)
    ventana = AplicacionDatosUbicacion()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
