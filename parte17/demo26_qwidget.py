import sys

from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget

class InterfazGrafica(QWidget):

    def __init__(self):
        super().__init__()

        self.inicializarGui()

    def inicializarGui(self):
        self.setWindowTitle('Interfaz Gráfica con QWidget')
        self.setFixedSize(400, 300)

        lbl_mensaje = QLabel('¡PyQt es genial!', self)
        lbl_mensaje.move(30, 30)
        lbl_mensaje.setFixedWidth(200)
        
        btn_cambiar_texto = QPushButton('Cambiar texto', self)
        btn_cambiar_texto.move(30, 90)
        btn_cambiar_texto.setFixedWidth(200)
        btn_cambiar_texto.clicked.connect(lambda _: lbl_mensaje.setText('¡Python es tremendo!'))

        txt_nombre = QLineEdit(self)
        txt_nombre.move(30, 120)
        txt_nombre.setFixedWidth(200)

def main():
    app = QApplication(sys.argv)
    widget = InterfazGrafica()
    widget.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
