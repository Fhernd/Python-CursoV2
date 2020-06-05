import sys

from PyQt5.QtWidgets import QApplication, QLabel, QListWidget, QMainWindow

class ListaLenguajesVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('Lista de Lenguajes de Programación')
        self.setFixedSize(360, 360)

        self.lst_lenguajes = QListWidget(self)
        self.lst_lenguajes.move(30, 20)
        self.lst_lenguajes.setFixedWidth(300)
        self.lst_lenguajes.setFixedHeight(300)
        self.lst_lenguajes.insertItem(0, 'Python')
        self.lst_lenguajes.insertItem(1, 'JavaScript')
        self.lst_lenguajes.insertItem(2, 'C#')
        self.lst_lenguajes.insertItem(3, 'Java')
        self.lst_lenguajes.insertItem(4, 'C++')
        self.lst_lenguajes.insertItem(5, 'PHP')
        self.lst_lenguajes.insertItem(6, 'C')
        self.lst_lenguajes.clicked.connect(self.mostrar_lenguaje_seleccionado)

        self.lbl_lenguaje_seleccionado = QLabel('', self)
        self.lbl_lenguaje_seleccionado.move(30, 330)
        self.lbl_lenguaje_seleccionado.setFixedWidth(300)
    
    def mostrar_lenguaje_seleccionado(self):
        lenguaje = self.lst_lenguajes.currentItem()
        self.lbl_lenguaje_seleccionado.setText(lenguaje.text())

def main():
    app = QApplication(sys.argv)
    ventana = ListaLenguajesVentana()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
