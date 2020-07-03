import sys

from PyQt5.QtWidgets import QApplication, QDialog, QGroupBox, QHBoxLayout, QPushButton

class SeleccionColorDialogo(QDialog):
    def __init__(self):
        super().__init__()

        self.inicializarGui()

    def inicializarGui(self):
        self.setWindowTitle('Selección Color')
        self.setFixedSize(300, 150)

        self.crearBotonesSeleccionColor()

        self.show()

    def crearBotonesSeleccionColor(self):
        self.gbx_seleccion_color = QGroupBox('¿Cuál es su color favorito?')

        layout = QHBoxLayout()

        btn_color_rojo = QPushButton('Rojo', self)
        btn_color_rojo.clicked.connect(self.seleccionar_color_rojo)
        layout.addWidget(btn_color_rojo)

        btn_color_verde = QPushButton('Verde', self)
        btn_color_verde.clicked.connect(self.seleccionar_color_verde)
        layout.addWidget(btn_color_verde)

        btn_color_azul = QPushButton('Azul', self)
        btn_color_azul.clicked.connect(self.seleccionar_color_azul)
        layout.addWidget(btn_color_azul)

    def seleccionar_color_rojo(self):
        pass

    def seleccionar_color_verde(self):
        pass

    def seleccionar_colorr_azul(self):
        pass

def main():
    app = QApplication(sys.argv)
    dialogo = SeleccionColorDialogo()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
