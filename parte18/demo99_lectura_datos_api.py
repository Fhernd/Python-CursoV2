import tkinter as tk
from tkinter import ttk

import requests


class LecturaDatosApi(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.tbl_datos = ttk.Treeview(self, columns=('Nombre', 'Ubicación', 'Teléfono', 'Email'))
        self.tbl_datos.heading('Nombre', text='Nombre')
        self.tbl_datos.heading('Ubicación', text='Ubicación')
        self.tbl_datos.heading('Teléfono', text='Teléfono')
        self.tbl_datos.heading('Email', text='Email')

        self.consultar_datos_api()