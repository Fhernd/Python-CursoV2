import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from demo49_inicio_sesion import Ui_InicioSesion

class AplicacionInicioSesion(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_InicioSesion()
        self.ui.setupUi(self)

        self.ui.btn_iniciar_sesion.clicked.connect(self.iniciar_sesion)

        self.show()
    
    def iniciar_sesion(self):
        nombre_usuario = self.ui.txt_nombre_usuario.text().strip()
        contrasegnia = self.ui.txt_contrasegnia.text().strip()
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle('Mensaje')

        if len(nombre_usuario) and len(contrasegnia):
            if nombre_usuario == 'johnlrnr' and contrasegnia == 'J0hN':
                mensaje.setIcon(QMessageBox.Information)
                mensaje.setText('Ha iniciado sesión.')
            else:
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.setText('Las credenciales escritas no son válidas. Intente nuevamente.')
        else:
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setText('Todos los campos son obligatorios.')
        
        mensaje.exec_()

def main():
    app = QApplication(sys.argv)
    ventana = AplicacionInicioSesion()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
