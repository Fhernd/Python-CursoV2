import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from demo89_posicion_puntero_mouse import Ui_VentanaPrincipal

class AplicacionPunteroMouse(QMainWindow):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_VentanaPrincipal()
        self.ui.setupUi(self)

        self.show()
    
    def mousePressEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            x = event.x()
            y = event.y()

            texto = f'El botón del mouse se presionó en x = {x}, y = {y}'

            self.ui.stt_principal.showMessage(texto, 2000)
    
    def mouseReleaseEvent(self, event):
        x = event.x()
        y = event.y()

        texto = f'El botón del mouse se soltó en x = {x}, y = {y}'

        self.ui.stt_principal.showMessage(texto, 2000)

        self.update()
    
def main():
    app = QApplication(sys.argv)
    ventana = AplicacionPunteroMouse()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
