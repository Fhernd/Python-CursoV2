import sys

from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QMessageBox, QPushButton

class SaludoVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('Mostrar Saludo')
        self.setFixedSize(250, 200)

        lbl_nombre = QLabel('Nombre:', self)
        lbl_nombre.move(30, 20)

        self.txt_nombre = QLineEdit(self)
        self.txt_nombre.move(30, 50)
        self.txt_nombre.setFixedWidth(190)

        self.btn_mostrar_saludo = QPushButton('Saludar', self)
        self.btn_mostrar_saludo.move(30, 100)
        self.btn_mostrar_saludo.setFixedWidth(190)
        self.btn_mostrar_saludo.clicked.connect(self.mostrar_saludo)
    
    def mostrar_saludo(self):
        nombre = self.txt_nombre.text().strip()

        mensaje = QMessageBox(self)
        mensaje.setWindowTitle('Mensaje')
        mensaje.setIcon(QMessageBox.Information)

        if len(nombre):
            saludo = f'¡Hola, {nombre}!'
            mensaje.setText(saludo)
        else:
            mensaje.setText('Debe escribir su nombre en el campo Nombre.')
            mensaje.setIcon(QMessageBox.Warning)

        mensaje.exec_()

def main():
    app = QApplication(sys.argv)
    ventana = SaludoVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
