import tkinter as tk
import webbrowser


class TextoEtiqueta(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Texto Etiquetas')
        self.geometry('350x350')
        self.resizable(0, 0)

        self.txa_contenido = tk.Text(self, width=60, height=15)

        self.btn_agregar_enlace = tk.Button(self, text='Agregar enlace')
        self.btn_agregar_enlace['command'] = self.agregar_enlace

        self.txa_contenido.tag_config('link', foreground='blue', underline=1)
        self.txa_contenido.tag_bind('link', '<Button-1>', self.abrir_enlace)
        self.txa_contenido.tag_bind('link', '<Enter>', lambda _: self.txa_contenido.config(cursor='hand2'))
    
    def agregar_enlace(self):
        pass

    def abrir_enlace(self):
        pass