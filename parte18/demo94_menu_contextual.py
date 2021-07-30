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
        self.mcx_edicion.add_command(label='Pegar', command=self.pegar)
        self.mcx_edicion.add_command(label='Eliminar', command=self.eliminar)

        self.txa_contenido = tk.Text(self, height=12, width=80)
        self.txa_contenido.bind('<Button-3>', self.mostrar_menu_contextual)
        self.txa_contenido.pack()
    
    def mostrar_menu_contextual(self, evento):
        self.mcx_edicion.post(evento.x_root, evento.y_root)

    def copiar(self):
        pass
    
    def cortar(self):
        pass
    
    def pegar(self):
        pass
    
    def eliminar(self):
        pass


def main():
    app = MenuContextualApp()
    app.mainloop()


if __name__ == '__main__':
    main()
