import sys

from PyQt5.QtWidgets import QApplication, QFileDialog, QLabel, QMainWindow, QPushButton
from PyQt5.QtGui import QPixmap

class SeleccionArchivoVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('Selección Archivo')
        self.setFixedSize(400, 500)

        btn_seleccionar_archivo = QPushButton('Seleccionar archivo...', self)
        btn_seleccionar_archivo.move(30, 20)
        btn_seleccionar_archivo.setFixedWidth(340)
        btn_seleccionar_archivo.clicked.connect(self.seleccionar_archivo)

        self.lbl_imagen = QLabel('', self)
        self.lbl_imagen.move(30, 40)
        self.lbl_imagen.setFixedWidth(340)
        self.lbl_imagen.setFixedHeight(340)
    
    def seleccionar_archivo(self):
        archivo, ok = QFileDialog.getOpenFileName(self, 'Seleccionar archivo de imagen...', 'C:\\', 'Archivos de imágenes (*.jpg *.png)')
        if ok:
            self.lbl_imagen.setPixmap(QPixmap(archivo))

def main():
    app = QApplication(sys.argv)
    ventana = SeleccionArchivoVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
