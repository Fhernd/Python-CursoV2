import sys

from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QMessageBox, QPushButton
from PyQt5.QtGui import QIntValidator

class EliminacionProductoVentana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initGui()
    
    def initGui(self):
        self.setWindowTitle('Eliminación Producto Por ID')
        self.setFixedSize(400, 200)

        self.lbl_producto_id = QLabel('Producto ID:', self)
        self.lbl_producto_id.move(30, 30)

        self.txt_producto_id = QLineEdit(self)
        self.txt_producto_id.move(150, 30)
        self.txt_producto_id.setValidator(QIntValidator())
        self.txt_producto_id.setFixedWidth(200)

        self.btn_eliminar_producto = QPushButton('Eliminar', self)
        self.btn_eliminar_producto.move(150, 70)
        self.btn_eliminar_producto.setFixedWidth(200)
        self.btn_eliminar_producto.clicked.connect(self.eliminar_producto)

        self.lbl_resultado = QLabel('Resultado:', self)
        self.lbl_resultado.move(30, 120)

        self.txt_resultado = QLineEdit(self)
        self.txt_resultado.move(150, 120)
        self.txt_resultado.setFixedWidth(200)
        self.txt_resultado.setEnabled(False)

    def eliminar_producto(self):
        confirmacion = QMessageBox()
        confirmacion.setText('¿Está seguro de querer eliminar este producto?')
        confirmacion.setIcon(QMessageBox.Question)
        confirmacion.setWindowTitle('Confirmación')
        confirmacion.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        boton_yes = confirmacion.button(QMessageBox.Yes)

        confirmacion.exec_()

        if confirmacion.clickedButton() == boton_yes:
            self.txt_resultado.setText('Se ha eliminado el producto con ID {}.'.format(self.txt_producto_id.text()))
        else:
            self.txt_resultado.setText('No se ha eliminado el producto.')

def main():
    app = QApplication(sys.argv)
    ventana = EliminacionProductoVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
