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
        
        btn_cambiar_color = tk.Button(self, text='Cambiar color del texto')
        btn_cambiar_color['command'] = partial(self.cambiar_color, 'fg')

        self.lbl_texto.pack(padx=20, pady=20)
        btn_cambiar_fondo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        btn_cambiar_color.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def cambiar_color(self, atributo):
        color_seleccionado  = askcolor()[1]
        self.lbl_texto.config(**{atributo: color_seleccionado})


def main():
    app = AparienciaComponentes()
    app.mainloop()


if __name__ == '__main__':
    main()
