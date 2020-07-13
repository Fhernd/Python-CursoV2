import sys

from PyQt5.QtWidgets import QApplication, QDialog
from demo66_hotel import Ui_HotelSistemaReservas

class AplicacionHotel(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_HotelSistemaReservas()
        self.ui.setupUi(self)

        self.ui.btn_calcular.clicked.connect(self.mostrar_resumen)

        self.show()
    
    def mostrar_resumen(self):
        fecha = self.ui.cal_fecha_reserva.selectedDate()
        fecha_texto = str(fecha.toPyDate())
        dias = self.ui.sbx_cantidad_dias.value()
        indice = self.ui.cbx_tipo_habitacion.currentIndex()
        tipo_habitacion = self.ui.cbx_tipo_habitacion.itemText(indice)

        resumen = f"""
        Fecha: {fecha_texto}
        Días: {dias}
        Tipo habitación: {tipo_habitacion}
        """

        self.ui.txt_resumen_seleccion.setText(resumen)

        if tipo_habitacion == 'Sencilla':
            costo = 10
        elif tipo_habitacion == 'Doble':
            costo = 20
        elif tipo_habitacion == 'Queen':
            costo = 30
        else:
            costo = 40

        costo *= dias

        self.ui.txt_costo.setText(f'{costo:,}')

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionHotel()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
