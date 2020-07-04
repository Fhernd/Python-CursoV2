import sys

from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QGroupBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import pyqtSlot

class CalculadoraDialogo(QDialog):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('QGridLayout')
        self.setFixedSize(300, 150)

        self.crearBotones()

        layout = QVBoxLayout()
        layout.addWidget(self.gbx_controles)
        self.setLayout(layout)

        self.show()
    
    def crearBotones(self):
        self.gbx_controles = QGroupBox('Botones')
        layout = QGridLayout()

        btn_uno = QPushButton('1')
        btn_uno.clicked.connect(self.click)
        layout.addWidget(btn_uno, 0, 0)
        
        layout.addWidget(QPushButton('2'), 0, 1)
        layout.addWidget(QPushButton('3'), 0, 2)
        layout.addWidget(QPushButton('4'), 1, 0)
        layout.addWidget(QPushButton('5'), 1, 1)
        layout.addWidget(QPushButton('6'), 1, 2)
        layout.addWidget(QPushButton('7'), 2, 0)
        layout.addWidget(QPushButton('8'), 2, 1)
        layout.addWidget(QPushButton('9'), 2, 2)

        self.gbx_controles.setLayout(layout)
    
    @pyqtSlot()
    def click(self):
        print('Se ha presionado un botón.')

def main():
    app = QApplication(sys.argv)
    dialogo = CalculadoraDialogo()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
