import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import threading
from urllib import request
import os
import validators

class Descargador(threading.Thread):

    def __init__(self, url, destino):
        super().__init__()
        self.url = url
        self.destino = destino

    def run(self):
        nombre_archivo = self.url.split('/')[-1]

        with request.urlopen(self.url) as r:
            with open(os.path.join(self.destino, nombre_archivo), 'wb') as f:
                f.write(r.read())
                messagebox.showinfo('Información', f'El archivo {nombre_archivo} se ha descargado en la siguiente ruta {self.destino}.')

class GestorDescargasApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Gestor Descargas')
        self.geometry('600x180')
        self.resizable(0, 0)

        frm_superior = tk.Frame(self)
        frm_superior.columnconfigure(0, weight=2)
        frm_superior.columnconfigure(1, weight=10)

        lbl_url = tk.Label(frm_superior, text='URL:', width=10, justify=tk.LEFT, anchor="w")
        lbl_url.grid(row=0, column=0, sticky=tk.W)

        self.url = tk.StringVar(self)
        self.txt_url = tk.Entry(frm_superior, textvariable=self.url, width=80)
        self.txt_url.grid(row=0, column=1, sticky=tk.EW)

        lbl_destino = tk.Label(frm_superior, text='Destino:', width=10, justify=tk.LEFT, anchor="w")
        lbl_destino.grid(row=1, column=0, sticky=tk.W, pady=10)

        self.destino = tk.StringVar(self)
        self.txt_destino = tk.Entry(frm_superior, textvariable=self.destino, width=80, state=tk.DISABLED)
        self.txt_destino.grid(row=1, column=1, sticky=tk.EW, pady=10)

        frm_superior.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=15)

        frm_inferior = tk.Frame(self)
        frm_inferior.columnconfigure(0, weight=1)

        self.lbl_estado = tk.Label(frm_inferior, text='Listo', width=10, justify=tk.LEFT, anchor="w")
        self.lbl_estado.grid(row=0, column=0, sticky=tk.W, pady=10)

        btn_seleccionar_destino = tk.Button(frm_inferior, text='Seleccionar destino...')
        btn_seleccionar_destino['command'] = self.seleccionar_destino
        btn_seleccionar_destino.grid(row=0, column=1, sticky='E', padx=10)
        
        self.btn_iniciar_descarga = tk.Button(frm_inferior, text='Iniciar descarga')
        self.btn_iniciar_descarga['command'] = self.iniciar_descarga
        self.btn_iniciar_descarga.grid(row=0, column=2, sticky='E')

        frm_inferior.grid(row=1, column=0, sticky=tk.NSEW, padx=10, pady=10)
    
    def seleccionar_destino(self):
        carpeta_destino = filedialog.askdirectory()

        self.destino.set(carpeta_destino)
    
    def iniciar_descarga(self):
        url = self.url.get().strip()

        if not validators.url(url):
            messagebox.showwarning('Mensaje', 'La URL escrita no es válida.')
            return
        
        destino = self.destino.get()

        if len(destino) == 0:
            messagebox.showwarning('Mensaje', 'Debe especificar una ruta para guardar el archivo.')
            return
        
        t = Descargador(url, destino)

        t.start()

        self.btn_iniciar_descarga['state'] = tk.DISABLED
        self.lbl_estado.config(text='Descargando archivo...')

        self.validar_finalizacion(t)
    
    def validar_finalizacion(self, t):
        self.after(1000, self.comprobar_fin_descarga, t)
    
    def comprobar_fin_descarga(self, t):
        if not t.is_alive():
            self.lbl_estado.config(text='La descarga ha finalizado.')
            self.btn_iniciar_descarga['state'] = tk.NORMAL
        else:
            self.validar_finalizacion(t)

def main():
    app = GestorDescargasApp()
    app.mainloop()

if __name__ == '__main__':
    main()
