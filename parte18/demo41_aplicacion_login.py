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

        btn_login = tk.Button(self.master, text='Mostrar ventana login')
        btn_login['command'] = self.login
        btn_login.place(x=110, y=180)
    
    def login(self):
        login_ventana = LoginVentana(self.master)
        self.master.wait_window(login_ventana.ventana)


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
        self.txt_usuario = tk.Entry(self.ventana)
        self.txt_usuario.place(x=80, y=20)
        self.txt_usuario.focus()

        lbl_clave = tk.Label(self.ventana, text='Clave:')
        lbl_clave.place(x=20, y=50)
        self.txt_clave = tk.Entry(self.ventana)
        self.txt_clave.place(x=80, y=50)

        btn_login = tk.Button(self.ventana, text='Login')
        btn_login.place(x=80, y=80)
        btn_login['command'] = self.login
    
    def login(self):
        usuario = self.txt_usuario.get()
        clave = self.txt_clave.get()

        # TODO: Validar datos sobre el login...

def main():
    root = tk.Tk()
    ventana = Aplicacion(root)
    root.mainloop()

if __name__ == "__main__":
    main()
