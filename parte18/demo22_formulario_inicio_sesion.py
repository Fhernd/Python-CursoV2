import tkinter as tk
from tkinter import messagebox
from functools import partial

class FormularioLogin(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        #self.pack()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        tk.Label(self.master, text='Usuario:').grid(row=0, column=0)

        self.usuario = tk.StringVar()
        tk.Entry(self.master, textvariable=self.usuario).grid(row=0, column=1)

        tk.Label(self.master, text='Contraseña:').grid(row=1, column=0)

        self.contrasegnia = tk.StringVar()
        tk.Entry(self.master, textvariable=self.contrasegnia, show='*').grid(row=1, column=1)

        validar_login_credenciales = partial(self.validar_login, self.usuario, self.contrasegnia)

        tk.Button(self.master, text='Login', command=validar_login_credenciales).grid(row=2, column=0)
    
    def validar_login(self, usuario, contrasegnia):
        if len(usuario.get()) == 0:
            messagebox.showwarning('Mensaje', 'El campo Usuario es obligatorio.')
            return
        
        if len(contrasegnia.get()) == 0:
            messagebox.showwarning('Mensaje', 'El campo Contraseña es obligatorio.')
            return
        
        if usuario.get() == 'admin' and contrasegnia.get() == 'User2k20':
            messagebox.showinfo('Mensaje', 'Ha accedido al sistema.')
        else:
            messagebox.showwarning('Mensaje', 'Las credenciales de acceso no son válidas.')

def main():
    app = tk.Tk()
    app.title('Formulario Login')
    app.geometry('350x250')

    ventana = FormularioLogin(app)
    ventana.mainloop()

if __name__ == "__main__":
    main()
