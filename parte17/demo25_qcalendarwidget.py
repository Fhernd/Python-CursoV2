import sys

from PyQt5.QtWidgets import QApplication, QCalendarWidget, QLabel, QMainWindow
from PyQt5.QtCore import QDate

class SelectorFechaVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('Selector Fecha')
        self.setFixedSize(300, 300)

        self.calendario = QCalendarWidget(self)
        self.calendario.setGridVisible(True)
        self.calendario.move(30, 20)
        self.calendario.setFixedWidth(200)
        self.calendario.setFixedHeight(200)
        self.calendario.clicked[QDate].connect(self.mostrar_fecha_seleccionada)

        self.lbl_fecha_seleccionada = QLabel('', self)
        self.lbl_fecha_seleccionada.move(30, 220)
        self.lbl_fecha_seleccionada.setFixedWidth(250)
    
    def mostrar_fecha_seleccionada(self, fecha):
        self.lbl_fecha_seleccionada.setText(fecha.toString())


def main():
    app = QApplication(sys.argv)
    ventana = SelectorFechaVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
