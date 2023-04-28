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
    
    def consultar_datos_api(self):
        respuesta = requests.get('https://randomuser.me/api?results=5')
        datos = respuesta.json()['results']

        for d in datos:
            nombre = f"{d['name']['first']} {d['name']['last']}"
            ubicacion = f"{d['location']['city']} ({d['location']['country']})"
            telefono = d['phone']
            email = d['email']

            self.tbl_datos.insert('', 'end', values=(nombre, ubicacion, telefono, email))


if __name__ == '__main__':
    root = tk.Tk()
    app = LecturaDatosApi(root)
    app.mainloop()
