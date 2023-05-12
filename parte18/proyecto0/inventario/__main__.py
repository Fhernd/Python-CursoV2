import pickle
import os
import tkinter as tk
from tkinter import messagebox

from .modelos.inventario import Inventario
from .modelos.producto import Producto
from .modelos.venta import Venta


class VentanaPrincipal(tk.Frame):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        self.inicializar_gui()
        self.cargar_inventario()

    def inicializar_gui(self):
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
        registro_producto_frame = ProductoCrearFrame(self.parent, self.inventario)
        registro_producto_frame.grab_set()

    def cargar_inventario(self):
        if os.path.isfile('inventario/inventario.pickle'):
            # Usar un diálogo de confirmación para preguntar si se desea cargar el inventario:
            self.inventario = Inventario()
            
            if messagebox.askyesno('Mensaje', '¿Desea cargar el inventario?'):
                with open('inventario/inventario.pickle', 'rb') as f:
                    resultado = pickle.load(f)
                
                if resultado:
                    self.inventario.productos = resultado.productos
                    self.inventario.ventas = resultado.ventas


class ProductoCrearFrame(tk.Toplevel):
    def __init__(self, parent, inventario):
        tk.Toplevel.__init__(self, parent)

        self.inventario = inventario

        self.inicializar_gui()

    def inicializar_gui(self):
        self.title('Producto - Crear')
        
        # Variable para almacenar el inventario:
        self.codigo_var = tk.IntVar()
        codigo_label = tk.Label(self, text='Código:')
        codigo_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        codigo_entry = tk.Entry(self, textvariable=self.codigo_var)
        codigo_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.nombre_var = tk.StringVar()
        nombre_label = tk.Label(self, text='Nombre:')
        nombre_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        nombre_entry = tk.Entry(self, textvariable=self.nombre_var)
        nombre_entry.grid(row=1, column=1, padx=5, pady=5)

        self.precio_var = tk.DoubleVar()
        precio_label = tk.Label(self, text='Precio:')
        precio_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        precio_entry = tk.Entry(self, textvariable=self.precio_var)
        precio_entry.grid(row=2, column=1, padx=5, pady=5)

        self.cantidad_var = tk.IntVar()
        cantidad_label = tk.Label(self, text='Cantidad:')
        cantidad_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        cantidad_entry = tk.Entry(self, textvariable=self.cantidad_var)
        cantidad_entry.grid(row=3, column=1, padx=5, pady=5)

        self.disponible_var = tk.BooleanVar()
        disponible_checkbutton = tk.Checkbutton(self, text='Disponible para venta?', variable=self.disponible_var)
        disponible_checkbutton.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

        # Crear el botón de crear y la función asociada
        crear_button = tk.Button(self, text='Crear', command=lambda: self.crear_producto())
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

    def crear_producto(self):
        codigo = self.codigo_var.get()
        nombre = self.nombre_var.get()
        precio = self.precio_var.get()
        cantidad = self.cantidad_var.get()
        disponible = self.disponible_var.get()
        
        if not codigo or not nombre or not precio or not cantidad:
            messagebox.showwarning('Mensaje', 'Todos los campos son obligatorios. Los valores numéricos deben ser mayores a 0.')
            return
        
        try:
            codigo = int(codigo)
        except ValueError:
            messagebox.showwarning('Mensaje', 'El código debe ser numérico.')
            return

        if codigo <= 0:
            messagebox.showwarning('Mensaje', 'El código debe ser positivo.')
            return
        
        try:
            precio = float(precio)
        except ValueError:
            messagebox.showwarning('Mensaje', 'El precio debe ser numérico.')
            return

        if precio <= 0:
            messagebox.showwarning('Mensaje', 'El precio debe ser positivo.')
            return
        
        try:
            cantidad = int(cantidad)
        except ValueError:
            messagebox.showwarning('Mensaje', 'La cantidad debe ser numérica.')
            return

        if cantidad <= 0:
            messagebox.showwarning('Mensaje', 'La cantidad debe ser positiva.')
            return
        
        nuevo_producto = Producto(codigo, nombre, precio, cantidad, disponible)
        self.inventario.registrar_producto(nuevo_producto)

        messagebox.showinfo('Mensaje', 'El producto se ha creado de forma satisfactoria.')

        # Limpiar cada uno de los campos:
        self.codigo_var.set('')
        self.nombre_var.set('')
        self.precio_var.set('')
        self.cantidad_var.set('')
        self.disponible_var.set(False)
        

    def quit(self) -> None:
        """
        Cierra la aplicación.
        """
        if messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?"):
            exit()


from tkinter import Toplevel, Label, Entry, Button, Grid, IntVar

class ProductoVenderFrame(tk.Toplevel):
    def __init__(self, parent, inventario):
        super().__init__(parent)
        self.title("Venta de Producto")
        self.parent = parent
        self.inventario = inventario
        
        self.inicializar_gui()
    
    def inicializar_gui(self):
        label_codigo = tk.Label(self, text="Código:")
        label_codigo.grid(row=0, column=0)
        
        self.codigo_var = tk.IntVar()
        entry_codigo = tk.Entry(self, textvariable=self.codigo_var)
        entry_codigo.grid(row=0, column=1)
        
        label_cantidad = tk.Label(self, text="Cantidad:")
        label_cantidad.grid(row=1, column=0)
        
        self.cantidad_var = tk.IntVar()
        entry_cantidad = tk.Entry(self, textvariable=self.cantidad_var)
        entry_cantidad.grid(row=1, column=1)
        
        button_vender = tk.Button(self, text="Vender", command=lambda: self.vender_producto())
        button_vender.grid(row=2, columnspan=2)
    
    def vender_producto(self, codigo, cantidad):
        # Leer los datos de los campos:
        codigo = self.codigo_var.get()
        cantidad = self.cantidad_var.get()

        if not codigo or not cantidad:
            messagebox.showwarning("Mensaje", "Todos los campos son obligatorios. Los valores numéricos deben ser mayores a 0.")
            return

        try:
            codigo = int(codigo)
        except ValueError:
            messagebox.showwarning("Mensaje", "El código debe ser numérico.")
            return
        
        if codigo <= 0:
            messagebox.showwarning("Mensaje", "El código debe ser positivo.")
            return
        
        producto = self.inventario.buscar_producto(codigo)

        if not producto:
            messagebox.showwarning("Mensaje", "El producto no existe.")
            return

        try:
            cantidad = int(cantidad)
        except ValueError:
            messagebox.showwarning("Mensaje", "La cantidad debe ser numérica.")
            return

        if cantidad <= 0:
            messagebox.showwarning("Mensaje", "La cantidad debe ser positiva.")
            return
        
        if cantidad > producto.cantidad:
            messagebox.showwarning("Mensaje", "La cantidad solicitada es mayor a la cantidad disponible.")
            return
        
        venta = Venta(codigo, cantidad, producto.precio * cantidad)
        self.inventario.realizar_venta(venta)

        messagebox.showinfo("Mensaje", "La venta se ha realizado de forma satisfactoria.")

        self.codigo_var.set('')
        self.cantidad_var.set('')


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")

    app = VentanaPrincipal(root)
    
    app.mainloop()
