import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5.QtGui import QPixmap
from demo96_animacion_objeto import Ui_AnimacionObjeto

class AplicacionAnimacionObjeto(QMainWindow):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_AnimacionObjeto()
        self.ui.setupUi(self)

        imagen = 'parte17/ball.jpg'
        self.ui.lbl_imagen.setPixmap(QPixmap(imagen))

        self.ui.btn_iniciar_animacion.clicked.connect(self.iniciar_animacion)

        self.show()
    
    def iniciar_animacion(self):
        self.animacion = QPropertyAnimation(self.ui.lbl_imagen, b"geometry")
        self.animacion.setDuration(7000)
        self.animacion.setStartValue(QRect(190, 10, 96, 96))
        self.animacion.setEndValue(QRect(190, 10, 450, 450))
        self.animacion.start()

def main():
    app = QApplication(sys.argv)
    ventana = AplicacionAnimacionObjeto()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
