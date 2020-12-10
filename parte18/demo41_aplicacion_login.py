import tkinter as tk
from tkinter import ttk
import time

class Aplicacion:

    def __init__(self, master):
        self.master = master
        self.master.title('Inicio')
        self.master.geometry('350x350')

        self.inicializar_gui()
    
    def inicializar_gui(self):
        lbl_bienvenido = tk.Label(self.master, text='¡Bienvenido!', font=('Helvetica', 43))
        lbl_bienvenido.place(x=140, y=120)

        btn_login = tk.Button(self.master, text='Login')
        btn_login['command'] = self.login
    
    def login(self):
        pass

def main():
    root = tk.Tk()
    ventana = Aplicacion(root)
    root.mainloop()

if __name__ == "__main__":
    main()
