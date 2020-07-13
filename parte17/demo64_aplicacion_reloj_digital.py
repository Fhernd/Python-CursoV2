import sys

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QTime, QTimer
from demo64_reloj_digital import Ui_RelojDigital

class AplicacionRelojDigital(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_RelojDigital()
        self.ui.setupUi(self)

        timer = QTimer(self)
        timer.timeout.connect(self.tick)
        timer.start(1000)
        
        self.show()
    
    def tick(self):
        hora = QTime.currentTime()
        hora_texto = hora.toString('hh:mm')

        self.ui.lcd_hora.display(hora_texto)

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionRelojDigital()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
