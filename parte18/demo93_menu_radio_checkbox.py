import tkinter as tk


class Aplicacion(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Menú Opciones')
        self.geometry('350x350')

        self.seleccionado = tk.BooleanVar()
        self.seleccionado.trace('w', self.seguir_seleccionado)

        self.elemento_seleccionado = tk.StringVar()
        self.elemento_seleccionado.set('1')
        self.elemento_seleccionado.trace('w', self.seguir_elemento_seleccionado)
    
    def seguir_seleccionado(self):
        pass

    def seguir_elemento_seleccionado(self):
        pass


def main():
    app = Aplicacion()
    app.mainloop()


if __name__ == '__main__':
    main()
