import threading
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import validators
import requests


class DescargaHtmlAsincronico(threading.Thread):

    def __init__(self, url):
        super().__init__()

        self.url = url
        self.html = None
    
    def run(self):
        try:
            respuesta = requests.get(self.url)
            self.html = respuesta.text
        except:
            self.html = 'EL DOMINIO NO ESTÁ DISPONIBLE'


class DescargadorHtmlApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()

    def inicializar_gui(self):
        self.title('Descargador HTML')
        self.geometry('680x435')
        self.resizable(0, 0)

        self.frm_superior = tk.Frame(self)
        self.frm_superior.columnconfigure(0, weight=1)
        self.frm_superior.columnconfigure(1, weight=10)
        self.frm_superior.columnconfigure(2, weight=1)

        lbl_url = ttk.Label(self.frm_superior, text='URL:')
        lbl_url.grid(row=0, column=0, sticky=tk.W)

        self.url = tk.StringVar(self)
        txt_url = ttk.Entry(self.frm_superior, textvariable=self.url, width=90)
        txt_url.grid(row=0, column=1, sticky=tk.EW)

        self.btn_descargar = ttk.Button(self.frm_superior, text='Descargar')
        self.btn_descargar['command'] = self.descargar
        self.btn_descargar.grid(row=0, column=2, sticky=tk.E)

        self.frm_superior.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=10)

        frm_intermedio = ttk.Frame(self)

        self.txa_html = tk.Text(frm_intermedio, height=20)
        self.txa_html.grid(row=1, column=0)

        sbr_txa_html = ttk.Scrollbar(frm_intermedio, orient='vertical', command=self.txa_html.yview)
        sbr_txa_html.grid(row=1, column=1, sticky=tk.NS)
        self.txa_html['yscrollcommand'] = sbr_txa_html.set

        frm_intermedio.grid(row=1, column=0, sticky=tk.NSEW, padx=10, pady=10)

        frm_inferior = ttk.Frame(self)
        frm_inferior.columnconfigure(0, weight=1)

        btn_copiar = ttk.Button(frm_inferior, text='Copiar', command=self.copiar)
        btn_copiar.grid(row=0, column=0, sticky=tk.E)

        btn_salir = ttk.Button(frm_inferior, text='Salir', command=self.destroy)
        btn_salir.grid(row=0, column=1, sticky=tk.E)

        frm_inferior.grid(row=2, column=0, sticky=tk.NSEW, padx=10, pady=10)

    def descargar(self):
        url = self.url.get()

        if not validators.url(url):
            messagebox.showwarning('Advertencia', 'La URL especificada no es válida.')
            return
        
        self.btn_descargar['state'] = tk.DISABLED
        self.txa_html.delete(1.0, 'end')

        thread_descarga = DescargaHtmlAsincronico(url)
        thread_descarga.start()

        self.monitorear_descarga(thread_descarga)
    
    def monitorear_descarga(self, thread_descarga):
        if thread_descarga.is_alive():
            self.after(100, lambda: self.monitorear_descarga(thread_descarga))
        else:
            self.txa_html.insert(1.0, thread_descarga.html)
            self.btn_descargar['state'] = tk.NORMAL
    
    def copiar(self):
        if len(self.txa_html.get(1.0, 'end')):
            self.clipboard_clear()
            self.clipboard_append(self.txa_html.get(1.0, 'end'))

def main():
    app = DescargadorHtmlApp()
    app.mainloop()

if __name__ == '__main__':
    main()
