import sys

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMessageBox, QPushButton

class EliminacionProductoVentana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initGui()
    
    def initGui(self):
        self.setWindowTitle('Eliminación Producto Por ID')
        self.setFixedSize(400, 350)


def main():
    app = QApplication(sys.argv)
    ventana = EliminacionProductoVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
