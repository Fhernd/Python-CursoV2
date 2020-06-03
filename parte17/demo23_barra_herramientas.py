import sys

from PyQt5.QtWidgets import QAction, QApplication, QMainWindow, QPlainTextEdit
from PyQt5.QtGui import QIcon

class BarraHerramientasVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('Editor Básico de Texto')
        self.setFixedSize(400, 300)

        barra_herramientas = self.addToolBar('Archivo')

        nuevo_archivo = QAction(QIcon('parte17/new.png'), 'Nuevo', self)
        barra_herramientas.addAction(nuevo_archivo)

        abrir_archivo = QAction(QIcon('parte17/open.png'), 'Abrir', self)
        barra_herramientas.addAction(abrir_archivo)

        guardar_archivo = QAction(QIcon('parte17/save.png'), 'Guardar', self)
        barra_herramientas.addAction(guardar_archivo)

        self.contenido = QPlainTextEdit(self)
        self.contenido.move(10, 50)
        self.contenido.setFixedWidth(380)
        self.contenido.setFixedHeight(240)

def main():
    app = QApplication(sys.argv)
    ventana = BarraHerramientasVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
