import tkinter as tk

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

def main():
    app = tk.Tk()
    app.title('Formulario Login')
    app.geometry('350x250')

    ventana = FormularioLogin(app)
    ventana.mainloop()

if __name__ == "__main__":
    main()
