import tkinter as tk
from tkinter import messagebox

from .modelos.inventario import Inventario
from .modelos.producto import Producto
from .modelos.venta import Venta


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor Inventario - Dispositivos S.a.s.")

        self.geometry("500x500")

        self.menu_bar = tk.Menu(self)
        
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Salir", command=self.quit)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)

        self.product_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.product_menu.add_command(label="Registrar")
        self.product_menu.add_command(label="Vender")
        self.product_menu.add_command(label="Buscar")
        self.product_menu.add_command(label="Cambiar disponibilidad")
        self.menu_bar.add_cascade(label="Productos", menu=self.product_menu)
        self.report_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.report_menu.add_command(label="Ventas en un rango de fechas")
        self.report_menu.add_command(label="Top 5 de productos más vendidos")
        self.report_menu.add_command(label="Top 5 de productos menos vendidos")
        self.menu_bar.add_cascade(label="Reportes", menu=self.report_menu)
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Acerca de")
        self.menu_bar.add_cascade(label="Ayuda", menu=self.help_menu)
        self.config(menu=self.menu_bar)
        
    def quit(self) -> None:
        """
        Cierra la aplicación.
        """
        if messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?"):
            exit()


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()



def main():
    """
    Punto de entrada a la aplicación.
    """
    app = VentanaPrincipal()
    app.mainloop()


if __name__ == '__main__':
    main()
