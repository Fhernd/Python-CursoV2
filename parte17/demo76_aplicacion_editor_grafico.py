import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from demo76_editor_grafico import Ui_EditorGrafico

class AplicacionEditorGrafico(QMainWindow):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_EditorGrafico()
        self.ui.setupUi(self)

        self.ui.mni_circulo.triggered.connect(self.dibujar_circulo)
        self.ui.mni_rectangulo.triggered.connect(self.dibujar_rectangulo)
        self.ui.mni_linea.triggered.connect(self.dibujar_linea)

        self.ui.mni_acerca_de.triggered.connect(self.mostrar_acerca_def)

        self.show()
    
    def dibujar_circulo(self):
        pass

    def dibujar_rectangulo(self):
        pass

    def dibujar_linea(self):
        pass
    
    def mostrar_acerca_def(self):
        pass

def main():
    app = QApplication(sys.argv)
    ventana = AplicacionEditorGrafico()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
