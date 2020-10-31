import tkinter as tk

class VentanaBotones(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.inicializar_gui()
    
    def inicializar_gui(self):
        tk.Button(self, text='Azul', bg='blue').grid(row=0, column=0)
        tk.Button(self, text='Amarillo', bg='yellow').grid(row=1, column=0)
        tk.Button(self, text='Rojo', bg='red').grid(row=2, column=0)
        tk.Button(self, text='Verde', bg='green').grid(row=3, column=0)
        tk.Button(self, text='Blanco', bg='white').grid(row=4, column=0)

        tk.Button(self, text='#AF12BC', bg='#AF12BC').grid(row=5, column=0)

def main():
    app = tk.Tk()
    app.title('Colores para botones')
    app.geometry('350x300')

    ventana = VentanaBotones(app)
    ventana.mainloop()

if __name__ == "__main__":
    main()
