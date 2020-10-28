import tkinter as tk
from tkinter import ttk

class VentanaPrincipal(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.inicializar_gui()

    def inicializar_gui(self):
        contenedor = ttk.Notebook(self.master)
        tab_datos =  ttk.Frame(contenedor)
        contenedor.add(tab_datos, text='Datos')


        contenedor.pack(expand=1, fill='both')

def main():
    app = tk.Tk()
    app.geometry('350x300')
    app.title('Pestañas')

    ventana = VentanaPrincipal(app)
    ventana.mainloop()

if __name__ == "__main__":
    main()
