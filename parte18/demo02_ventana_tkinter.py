import tkinter as tk

class VentanaPrincipal(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

def main():
    principal = tk.Tk()
    principal.geometry('300x300')
    principal.title('Ventana Principal')

    aplicacion = VentanaPrincipal(principal)
    aplicacion.mainloop()

if __name__ == "__main__":
    main()
