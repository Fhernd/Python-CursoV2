import tkinter as tk


class CambioFuenteTexto(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()

    def inicializar_gui(self):
        self.title('Cambio fuente texto')
        self.geometry('300x300')

        texto = 'Python es un lenguaje de programación multiparadigma'
        self.lbl_texto = tk.Label(self, text=texto)

        self.fuente = tk.StringVar(self)
        self.fuente.trace('w', self.cambiar_fuente)

        fuentes = ('Courier', 'Helvetica', 'Times')
        opt_fuentes = tk.OptionMenu(self, self.fuente, *fuentes)

        self.tamagnio = tk.StringVar(self)
        self.tamagnio.trace('w', self.cambiar_fuente)
        spx_tamagnio = tk.Spinbox(self, from_=8, to=18, textvariable=self.tamagnio)

        self.lbl_texto.pack(padx=20, pady=20)
        opt_fuentes.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        spx_tamagnio.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    def cambiar_fuente(self, *argumentos):
        fuente = self.fuente.get()
        tamagnio = self.tamagnio.get()
        self.lbl_texto.config(font=(fuente, tamagnio))


def main():
    app = CambioFuenteTexto()
    app.mainloop()


if __name__ == '__main__':
    main()
