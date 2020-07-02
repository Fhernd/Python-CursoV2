import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

class TablaDatosVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('Tabla de Datos')
        self.setFixedSize(400, 400)

        self.crearTabla()

    def crearTabla(self):
        self.tbl_datos = QTableWidget()
        self.tbl_datos.setRowCount(5)
        self.tbl_datos.setColumnCount(3)

        self.tbl_datos.setItem(0, 0, QTableWidgetItem('Dato 1'))
        self.tbl_datos.setItem(0, 1, QTableWidgetItem('Dato 2'))
        self.tbl_datos.setItem(0, 2, QTableWidgetItem('Dato 3'))
        self.tbl_datos.setItem(1, 0, QTableWidgetItem('Dato 4'))
        self.tbl_datos.setItem(1, 1, QTableWidgetItem('Dato 5'))
        self.tbl_datos.setItem(1, 2, QTableWidgetItem('Dato 6'))
        self.tbl_datos.setItem(1, 0, QTableWidgetItem('Dato 4'))
        self.tbl_datos.setItem(1, 1, QTableWidgetItem('Dato 5'))
        self.tbl_datos.setItem(1, 2, QTableWidgetItem('Dato 6'))

def main():
    app = QApplication(sys.argv)
    ventana = TablaDatosVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
