import tkinter as tk
from tkinter.colorchooser import askcolor

from functools import partial


class AparienciaComponentes(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Cambiar apariencia')
        self.geometry('350x350')

        texto = 'Python es un lenguaje de programación multiparadigma.'
        self.lbl_texto = tk.Label(self, text=texto)

        btn_cambiar_fondo = tk.Button(self, text='Cambiar color de fondo')
        btn_cambiar_fondo['command'] = partial(self.cambiar_color, 'bg')
