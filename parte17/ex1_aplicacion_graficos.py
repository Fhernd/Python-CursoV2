import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from ex1_graficos import Ui_Graficos

class GraficosAplicacion(QMainWindow):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_Graficos()
        self.ui.setupUi(self)

        self.show()

def main():
    app = QApplication(sys.argv)
    ventana = GraficosAplicacion()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
