import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class GestorAccesoriosComputador(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
        self.bd = GestionBaseDatos('demo66_componentes.db')
        self.cargar_componentes()
        self.componente_seleccionado = 0
    
    def inicializar_gui(self):
        self.title('Gestor Accesorios & Repuestos para Computador')
        self.geometry('550x340')

        frm_entrada = tk.Frame(self)
        frm_entrada.place(relx=0.05, rely=0.05, relwidth=1, relheight=0.2)

        lbl_nombre = tk.Label(frm_entrada, text='Nombre:')
        lbl_nombre.place(relx=0, rely=0, relwidth=0.25, relheight=0.5)
        self.nombre = tk.StringVar(self)
        self.txt_nombre = tk.Entry(frm_entrada, textvariable=self.nombre)
        self.txt_nombre.place(relx=0.25, rely=0, relwidth=0.25, relheight=0.5)
        
        lbl_cliente = tk.Label(frm_entrada, text='Cliente:')
        lbl_cliente.place(relx=0.5, rely=0, relwidth=0.25, relheight=0.5)
        self.cliente = tk.StringVar(self)
        self.txt_cliente = tk.Entry(frm_entrada, textvariable=self.cliente)
        self.txt_cliente.place(relx=0.70, rely=0, relwidth=0.25, relheight=0.5)
        
        lbl_tipo = tk.Label(frm_entrada, text='Tipo:')
        lbl_tipo.place(relx=0, rely=0.5, relwidth=0.25, relheight=0.5)
        self.cbx_tipo = ttk.Combobox(frm_entrada)
        tipos = ('Periférico', 'Board', 'Procesador', 'Almacenamiento', 'Red', 'Impresión', 'Otros')
        self.cbx_tipo['values'] = tipos
        self.cbx_tipo.place(relx=0.25, rely=0.5, relwidth=0.25, relheight=0.5)

        lbl_costo = tk.Label(frm_entrada, text='Costo:')
        lbl_costo.place(relx=0.5, rely=0.5, relwidth=0.25, relheight=0.5)
        self.costo = tk.StringVar(self)
        self.txt_costo = tk.Entry(frm_entrada, textvariable=self.costo)
        self.txt_costo.place(relx=0.70, rely=0.5, relwidth=0.25, relheight=0.5)

        frm_botones = tk.Frame(self)
        frm_botones.place(relx=0.025, rely=0.30, relwidth=0.95, relheight=0.1)

        btn_agregar = tk.Button(frm_botones, text='Agregar')
        btn_agregar['command'] = self.agregar
        btn_agregar.place(relx=0, rely=0, relwidth=0.25, relheight=1)
        
        btn_remover = tk.Button(frm_botones, text='Remover')
        btn_remover['command'] = self.remover
        btn_remover.place(relx=0.25, rely=0, relwidth=0.25, relheight=1)
        
        btn_actualizar = tk.Button(frm_botones, text='Actualizar')
        btn_actualizar['command'] = self.actualizar
        btn_actualizar.place(relx=0.5, rely=0, relwidth=0.25, relheight=1)
        
        btn_limpiar = tk.Button(frm_botones, text='Limpiar')
        btn_limpiar['command'] = self.limpiar
        btn_limpiar.place(relx=0.75, rely=0, relwidth=0.25, relheight=1)

        frm_lista = tk.Frame(self)
        frm_lista.place(relx=0.025, rely=0.42, relwidth=0.95, relheight=1)

        self.lbx_componentes = tk.Listbox(frm_lista)
        self.lbx_componentes.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.lbx_componentes.bind('<<ListboxSelect>>', self.seleccionar_componente)
    
    def cargar_componentes(self):
        self.lbx_componentes.delete(0, tk.END)

        componentes = self.bd.todos()

        for c in componentes:
            self.lbx_componentes.insert(tk.END, c)

    def agregar(self):
        nombre = self.nombre.get().strip()
        cliente = self.cliente.get().strip()
        tipo = self.cbx_tipo.get()
        costo = self.costo.get().strip()

        if len(nombre) == 0 or len(cliente) == 0 or len(costo) == 0:
            messagebox.showwarning('Mensaje', 'Todos los campos son obligatorios.')
            return
        
        componente = Componente(None, nombre, cliente, tipo, costo)
        
        self.bd.insertar(componente)

        self.limpiar()
        self.cargar_componentes()
    
    def remover(self):
        self.bd.remover(self.componente_seleccionado.id_)
        self.limpiar()
        self.cargar_componentes()
    
    def actualizar(self):
        nombre = self.nombre.get().strip()
        cliente = self.cliente.get().strip()
        tipo = self.cbx_tipo.get()
        costo = self.costo.get().strip()

        if len(nombre) == 0 or len(cliente) == 0 or len(costo) == 0:
            messagebox.showwarning('Mensaje', 'Todos los campos son obligatorios.')
            return
        
        id_ = self.componente_seleccionado.id_
        nombre = nombre
        cliente = cliente
        tipo = tipo
        costo = costo
        
        componente = Componente(id_, nombre, cliente, tipo, costo)

        self.bd.actualizar(id_, componente)
        self.limpiar()
        self.cargar_componentes()
    
    def limpiar(self):
        self.txt_nombre.delete(0, 'end')
        self.txt_cliente.delete(0, 'end')
        self.txt_costo.delete(0, 'end')

    def seleccionar_componente(self, event):
        try:
            indice = self.lbx_componentes.curselection()[0]
            datos = self.lbx_componentes.get(indice)

            self.componente_seleccionado = Componente(*datos)

            self.txt_nombre.delete(0, tk.END)
            self.txt_nombre.insert(tk.END, self.componente_seleccionado.nombre)
            self.txt_cliente.delete(0, tk.END)
            self.txt_cliente.insert(tk.END, self.componente_seleccionado.cliente)
            self.txt_costo.delete(0, tk.END)
            self.txt_costo.insert(tk.END, self.componente_seleccionado.costo)
            self.cbx_tipo.set(self.componente_seleccionado.tipo)
        except IndexError:
            pass

class Componente:
    def __init__(self, id_, nombre, cliente, tipo, costo):
        self.id_ = id_
        self.nombre = nombre
        self.cliente = cliente
        self.tipo = tipo
        self.costo = costo


class GestionBaseDatos:

    def __init__(self, nombre_bd):
        self.conexion = sqlite3.connect(f'parte18/{nombre_bd}')
        self.cursor = self.conexion.cursor()
        self.inicializar_bd()
    
    def inicializar_bd(self):
        ddl_tabla = """
        CREATE TABLE IF NOT EXISTS componentes(
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            cliente TEXT,
            tipo TEXT,
            costo REAL
        )
        """
        self.cursor.execute(ddl_tabla)
    
    def todos(self):
        dml_todos = """
            SELECT * FROM componentes
        """
        registros = self.cursor.execute(dml_todos).fetchall()

        return registros

    def insertar(self, componente):
        dml_insertar = """
            INSERT INTO componentes VALUES (NULL, ?, ?, ?, ?)
        """
        self.cursor.execute(dml_insertar, 
            (componente.nombre, componente.cliente, componente.tipo, componente.costo))
        
        self.conexion.commit()
    
    def remover(self, id_):
        dml_remover = """
            DELETE FROM componentes WHERE id = ?
        """
        self.cursor.execute(dml_remover, (id_,))
        self.conexion.commit()
    
    def actualizar(self, id_, componente):
        dml_actualizar = """
            UPDATE componentes SET nombre = ?, cliente = ?, tipo = ?, costo = ? WHERE id = ?
        """

        self.cursor.execute(dml_actualizar, 
                            (componente.nombre, componente.cliente, componente.tipo, componente.costo, id_))
        
        self.conexion.commit()
    
    def __del__(self):
        self.conexion.close()

def main():

    app = GestorAccesoriosComputador()
    app.mainloop()

if __name__ == '__main__':
    main()
