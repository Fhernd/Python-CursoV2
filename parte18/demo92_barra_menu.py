import tkinter as tk


class AplicacionBarraMenu(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()

    def inicializar_gui(self):
        mnu_principal = tk.Menu(self)
        mnu_archivo = tk.Menu(mnu_principal, tearoff=0)

        mnu_archivo.add_command(label='Nuevo archivo')
        mnu_archivo.add_command(label='Abrir')
        mnu_archivo.add_separator()
        mnu_archivo.add_command(label='Guardar')
        mnu_archivo.add_command(label='Guardar como...')

        mnu_principal.add_cascade(label='Archivo', menu=mnu_archivo)
        mnu_principal.add_command(label='Acerca de')
        mnu_principal.add_command(label='Salir', command=self.destroy)

        self.config(menu=mnu_principal)


def main():
    app = AplicacionBarraMenu()
    app.mainloop()


if __name__ == '__main__':
    main()
