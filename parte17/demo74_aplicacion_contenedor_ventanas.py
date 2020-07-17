import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from demo74_contenedor_ventanas import Ui_ContenedorVentanas

class AplicacionContenedorVentanas(QMainWindow):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()

    def inicializar_gui(self):
        self.ui = Ui_ContenedorVentanas()
        self.ui.setupUi(self)

        self.ui.mdi_contenedor.addSubWindow(self.ui.wdg_primera_ventana)
        self.ui.mdi_contenedor.addSubWindow(self.ui.wdg_segunda_ventana)

        self.ui.mni_tabs.triggered.connect(self.mostrar_tabs)
        self.ui.mni_cascada.triggered.connect(self.mostrar_cascada)
        self.ui.mni_cuadricula.triggered.connect(self.mostrar_cuadricula)
        self.ui.mni_subventanas.triggered.connect(self.mostrar_subventanas)

        self.show()
    
    def mostrar_tabs(self):
        self.ui.mdi_contenedor.setViewMode(1)
    
    def mostrar_cascada(self):
        self.ui.mdi_contenedor.cascadeSubWindows()
    
    def mostrar_cuadricula(self):
        self.ui.mdi_contenedor.tileSubWindows()
    
    def mostrar_subventanas(self):
        self.ui.mdi_contenedor.setViewMode(0)

def main():
    app = QApplication(sys.argv)
    ventana = AplicacionContenedorVentanas()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
