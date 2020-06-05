import sys

from PyQt5.QtWidgets import QApplication, QLineEdit, QTabWidget, QWidget

class CapturaDatos(QTabWidget):
    def __init__(self):
        super().__init__()

        self.inicializarGui()

    def inicializarGui(self):
        self.setWindowTitle('Captura Datos Básicos')
        self.setFixedSize(300, 300)

        self.tab_datos_basicos = QWidget()
        self.tab_datos_contacto = QWidget()
        self.tab_datos_educacion = QWidget()

        self.addTab(self.tab_datos_basicos, 'Básicos')
        self.addTab(self.tab_datos_contacto, 'Contacto')
        self.addTab(self.tab_datos_educacion, 'Educación')

        self.inicializar_tab_datos_basicos()
        self.inicializar_tab_datos_contacto()
        self.inicializar_tab_datos_educacion()
    
    def inicializar_tab_datos_basicos(self):
        pass

    def inicializar_tab_datos_contacto(self):
        pass
    
    def inicializar_tab_datos_educacion(self):
        pass

def main():
    app = QApplication(sys.argv)
    ventana = CapturaDatos()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
