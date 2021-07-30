import tkinter as tk


class MenuContextualApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Editor de Texto')
        self.geometry('400x400')

        self.mcx_edicion = tk.Menu(self, tearoff=0)
        self.mcx_edicion.add_command(label='Copiar', command=self.copiar)
        self.mcx_edicion.add_command(label='Cortar', command=self.cortar)
    
    def copiar(self):
        pass
    
    def cortar(self):
        pass
