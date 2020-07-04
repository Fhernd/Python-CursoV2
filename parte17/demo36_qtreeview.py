import sys

from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QVBoxLayout, QWidget

class ExploradorArchivos(QWidget):
    def __init__(self):
        super().__init__()

        self.inicializarGui()
    
    def inicializarGui(self):
        self.setWindowTitle('Explorador Archivos')
        self.setFixedSize(600, 600)

        self.modelo = QFileSystemModel()
        self.modelo.setRootPath('')

        self.explorador = QTreeView()
        self.explorador.setModel(self.modelo)

        self.explorador.setAnimated(False)
        self.explorador.setIndentation(20)
        self.explorador.setSortingEnabled(True)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.explorador)

        self.setLayout(self.layout)

        self.show()

def main():
    app = QApplication(sys.argv)
    dialogo = ExploradorArchivos()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
