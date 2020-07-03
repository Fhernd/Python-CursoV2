import sys

from PyQt5.QtWidgets import QApplication, QDialog, QGroupBox, QHBoxLayout, QMessageBox, QPushButton, QVBoxLayout

class SeleccionColorDialogo(QDialog):
    def __init__(self):
        super().__init__()

        self.inicializarGui()

    def inicializarGui(self):
        self.setWindowTitle('Selección Color')
        self.setFixedSize(300, 150)

        self.crearBotonesSeleccionColor()

        layout = QVBoxLayout()
        layout.addWidget(self.gbx_seleccion_color)
        self.setLayout(layout)

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

        self.gbx_seleccion_color.setLayout(layout)

    def seleccionar_color_rojo(self):
        self.mostrar_mensaje('rojo')

    def seleccionar_color_verde(self):
        self.mostrar_mensaje('verde')

    def seleccionar_color_azul(self):
        self.mostrar_mensaje('azul')

    def mostrar_mensaje(self, color):
        mensaje = QMessageBox(self)
        mensaje.setIcon(QMessageBox.Information)
        mensaje.setWindowTitle('Mensaje')
        mensaje.setText(f'Ud. ha seleccionado el color {color}.')

        mensaje.exec_()

def main():
    app = QApplication(sys.argv)
    dialogo = SeleccionColorDialogo()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
