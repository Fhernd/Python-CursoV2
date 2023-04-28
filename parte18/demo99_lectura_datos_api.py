import tkinter as tk
from tkinter import ttk

import requests


class LecturaDatosApi(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.tbl_datos = ttk.Treeview(self.master, selectmode ='browse') 
        self.tbl_datos['columns'] = ('ID', 'Nombre', 'Ubicación', 'Teléfono', 'Email')
        self.tbl_datos['show'] = 'headings'

        self.tbl_datos.pack(side='left',expand=True, fill='both')

        vsl_datos = ttk.Scrollbar(self, orient='vertical', command=self.tbl_datos.yview)
        vsl_datos.pack(side='right', fill='y')
        self.tbl_datos.configure(yscrollcommand=vsl_datos.set)

        self.consultar_datos_api()
    
    def consultar_datos_api(self):
        respuesta = requests.get('https://randomuser.me/api?results=100')
        datos = respuesta.json()['results']

        self.tbl_datos.column("ID", width = 90, anchor ='c')
        self.tbl_datos.column("Nombre", width = 90, anchor ='c')
        self.tbl_datos.column("Ubicación", width = 90, anchor ='c')
        self.tbl_datos.column("Teléfono", width = 90, anchor ='c')
        self.tbl_datos.column("Email", width = 90, anchor ='c')

        self.tbl_datos.heading('ID', text='ID')
        self.tbl_datos.heading('Nombre', text='Nombre')
        self.tbl_datos.heading('Ubicación', text='Ubicación')
        self.tbl_datos.heading('Teléfono', text='Teléfono')
        self.tbl_datos.heading('Email', text='Email')

        for i, d in enumerate(datos):
            nombre = f"{d['name']['first']} {d['name']['last']}"
            ubicacion = f"{d['location']['city']} ({d['location']['country']})"
            telefono = d['phone']
            email = d['email']

            self.tbl_datos.insert('', 'end', values=((i + 1), nombre, ubicacion, telefono, email))


if __name__ == '__main__':
    root = tk.Tk()
    app = LecturaDatosApi(master=root)
    app.mainloop()
