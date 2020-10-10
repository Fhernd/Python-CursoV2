import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        tk.Label(self, text='Primer número: ').grid(row=0, column=0)
        self.sbx_primer_numero = tk.Spinbox(self, from_=-1000, to=1000, width=5)
        self.sbx_primer_numero.grid(row=0, column=1)

        tk.Label(self, text='Segundo número: ').grid(row=1, column=0)
        self.sbx_segundo_numero = tk.Spinbox(self, from_=-1000, to=1000, width=5)
        self.sbx_segundo_numero.grid(row=1, column=1)

        tk.Button(self, text='Sumar', command=self.sumar).grid(row=2, column=0)
    
    def sumar(self):
        primer_numero = int(self.sbx_primer_numero.get())
        segundo_numero = int(self.sbx_segundo_numero.get())

        suma = primer_numero + segundo_numero

        messagebox.showinfo('Resultado', f'La suma de {primer_numero} y {segundo_numero} es igual a {suma}')

def main():
    app = tk.Tk()
    app.title('Calculadora')
    app.geometry('300x300')

    ventana = Calculadora(app)
    ventana.mainloop()

if __name__ == "__main__":
    main()
