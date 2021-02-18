import tkinter as tk
from tkinter import messagebox

class FormularioRegistro(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Validación Datos')
        self.minsize(400, 350)

def main():
    app = FormularioRegistro()
    app.mainloop()

if __name__ == '__main__':
    main()
