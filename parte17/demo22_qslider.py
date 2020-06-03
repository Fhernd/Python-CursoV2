import sys

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QSlider, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class SelectorTamagnioFuenteVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('Cambio Tamaño Fuente')
        self.setFixedSize(400, 250)

        layout = QVBoxLayout()

        self.sdr_selector_tamagnio_fuente = QSlider(Qt.Horizontal)
        self.sdr_selector_tamagnio_fuente.setMinimum(10)
        self.sdr_selector_tamagnio_fuente.setMaximum(42)
        self.sdr_selector_tamagnio_fuente.setValue(18)
        self.sdr_selector_tamagnio_fuente.setTickInterval(2)
        self.sdr_selector_tamagnio_fuente.setTickPosition(QSlider.TicksBelow)
        self.sdr_selector_tamagnio_fuente.valueChanged.connect(self.cambiar_tamagnio_fuente)

        layout.addWidget(self.sdr_selector_tamagnio_fuente)

        self.lbl_python = QLabel('Python')
        self.lbl_python.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(self.lbl_python)
        
        qwidget = QWidget(self)
        self.setCentralWidget(qwidget)
        qwidget.setLayout(layout)
    
    def cambiar_tamagnio_fuente(self):
        self.lbl_python.setFont(QFont('Arial', self.sdr_selector_tamagnio_fuente.value()))

def main():
    app = QApplication(sys.argv)
    ventana = SelectorTamagnioFuenteVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
