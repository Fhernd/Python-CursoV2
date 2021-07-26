import tkinter as tk
from tkinter.messagebox import showinfo

class Aplicacion(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Menú Opciones')
        self.geometry('350x350')

        self.seleccionado = tk.BooleanVar()
        self.seleccionado.trace('w', self.seguir_seleccionado)

        self.color_seleccionado = tk.StringVar()
        self.color_seleccionado.set('1')
        self.color_seleccionado.trace('w', self.seguir_color_seleccionado)

        mnu_principal = tk.Menu(self)
        mnu_opciones = tk.Menu(mnu_principal, tearoff=0)

        mnu_opciones.add_checkbutton(label='Activo', onvalue=True, offvalue=False, variable=self.seleccionado)

        mnu_opciones.add_separator()

        mnu_opciones.add_radiobutton(label='Rojo', value='rojo', variable=self.color_seleccionado)
        mnu_opciones.add_radiobutton(label='Verde', value='verde', variable=self.color_seleccionado)
        mnu_opciones.add_radiobutton(label='Azul', value='azul', variable=self.color_seleccionado)

        mnu_principal.add_cascade(label='Opciones', menu=mnu_opciones)
        mnu_principal.add_command(label='Salir', command=self.destroy)

        self.config(menu=mnu_principal)

    
    def seguir_seleccionado(self, *args):
        showinfo('Mensaje', self.seleccionado.get())

    def seguir_color_seleccionado(self, *args):
        showinfo('Mensaje', self.color_seleccionado.get())


def main():
    app = Aplicacion()
    app.mainloop()


if __name__ == '__main__':
    main()
