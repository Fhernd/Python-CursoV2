import sys

from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QMessageBox, QPushButton

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initUi()
    
    def initUi(self):
        self.setWindowTitle('Mensaje Saludo Usuario')
        self.setFixedSize(350, 200)

        self.lbl_nombre = QLabel('Nombre: ', self)
        self.lbl_nombre.move(30, 30)

        self.txt_nombre = QLineEdit(self)
        self.txt_nombre.move(100, 30)

        self.btn_mostrar_saludo = QPushButton('Mostrar saludo', self)
        self.btn_mostrar_saludo.move(210, 30)
        self.btn_mostrar_saludo.clicked.connect(self.mostrar_saludo)
    
    def mostrar_saludo(self):
        nombre = self.txt_nombre.text().strip()

        mensaje = QMessageBox()
        mensaje.setWindowTitle('Información')

        if len(nombre):
            mensaje.setText(f'¡Hola, {nombre}!')
            mensaje.setIcon(QMessageBox.Information)
        else:
            mensaje.setText('El campo Nombre es obligatorio.')
            mensaje.setIcon(QMessageBox.Warning)
        
        mensaje.exec_()


def main():
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
