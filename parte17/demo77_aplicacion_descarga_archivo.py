import sys
from threading import Thread
from time import sleep

from PyQt5.QtWidgets import QApplication, QDialog
from demo77_descarga_archivo import Ui_DescargaArchivo

class AplicacionDescargaArchivo(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_DescargaArchivo()
        self.ui.setupUi(self)

        self.show()

class ProcesoDescargaArchivo(Thread):

    def __init__(self, dialogo):
        Thread.__init__(self)

        self.dialogo = dialogo
        self.contador = 0
    
    def run(self):
        while self.contador <= 100:
            sleep(1)
            self.dialogo.ui.pgr_descarga_archivo.setValue(self.contador)
            self.contador += 10

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionDescargaArchivo()

    proceso = ProcesoDescargaArchivo(dialogo)
    proceso.start()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
