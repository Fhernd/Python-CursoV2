import sqlite3
import tkinter as tk
import tkinter.ttk as ttk


class Producto:
    def __init__(self, id, nombre, descripcion, categoria, precio):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria
        self.precio = precio
    
    def __repr__(self) -> str:
        return f'ID: {self.id} - Nombre: {self.nombre}'


class BaseDatosProductos:
    def __init__(self):
        self.conexion = sqlite3.connect('parte18/productos.db')
        self.conexion.row_factory = sqlite3.Row

        self.cursor = self.conexion.cursor()

        self.crear_tabla_producto()
    
    def crear_tabla_producto(self):
        sql = """
        
        CREATE TABLE IF NOT EXISTS producto (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL
        )
        
        """

        self.cursor.execute(sql)
    
    def insertar(self, producto):
        sql = """
        INSERT INTO producto VALUES (?, ?, ?, ?, ?)
        """

        self.cursor.execute(sql, (producto.id, producto.nombre, producto.descripcion, producto.categoria, producto.precio))

        self.conexion.commit()
    
    def recuperar_todos(self):
        sql = """
        
        SELECT * FROM producto
        
        """

        self.cursor.execute(sql)
        registros = self.cursor.fetchall()

        productos = []

        for r in registros:
            productos.append(Producto(**dict(r)))
        
        return productos


class GestorProductos(tk.Frame):
    def __init__(self, master=None, bd=None):
        super().__init__(master)
        self.master = master
        self.bd = bd

        self.pack()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.lbl_id = tk.Label(self, text='ID:')
        self.lbl_id.grid(row=0, column=0)
        self.txt_id = tk.Entry(self)
        self.txt_id.grid(row=0, column=1)
        
        self.lbl_nombre = tk.Label(self, text='Nombre:')
        self.lbl_nombre.grid(row=1, column=0)
        self.txt_nombre = tk.Entry(self)
        self.txt_nombre.grid(row=1, column=1)
        
        self.lbl_descripcion = tk.Label(self, text='Descripción:')
        self.lbl_descripcion.grid(row=2, column=0)
        self.txt_descripcion = tk.Entry(self)
        self.txt_descripcion.grid(row=2, column=1)

        self.lbl_categoria = tk.Label(self, text='Categoría:')
        self.lbl_categoria.grid(row=3, column=0)
        self.cbx_categoria = ttk.Combobox(self, values=['Electrónicos', 'Ropa', 'Calzado', 'Herramientas', 'Otro'])
        self.cbx_categoria.grid(row=3, column=1)

        self.lbl_precio = tk.Label(self, text='Precio:')
        self.lbl_precio.grid(row=4, column=0)
        self.txt_precio = tk.Entry(self)
        self.txt_precio.grid(row=4, column=1)
    
        self.btn_agregar = tk.Button(self, text='Crear', command=self.crear_producto)
        self.btn_agregar.grid(row=5, column=0, columnspan=2)

        self.lst_productos = tk.Listbox(self, height=20, width=80)
        self.lst_productos.grid(row=6, columnspan=2)

        self.leer_productos()
    
    def crear_producto(self):
        id = self.txt_id.get()
        nombre = self.txt_nombre.get()
        descripcion = self.txt_descripcion.get()
        categoria = self.cbx_categoria.get()
        precio = self.txt_precio.get()

        producto = Producto(id, nombre, descripcion, categoria, precio)

        self.bd.insertar(producto)

        self.lst_productos.insert('end', f'{id} - {nombre} - ${precio}')

    def leer_productos(self):
        productos = self.bd.recuperar_todos()

        for p in productos:
            self.lst_productos.insert('end', f'{p.id} - {p.nombre} - ${p.precio}')

if __name__ == '__main__':
    bd = BaseDatosProductos()
    
    root = tk.Tk()
    app = GestorProductos(master=root, bd=bd)
    app.mainloop()
