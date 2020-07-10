import sys

from PyQt5.QtWidgets import QApplication, QDialog, QInputDialog, QMessageBox, QListWidgetItem
from demo58_editor_comidas_favoritas import Ui_ComidasFavoritasEditor

class AplicacionEditorComidasFavoritas(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_ComidasFavoritasEditor()
        self.ui.setupUi(self)

        self.ui.btn_agregar.clicked.connect(self.agregar_comida)
        self.ui.btn_editar.clicked.connect(self.editar_comida)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_comida)
        self.ui.btn_eliminar_todos.clicked.connect(self.eliminar_todos)

        self.show()
    
    def agregar_comida(self):
        nombre_comida = self.ui.txt_nombre_comida_favorita.text().strip()

        if len(nombre_comida):
            self.ui.lst_comidas_favoritas.addItem(nombre_comida)
            self.ui.btn_editar.setEnabled(True)
            self.ui.btn_eliminar.setEnabled(True)
            self.ui.btn_eliminar_todos.setEnabled(True)
        else:
            mensaje = QMessageBox(self)
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setWindowTitle('Mensaje')
            mensaje.setText('El campo Nombre comida favorita es obligatorio.')

            mensaje.exec_()
    
    def editar_comida(self):
        item_seleccionado = self.ui.lst_comidas_favoritas.currentRow()

        texto, resultado = QInputDialog.getText(self, 'Editar comida favorita...', 'Ingrese el nuevo nombre:')

        if resultado and len(texto.strip()):
            self.ui.lst_comidas_favoritas.takeItem(item_seleccionado)
            self.ui.lst_comidas_favoritas.insertItem(item_seleccionado, QListWidgetItem(texto))
    
    def eliminar_comida(self):
        self.ui.lst_comidas_favoritas.takeItem(self.ui.lst_comidas_favoritas.currentRow())

    def eliminar_todos(self):
        self.ui.lst_comidas_favoritas.clear()

        self.ui.btn_editar.setEnabled(False)
        self.ui.btn_eliminar.setEnabled(False)
        self.ui.btn_eliminar_todos.setEnabled(False)

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionEditorComidasFavoritas()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
