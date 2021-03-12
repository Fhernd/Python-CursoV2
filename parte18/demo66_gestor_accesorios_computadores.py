import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class GestorAccesoriosComputador(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Gestor Accesorios & Repuestos para Computador')
        self.geometry('550x340')

        frm_entrada = tk.Frame(self)
        frm_entrada.place(relx=0.05, rely=0.05, relwidth=1, relheight=0.2)

        lbl_nombre = tk.Label(frm_entrada, text='Nombre:')
        lbl_nombre.place(relx=0, rely=0, relwidth=0.25, relheight=0.5)
        self.txt_nombre = tk.Entry(frm_entrada)
        self.txt_nombre.place(relx=0.25, rely=0, relwidth=0.25, relheight=0.5)
        
        lbl_cliente = tk.Label(frm_entrada, text='Cliente:')
        lbl_cliente.place(relx=0.5, rely=0, relwidth=0.25, relheight=0.5)
        self.txt_cliente = tk.Entry(frm_entrada)
        self.txt_cliente.place(relx=0.70, rely=0, relwidth=0.25, relheight=0.5)
        
        lbl_tipo = tk.Label(frm_entrada, text='Tipo:')
        lbl_tipo.place(relx=0, rely=0.5, relwidth=0.25, relheight=0.5)
        self.cbx_tipo = ttk.Combobox(frm_entrada)
        tipos = ('Periférico', 'Board', 'Procesador', 'Almacenamiento', 'Red', 'Impresión', 'Otros')
        self.cbx_tipo['values'] = tipos
        self.cbx_tipo.place(relx=0.25, rely=0.5, relwidth=0.25, relheight=0.5)

        lbl_costo = tk.Label(frm_entrada, text='Costo:')
        lbl_costo.place(relx=0.5, rely=0.5, relwidth=0.25, relheight=0.5)
        self.txt_costo = tk.Entry(frm_entrada)
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

        lbx_componentes = tk.Listbox(frm_lista)
        lbx_componentes.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    def agregar(self):
        pass
    
    def remover(self):
        pass
    
    def actualizar(self):
        pass
    
    def limpiar(self):
        self.txt_nombre.delete(0, 'end')
        self.txt_cliente.delete(0, 'end')
        self.txt_costo.delete(0, 'end')


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
            tipo TEXT
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
            INSERT INTO componentes VALUES (NULL, ?, ?, ?)
        """
        self.cursor.execute(dml_insertar, 
            (componente.nombre, componente.cliente, componente.tipo))
        
        self.conexion.commit()
    
    def remover(self, id_):
        dml_remover = """
            DELETE FROM componentes WHERE id = ?
        """
        self.cursor.execute(dml_remover, (id_,))
        self.conexion.commit()

def main():

    app = GestorAccesoriosComputador()
    app.mainloop()

if __name__ == '__main__':
    main()
