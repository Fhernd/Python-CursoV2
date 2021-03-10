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
        frm_entrada.place(relx=0.05, rely=0.05, relwidth=1, relheight=0.2, anchor='n')

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
        self.cbx_tipo.place(relx=0.25, rely=0.5, relwidth=0.25, relheight=0.5)

        lbl_costo = tk.Label(frm_entrada, text='Costo:')
        lbl_costo.place(relx=0.5, rely=0.5, relwidth=0.25, relheight=0.5)
        self.txt_costo = tk.Entry(frm_entrada)
        self.txt_costo.place(relx=0.70, rely=0.5, relwidth=0.25, relheight=0.5)

        frm_botones = tk.Frame(self)
        frm_entrada.place(relx=0.05, rely=0.25, relwidth=1, relheight=0.1, anchor='n')

        btn_agregar = tk.Button(frm_botones, text='Agregar')
        btn_agregar['command'] = self.agregar
        btn_agregar.place(relx=0, rely=0, relwidth=0.25, relheight=1)
    
    def agregar(self):
        pass

def main():

    app = GestorAccesoriosComputador()
    app.mainloop()

if __name__ == '__main__':
    main()
