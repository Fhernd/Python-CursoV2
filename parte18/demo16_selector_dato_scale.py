import tkinter as tk

class SeleccionDato(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.valor_seleccionado = tk.DoubleVar()

        self.scl_dato = tk.Scale(self, variable=self.valor_seleccionado, from_=1, to=100, orient=tk.HORIZONTAL)
        self.scl_dato.pack()

        tk.Label(self, text='Scale horizontal').pack()

        tk.Button(self, text='Seleccionar valor', command=self.seleccionar_valor).pack()

        self.lbl_valor_seleccionado = tk.Label(self)
        self.lbl_valor_seleccionado.pack()
    
    def seleccionar_valor(self):
        seleccion = f'El valor seleccionado es: {self.valor_seleccionado.get()}'

        self.lbl_valor_seleccionado.config(text=seleccion, font=('Courier', 15))

def main():
    app = tk.Tk()
    app.title('Selector de Datos')
    app.geometry('350x300')

    ventana = SeleccionDato(app)
    ventana.mainloop()

if __name__ == "__main__":
    main()
