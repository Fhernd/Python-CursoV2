import tkinter as tk


class Aplicacion(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Base de datos de opciones')

        self.option_add('*font', 'helvetica 12')
        self.option_add('*header.font', 'helvetica 20 bold')
        self.option_add('*subtitle.font', 'helvetica 16 italic')
        
        self.option_add('*Button.foreground', 'green')
        self.option_add('*Button.background', 'black')
        self.option_add('*Button.activeForeground', 'red')
        self.option_add('*Button.activeBackground', 'black')

        self.crear_etiqueta(name='header', text='Este es un encabezado')
        self.crear_etiqueta(name='subtitle', text='Este es un subtítulo')
        self.crear_etiqueta(text='Este es un párrafo')
        self.crear_etiqueta(text='Este es otro párrafo')

        self.crear_boton(text='Tkinter')

    def crear_etiqueta(self, **opciones):
        tk.Label(self, **opciones).pack(padx=20, pady=5, anchor=tk.W)
    
    def crear_boton(self, **opciones):
        tk.Button(self, **opciones).pack(padx=5, pady=5, anchor=tk.E)


def main():
    app = Aplicacion()
    app.mainloop()


if __name__ == '__main__':
    main()
