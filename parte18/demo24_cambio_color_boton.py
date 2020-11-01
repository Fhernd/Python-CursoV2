import tkinter as tk

class VentanaPrincipal(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        btn_saludar = tk.Button(self, text='Saludar', bg='#FFF', activebackground='yellow')
        btn_saludar.pack()

def main():
    app = tk.Tk()
    app.title('Cambio color botón')
    app.geometry('300x300')

    ventana = VentanaPrincipal(app)
    ventana.mainloop()

if __name__ == "__main__":
    main()
