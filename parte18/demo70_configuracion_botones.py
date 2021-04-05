import tkinter as tk

class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Configuración Botones')

        relieves = [tk.SUNKEN, tk.RAISED, tk.GROOVE, tk.RIDGE, tk.FLAT]

        self.botones = [self.crear_boton(r) for r in relieves]

        for b in self.botones:
            b.pack(padx=10, pady=10, side=tk.LEFT)
    
    def crear_boton(self, r):
        return tk.Button(self, text=r, relief=r)


def main():
    ventana = VentanaPrincipal()
    ventana.mainloop()


if __name__ == '__main__':
    main()
