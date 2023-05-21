import pickle
import os
import tkinter as tk
from tkinter import ttk
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
        self.product_menu.add_command(label="Listar", command=self.listar_productos)
        self.product_menu.add_command(label="Vender", command=self.vender_producto)
        self.product_menu.add_command(label="Buscar", command=self.buscar_producto)
        self.product_menu.add_command(label="Cambiar disponibilidad", command=self.cambiar_disponibilidad_producto)
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

    def listar_productos(self):
        listar_productos_frame = ProductosListarFrame(self.parent, self.inventario)
        listar_productos_frame.grab_set()

    def vender_producto(self):
        venta_producto_frame = ProductoVenderFrame(self.parent, self.inventario)
        venta_producto_frame.grab_set()

    def buscar_producto(self):
        buscar_producto_frame = ProductoBuscarFrame(self.parent, self.inventario)
        buscar_producto_frame.grab_set()
    
    def cambiar_disponibilidad_producto(self):
        cambiar_disponibilidad_producto_frame = ProductoCambiarDisponibilidadFrame(self.parent, self.inventario)
        cambiar_disponibilidad_producto_frame.grab_set()

    def cargar_inventario(self):
        """
        Carga el inventario desde el archivo inventario.pickle si es que existe.
        """
        if os.path.isfile('inventario/inventario.pickle'):
            self.inventario = Inventario()
            
            if messagebox.askyesno('Mensaje', '¿Desea cargar el inventario?'):
                with open('inventario/inventario.pickle', 'rb') as f:
                    resultado = pickle.load(f)
                
                if resultado:
                    self.inventario.productos = self.cargar_productos(resultado['productos']) if 'productos' in resultado else []
                    self.inventario.ventas = self.cargar_ventas(resultado['ventas']) if 'ventas' in resultado else []

    def cargar_productos(self, productos):
        """
        Carga los productos en el inventario.

        Parameters:
        productos: lista de productos a cargar en el inventario.

        Returns:
        Lista de productos cargados en el inventario.
        """
        productos_inventario = []

        for p in productos:
            producto = Producto(p['id_producto'], p['nombre'], p['precio'], p['cantidad'], p['disponible'])
            productos_inventario.append(producto)
        
        return productos_inventario

    def cargar_ventas(self, ventas):
        """
        Carga las ventas en el inventario.

        Parameters:
        ventas: lista de ventas a cargar en el inventario.

        Returns:
        Lista de ventas cargadas en el inventario.
        """
        ventas_inventario = []

        for v in ventas:
            venta = Venta(v['id_producto'], v['cantidad'], v['total_sin_iva'], v['fecha'])
            ventas_inventario.append(venta)
        
        return ventas_inventario


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
        
        producto = self.inventario.buscar_producto(codigo)

        if producto:
            messagebox.showwarning('Mensaje', 'Ya existe un producto con el código especificado.')
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

class ProductosListarFrame(tk.Toplevel):
    def __init__(self, master, inventario):
        super().__init__(master)
        self.inventario = inventario

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title("Productos")
        
        self.table = ttk.Treeview(self)
        self.table["columns"] = ("Código", "Nombre", "Precio", "Cantidad", "Disponible")
        
        self.table.heading("Código", text="Código")
        self.table.heading("Nombre", text="Nombre")
        self.table.heading("Precio", text="Precio")
        self.table.heading("Cantidad", text="Cantidad")
        self.table.heading("Disponible", text="¿Disponible?")
        
        for producto in self.inventario.productos:
            codigo = producto.codigo
            nombre = producto.nombre
            precio = producto.precio
            cantidad = producto.cantidad
            disponible = 'Sí' if producto.disponible else 'No'
            
            self.table.insert("", tk.END, values=(codigo, nombre, precio, cantidad, disponible))
        
        # Ajustar el tamaño de las columnas
        for column in ("Código", "Nombre", "Precio", "Cantidad", "Disponible"):
            self.table.column(column, width=100, anchor=tk.CENTER)
        
        # Colocar la tabla en el layout
        self.table.pack(fill=tk.BOTH, expand=True)

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
        
        button_vender = tk.Button(self, text="Vender", command=self.vender_producto)
        button_vender.grid(row=2, columnspan=2)
    
    def vender_producto(self):
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
        
        total = producto.precio * cantidad

        venta = Venta(codigo, cantidad, total)
        self.inventario.realizar_venta(venta)

        messagebox.showinfo("Mensaje", f"La venta se ha realizado de forma satisfactoria. Total a pagar: ${total * 1.19}")

        self.codigo_var.set('')
        self.cantidad_var.set('')

class ProductoBuscarFrame(tk.Toplevel):
    def __init__(self, master, inventario):
        super().__init__(master)
        self.inventario = inventario

        self.title("Producto - Buscar")

        self.inicializar_gui()

    def inicializar_gui(self):
        label_codigo = ttk.Label(self, text="Código:")
        label_nombre = ttk.Label(self, text="Nombre:")
        label_precio = ttk.Label(self, text="Precio:")
        label_cantidad = ttk.Label(self, text="Cantidad:")

        self.codigo_var = tk.IntVar()
        self.entry_codigo = ttk.Entry(self, textvariable=self.codigo_var)
        self.entry_codigo.focus()

        self.nombre_var = tk.StringVar()
        self.entry_nombre = ttk.Entry(self, textvariable=self.nombre_var)
        self.entry_nombre.state(['disabled'])

        self.precio_var = tk.DoubleVar()
        self.entry_precio = ttk.Entry(self, textvariable=self.precio_var)
        self.entry_precio.state(['disabled'])

        self.cantidad_var = tk.IntVar()
        self.entry_cantidad = ttk.Entry(self, textvariable=self.cantidad_var)
        self.entry_cantidad.state(['disabled'])

        self.disponible_var = tk.BooleanVar()
        self.checkbox_disponible = ttk.Checkbutton(self, text="Disponible para venta", variable=self.disponible_var)
        self.checkbox_disponible.state(['disabled'])

        button_buscar = ttk.Button(self, text="Buscar", command=self.buscar_producto)

        label_codigo.grid(row=0, column=0, sticky=tk.W)
        self.entry_codigo.grid(row=0, column=1)
        button_buscar.grid(row=0, column=2)

        label_nombre.grid(row=1, column=0, sticky=tk.W)
        self.entry_nombre.grid(row=1, column=1)

        label_precio.grid(row=2, column=0, sticky=tk.W)
        self.entry_precio.grid(row=2, column=1)

        label_cantidad.grid(row=3, column=0, sticky=tk.W)
        self.entry_cantidad.grid(row=3, column=1)

        self.checkbox_disponible.grid(row=4, columnspan=2, sticky=tk.W)

    def buscar_producto(self):
        codigo = self.entry_codigo.get()

        if not codigo and codigo == 0:
            messagebox.showwarning("Mensaje", "El código es obligatorio.")
            return
        
        try:
            codigo = int(codigo)
        except ValueError:
            messagebox.showwarning("Mensaje", "El código debe ser numérico.")
            return

        producto = self.inventario.buscar_producto(codigo)
        
        self.nombre_var.set('')
        self.precio_var.set('')
        self.cantidad_var.set('')
        self.disponible_var.set(False)

        if not producto:
            messagebox.showwarning("Mensaje", "El producto no existe.")
            return

        self.nombre_var.set(producto.nombre)
        self.precio_var.set(producto.precio)
        self.cantidad_var.set(producto.cantidad)
        self.disponible_var.set(producto.disponible)

class ProductoCambiarDisponibilidadFrame(tk.Toplevel):
    def __init__(self, master, inventario):
        super().__init__(master)
        self.master = master

        self.inventario = inventario

        self.inicializar_gui()

    def inicializar_gui(self):
        self.title("Producto - Cambiar Disponibilidad")
        self.minsize(300, 200)
        
        label_codigo = ttk.Label(self, text="Código:")
        self.entry_codigo = ttk.Entry(self, validate="key", validatecommand=(self.register(self.validate_integer), "%P"))

        self.estado = tk.IntVar(value=0)
        self.checkbox_disponible = ttk.Checkbutton(self, text="¿Disponible para venta?", variable=self.estado)
        self.checkbox_disponible.state(['disabled'])

        # Evento para responder al cambio del checkbox:
        self.checkbox_disponible.bind("<Button-1>", self.cambiar_estado_producto)

        button_buscar = ttk.Button(self, text="Buscar", command=self.buscar_producto)

        label_codigo.grid(row=0, column=0, sticky=tk.W)
        self.entry_codigo.grid(row=0, column=1)
        button_buscar.grid(row=1, columnspan=2)
        self.checkbox_disponible.grid(row=2, columnspan=2, sticky=tk.W)

    def validate_integer(self, value):
        # Validar que solo se ingresen números enteros en el campo de código
        if value.isdigit() or value == "":
            return True
        return False

    def buscar_producto(self):
        codigo = self.entry_codigo.get().strip()

        if len(codigo) == 0:
            messagebox.showwarning("Mensaje", "El código es obligatorio.")
            return
        
        codigo = int(codigo)

        if not codigo and codigo == 0:
            messagebox.showwarning("Mensaje", "El código es obligatorio.")
            return
        
        producto = self.inventario.buscar_producto(codigo)

        if not producto:
            self.checkbox_disponible.state(['!disabled'])
            messagebox.showwarning("Mensaje", "El producto no existe.")
            return

        current_state = self.estado.get()
        new_state = 0 if current_state == 1 else 1
        self.estado.set(new_state)

        self.checkbox_disponible.state(['!disabled'])

    def cambiar_estado_producto(self, event):
        codigo = int(self.entry_codigo.get())

        if not codigo and codigo == 0:
            messagebox.showwarning("Mensaje", "El código es obligatorio.")
            return

        producto = self.inventario.buscar_producto(codigo)

        if not producto:
            messagebox.showwarning("Mensaje", "El producto no existe.")
            return

        self.inventario.cambiar_estado_producto(producto)

    
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")

    app = VentanaPrincipal(root)
    
    app.mainloop()
