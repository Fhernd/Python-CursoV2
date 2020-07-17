import sys

from PyQt5.QtWidgets import QApplication, QDialog
from demo75_restaurante_pedidos import Ui_RestaurantePedidos

class AplicacionRestaurantePedidos(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_RestaurantePedidos()
        self.ui.setupUi(self)

        self.show()

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionRestaurantePedidos()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
