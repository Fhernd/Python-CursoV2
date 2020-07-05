import sys

from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QWidget

class ArrastrarSoltarDialogo(QWidget):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('Arrastrar & Soltar')
        self.setFixedSize(400, 200)

        self.txt_entrada = QLineEdit('Arrastre este texto a la etiqueta', self)
        self.txt_entrada.setDragEnabled(True)
        self.txt_entrada.move(20, 30)
        self.txt_entrada.resize(200, 32)

        self.show()

class ContenedorLabel(QLabel):
    def __init__(self, texto, padre):
        super().__init__(texto, padre)
        self.setAcceptDrops(True)

def main():
    app = QApplication(sys.argv)
    dialogo = ArrastrarSoltarDialogo()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
