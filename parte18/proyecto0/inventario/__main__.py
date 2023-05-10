import tkinter as tk
from tkinter import messagebox

from .modelos.inventario import Inventario
from .modelos.producto import Producto
from .modelos.venta import Venta


class VentanaPrincipal(tk.Frame):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        self.parent.title("Gestor Inventario - Dispositivos S.a.s.")

        self.menu_bar = tk.Menu(self)
        
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Salir", command=self.quit)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)

        self.product_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.product_menu.add_command(label="Registrar", command=self.registrar_producto)
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
        self.parent.config(menu=self.menu_bar)

    def registrar_producto(self):
        registro_producto_frame = RegistroProductoFrame(self.parent)
        registro_producto_frame.grab_set()


class RegistroProductoFrame(tk.Toplevel):
    def __init__(self, parent=None):
        tk.Toplevel.__init__(self, parent)

        self.inicializar_gui()

    def inicializar_gui(self):
        self.title('Formulario')
        
        # Definir los campos del formulario
        codigo_label = tk.Label(self, text='Código:')
        codigo_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        codigo_entry = tk.Entry(self)
        codigo_entry.grid(row=0, column=1, padx=5, pady=5)

        nombre_label = tk.Label(self, text='Nombre:')
        nombre_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        nombre_entry = tk.Entry(self)
        nombre_entry.grid(row=1, column=1, padx=5, pady=5)

        precio_label = tk.Label(self, text='Precio:')
        precio_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        precio_entry = tk.Entry(self)
        precio_entry.grid(row=2, column=1, padx=5, pady=5)

        cantidad_label = tk.Label(self, text='Cantidad:')
        cantidad_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        cantidad_entry = tk.Entry(self)
        cantidad_entry.grid(row=3, column=1, padx=5, pady=5)

        disponible_var = tk.BooleanVar()
        disponible_checkbutton = tk.Checkbutton(self, text='Disponible para venta?', variable=disponible_var)
        disponible_checkbutton.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

        # Crear el botón de crear y la función asociada
        crear_button = tk.Button(self, text='Crear', command=lambda: self.crear_producto(codigo_entry.get(), nombre_entry.get(), precio_entry.get(), cantidad_entry.get(), disponible_var.get()))
        crear_button.grid(row=5, column=1, padx=5, pady=5, sticky=tk.E)

        # Establecer tamaño mínimo del formulario
        self.minsize(250, 250)

        # Hacer que el formulario se adapte al tamaño de la ventana anidada
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def crear_producto(self, codigo, nombre, precio, cantidad, disponible):
        # Aquí se puede implementar la lógica para crear el producto
        print('Creando producto...')
        print(f'Código: {codigo}')

    def quit(self) -> None:
        """
        Cierra la aplicación.
        """
        if messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?"):
            exit()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")

    app = VentanaPrincipal(root)
    
    app.mainloop()



def main():
    """
    Punto de entrada a la aplicación.
    """
    app = VentanaPrincipal()
    app.mainloop()


if __name__ == '__main__':
    main()
