import tkinter as tk


class VentanaIcono(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Ventana con ícono')
        self.geometry('300x300')

        self.iconbitmap('parte18/demo78_icono.ico')


def main():
    app = VentanaIcono()
    app.mainloop()


if __name__ == '__main__':
    main()
