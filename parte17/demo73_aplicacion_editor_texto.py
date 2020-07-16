import sys

from PyQt5.QtWidgets import QAction, QApplication, QFileDialog, QMainWindow
from demo73_editor_texto import Ui_EditorTexto

class AplicacionEditorTexto(QMainWindow):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_EditorTexto()
        self.ui.setupUi(self)

        self.ui.mni_abrir.triggered.connect(self.abrir)
        self.ui.mni_guardar.triggered.connect(self.guardar)
        self.ui.mni_salir.triggered.connect(self.salir)

        self.show()
    
    def abrir(self):
        archivo = QFileDialog.getOpenFileName(self, 'Abrir archivo0...', 'C:\\', 'Text files (.txt)')

        if archivo[0]:
            with open(archivo[0], 'rt') as f:
                contenido = f.read()

                self.ui.txt_contenido.insertPlainText(contenido)
    
    def guardar(self):
        opciones = QFileDialog.Options()
        opciones |= QFileDialog.DontUseNativeDialog

        archivo, _ = QFileDialog.getSaveFileName(self, 'Guardar archivo...', 'C:\\', 'Text files (.txt)', options=opciones)

        with open(archivo, 'wt') as f:
            f.write(self.ui.txt_contenido.toPlainText())
    
    def salir(self):
        sys.exit(0)

def main():
    app = QApplication(sys.argv)
    ventana =  AplicacionEditorTexto()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
