import sys

from PyQt5.QtWidgets import QApplication, QInputDialog, QLabel, QLineEdit, QMainWindow, QPushButton

class CapturaDatosVentana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('Captura de Datos - QInputDialog')
        self.setFixedSize(400, 440)

        self.btn_nombre = QPushButton('Capturar nombre', self)
        self.btn_nombre.move(100, 30)
        self.btn_nombre.setFixedWidth(200)
        self.btn_nombre.clicked.connect(self.capturar_nombre)

        self.btn_edad = QPushButton('Capturar edad', self)
        self.btn_edad.move(100, 70)
        self.btn_edad.setFixedWidth(200)
        self.btn_edad.clicked.connect(self.capturar_edad)

        self.btn_ahorros = QPushButton('Capturar ahorros', self)
        self.btn_ahorros.move(100, 110)
        self.btn_ahorros.setFixedWidth(200)
        self.btn_ahorros.clicked.connect(self.capturar_ahorros)

        self.btn_color = QPushButton('Capturar color', self)
        self.btn_color.move(100, 150)
        self.btn_color.setFixedWidth(200)
        self.btn_color.clicked.connect(self.capturar_color)

        lbl_resumen = QLabel('Resumen:', self)
        lbl_resumen.move(180, 220)

        lbl_nombre = QLabel('Nombre:', self)
        lbl_nombre.move(30, 270)

        self.txt_nombre = QLineEdit(self)
        self.txt_nombre.move(170, 270)
        self.txt_nombre.setFixedWidth(200)
        self.txt_nombre.setEnabled(False)

        lbl_edad = QLabel('Edad:', self)
        lbl_edad.move(30, 310)

        self.txt_edad = QLineEdit(self)
        self.txt_edad.move(170, 310)
        self.txt_edad.setFixedWidth(200)
        self.txt_edad.setEnabled(False)

        lbl_ahorros = QLabel('Ahorros:', self)
        lbl_ahorros.move(30, 350)

        self.txt_ahorros = QLineEdit(self)
        self.txt_ahorros.move(170, 350)
        self.txt_ahorros.setFixedWidth(200)
        self.txt_ahorros.setEnabled(False)

        lbl_color = QLabel('Color:', self)
        lbl_color.move(30, 390)

        self.txt_color = QLineEdit(self)
        self.txt_color.move(170, 390)
        self.txt_color.setFixedWidth(200)
        self.txt_color.setEnabled(False)
    
    def capturar_nombre(self):
        nombre, ok = QInputDialog.getText(self, 'Captura de datos', 'Escriba su nombre:')

        if ok:
            nombre = nombre.strip()

            if len(nombre):
                self.txt_nombre.setText(nombre)

    def capturar_edad(self):
        edad, ok = QInputDialog.getInt(self, 'Captura de datos', 'Escriba su edad:', 10, 1, 80)

        if ok:
            self.txt_edad.setText(str(edad))

    def capturar_ahorros(self):
        ahorros, ok = QInputDialog.getDouble(self, 'Captura de datos', 'Escriba la cantidad de ahorros:', 0, 1, 1000000)

        if ok:
            self.txt_ahorros.setText(str(ahorros))

    def capturar_color(self):
        colores = ['Rojo', 'Verde', 'Azul', 'Blanco', 'Regro', 'Gris', 'Amarillo']

        color, ok = QInputDialog.getItem(self, 'Captura de datos', 'Seleccione su color favorito:', colores, 0, False)

        if ok:
            self.txt_color.setText(color)

def main():
    app = QApplication(sys.argv)
    ventana = CapturaDatosVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
