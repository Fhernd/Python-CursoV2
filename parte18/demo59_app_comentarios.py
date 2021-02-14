from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class ComentariosApp(Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Comentarios App')
        self.configure(background='gray')
        self.minsize(400, 400)

        self.estilo = ttk.Style()
        self.estilo.configure('TFrame', background='black')
        self.estilo.configure('TButton', background='#95A3B3')
        self.estilo.configure('TLabel', background='#1E152A')

def main():
    app = ComentariosApp()
    app.mainloop()

if __name__ == '__main__':
    main()
