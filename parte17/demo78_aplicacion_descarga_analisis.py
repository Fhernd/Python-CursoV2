import sys

from threading import Thread, Lock
from time import sleep

from PyQt5.QtWidgets import QApplication, QDialog
from demo78_descarga_analisis_archivo import Ui_DescargaEscanerArchivos

bloqueo = None

class AplicacionDescargaAnalisis(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()

    def inicializar_gui(self):
        self.ui = Ui_DescargaEscanerArchivos()
        self.ui.setupUi(self)

        self.show()

class ProcesoSegundoPlano(Thread):

    def __init__(self, dialogo, pgr_indicador):
        Thread.__init__(self)

        self.dialogo = dialogo
        self.pgr_indicador = pgr_indicador
        self.contador = 0
    
    def run(self):
        bloqueo.acquire()

        while self.contador <= 100:
            sleep(1)
            self.pgr_indicador.setValue(self.contador)
            self.contador += 10
        
        bloqueo.release()

def main():
    global bloqueo
    app = QApplication(sys.argv)
    dialogo = AplicacionDescargaAnalisis()

    proceso_1 = ProcesoSegundoPlano(dialogo, dialogo.ui.pbr_descarga_archivo)
    proceso_2 = ProcesoSegundoPlano(dialogo, dialogo.ui.pbr_escaneo_archivo)

    bloqueo = Lock()
    
    proceso_1.start()
    proceso_2.start()

    dialogo.exec()

    proceso_1.join()
    proceso_2.join()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
