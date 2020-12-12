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
        lbl_bienvenido = tk.Label(self.master, text='¡Bienvenido!', font=('Helvetica', 27))
        lbl_bienvenido.place(x=80, y=90)

        btn_login = tk.Button(self.master, text='Login')
        btn_login['command'] = self.login
        btn_login.place(x=150, y=180)
    
    def login(self):
        pass


class LoginVentana:
    def __init__(self, master):
        self.master = master
        self.ventana = tk.Toplevel()
        self.ventana.title('Login')
        self.ventana.geometry('300x200')

        self.inicializar_gui()
    
    def inicializar_gui(self):
        lbl_usuario = tk.Label(self.ventana, text='Usuario:')
        lbl_usuario.place(x=20, y=20)
        txt_usuario = tk.Entry(self.ventana)
        txt_usuario.place(x=80, y=20)
        txt_usuario.focus()

def main():
    root = tk.Tk()
    ventana = Aplicacion(root)
    root.mainloop()

if __name__ == "__main__":
    main()
