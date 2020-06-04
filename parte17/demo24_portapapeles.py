import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QPushButton
from PyQt5.QtGui import QClipboard

class GestorPortapapelesVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('Gestor Portapapeles')
        self.setFixedSize(400, 300)

        self.txt_texto_fuente = QPlainTextEdit(self)
        self.txt_texto_fuente.move(30, 10)
        self.txt_texto_fuente.setFixedWidth(340)
        self.txt_texto_fuente.setFixedHeight(100)

        self.btn_copiar = QPushButton('Copiar', self)
        self.btn_copiar.move(30, 110)
        self.btn_copiar.setFixedWidth(340)
        self.btn_copiar.clicked.connect(self.copiar)

        self.txt_texto_destino = QPlainTextEdit(self)
        self.txt_texto_destino.move(30, 150)
        self.txt_texto_destino.setFixedWidth(340)
        self.txt_texto_destino.setFixedHeight(100)

        self.btn_pegar = QPushButton('Pegar', self)
        self.btn_pegar.move(30, 250)
        self.btn_pegar.setFixedWidth(340)
        self.btn_pegar.clicked.connect(self.pegar)

    def copiar(self):
        self.txt_texto_fuente.copy()

    def pegar(self):
        self.txt_texto_destino.paste()


def main():
    app = QApplication(sys.argv)
    ventana = GestorPortapapelesVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
