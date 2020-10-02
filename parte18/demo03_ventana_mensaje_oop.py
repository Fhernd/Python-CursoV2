import tkinter as tk

class VentanaPrincipal(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.lbl_mensaje = tk.Label(self.master, text='¡Hola, Tkinter!', font=('Arial', 23), fg='#00ff00', bg='#000000')
        self.lbl_mensaje.place(x=30, y=150)

def main():
    root = tk.Tk()
    root.title('Saludo Tkinter')
    root.geometry('300x300')

    principal = VentanaPrincipal(root)

    principal.mainloop()

if __name__ == "__main__":
    main()
