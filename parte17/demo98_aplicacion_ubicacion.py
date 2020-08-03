import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QDoubleValidator
from googlemaps import Client
from demo98_ubicacion_latitud_longitud import Ui_UbicacionLatitudLongitud

class AplicacionUbicacion(QMainWindow):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_UbicacionLatitudLongitud()
        self.ui.setupUi(self)

        self.ui.txt_latitud.setValidator(QDoubleValidator(-90, 90, 7))
        self.ui.txt_longitud.setValidator(QDoubleValidator(-180, 180, 7))

        self.ui.btn_buscar.clicked.connect(self.buscar)

        self.mensaje = QMessageBox(self)
        self.mensaje.setWindowTitle('Mensaje')

        self.show()
    
    def buscar(self):
        latitud = self.ui.txt_latitud.text().strip()

        if len(latitud):
            longitud = self.ui.txt_longitud.text().strip()

            if len(longitud):
                cliente = Client(key='AIzaSyDCugQUG_8vYlrXz2URJEUgYKuOF4miIcU')

                resultado = cliente.reverse_geocode((latitud, longitud))

                if len(resultado):
                    ciudad = resultado[1]['address_components'][2]['long_name']
                    departamento = resultado[1]['address_components'][4]['long_name']
                    pais = resultado[1]['address_components'][5]['long_name']
                    nombre_completo_ubicacion = resultado[0]['formatted_address']

                    self.ui.txt_ciudad.setText(ciudad)
                    self.ui.txt_departamento.setText(departamento)
                    self.ui.txt_pais.setText(pais)
                    self.ui.txt_nombre_completo_ubicacion.setText(nombre_completo_ubicacion)
                else:
                    self.mensaje.setIcon(QMessageBox.Warning)
                    self.mensaje.setText('No hay resultados para la latitud y longitud especificados.')
                    self.mensaje.exec_() 
            else:
                self.mensaje.setIcon(QMessageBox.Warning)
                self.mensaje.setText('El campo Longitud es obligatorio.')
                self.mensaje.exec_()
        else:
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.setText('El campo Latitud es obligatorio.')
            self.mensaje.exec_()

def main():
    app = QApplication(sys.argv)
    ventana = AplicacionUbicacion()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
