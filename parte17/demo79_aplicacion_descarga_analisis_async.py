import sys
import asyncio
from time import sleep

from PyQt5.QtWidgets import QApplication, QDialog
from demo79_descarga_analisis_async import Ui_DescargaAnalisisAsync

from quamash import QEventLoop

class AplicacionDescargaAnalisisAsync(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_DescargaAnalisisAsync()
        self.ui.setupUi(self)

        self.ui.btn_iniciar.clicked.connect(self.iniciar)

        self.show()
    
    def iniciar(self):
        asyncio.ensure_future(self.actualizar(0.1, self.ui.pgr_descarga_archivo))
        asyncio.ensure_future(self.actualizar(0.2, self.ui.pbr_analisis_archivo))
    
    @staticmethod
    async def actualizar(retraso, pgr_indicador_progreso):
        for i in range(101):
            sleep(retraso)
            pgr_indicador_progreso.setValue(i)

def main():
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    dialogo = AplicacionDescargaAnalisisAsync()
    dialogo.exec()

    with loop:
        loop.run_forever()
        loop.close()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
