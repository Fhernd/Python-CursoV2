import tkinter as tk


class OrganizacionInterfaz(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Organización Interfaz')
        self.geometry('350x350')

        lbl_amarillo = tk.Label(self, text='1', bg='yellow')
        lbl_blanco = tk.Label(self, text='2', bg='white')
        lbl_rojo = tk.Label(self, text='3', bg='red', fg='white')
        lbl_verde = tk.Label(self, text='4', bg='green', fg='white')
        lbl_azul = tk.Label(self, text='5', bg='blue', fg='white')

        opciones = {'fill': tk.BOTH, 'ipadx': 10, 'ipady': 10}

        lbl_amarillo.pack(side=tk.TOP, **opciones)
        lbl_blanco.pack(side=tk.TOP, **opciones)
        lbl_rojo.pack(side=tk.LEFT, expand=1, **opciones)
        lbl_verde.pack(side=tk.LEFT, expand=1, **opciones)
        lbl_azul.pack(side=tk.LEFT, expand=1, **opciones)


def main():
    app = OrganizacionInterfaz()
    app.mainloop()


if __name__ == '__main__':
    main()
