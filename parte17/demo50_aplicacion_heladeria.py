import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from demo50_heladeria import Ui_Heladeria

class AplicacionHeladeria(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_Heladeria()
        self.ui.setupUi(self)

        self.ui.chk_chocolate.stateChanged.connect(self.calcular_total)
        self.ui.chk_vainilla.stateChanged.connect(self.calcular_total)
        self.ui.chk_arequipe.stateChanged.connect(self.calcular_total)
        self.ui.chk_ron_pasas.stateChanged.connect(self.calcular_total)

        self.ui.chk_cafe.stateChanged.connect(self.calcular_total)
        self.ui.chk_agua.stateChanged.connect(self.calcular_total)
        self.ui.chk_soda.stateChanged.connect(self.calcular_total)
    
    def calcular_total(self):
        total = 0

        if self.ui.chk_chocolate.isChecked():
            total += 3
        if self.ui.chk_vainilla.isChecked():
            total += 2
        if self.ui.chk_arequipe.isChecked():
            total += 3
        if self.ui.chk_ron_pasas.isChecked():
            total += 4
        
        if self.ui.chk_cafe.isChecked():
            total += 2
        if self.ui.chk_agua.isChecked():
            total += 1
        if self.ui.chk_soda.isChecked():
            total += 3
        
        self.ui.lbl_total.setText(f'Total: ${total}')
        

def main():
    app = QApplication(sys.argv)
    ventana = AplicacionHeladeria()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
