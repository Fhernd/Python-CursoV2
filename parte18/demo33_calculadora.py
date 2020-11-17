import tkinter as tk
from tkinter import messagebox

class CalculadoraAplicacion:

    def __init__(self, root):
        self.root = root

        self.inicializar_gui()
    
    def inicializar_gui(self):
        lbl_primer_numero = tk.Label(self.root, text='Primer número: ')
        lbl_primer_numero.place(x=20, y=30)

        self.txt_primer_numero = tk.Entry(self.root)
        self.txt_primer_numero.place(x=200, y=30)

        lbl_segundo_numero = tk.Label(self.root, text='Segundo número:')
        lbl_segundo_numero.place(x=20, y=60)

        self.txt_segundo_numero = tk.Entry(self.root)
        self.txt_segundo_numero.place(x=200, y=60)

        btn_sumar = tk.Button(self.root, text='Sumar', command=self.sumar, width=7)
        btn_sumar.place(x=20, y=90)
        
        btn_restar = tk.Button(self.root, text='Restar', command=self.restar, width=7)
        btn_restar.place(x=90, y=90)
        
        btn_multiplicar = tk.Button(self.root, text='Multiplicar', command=self.multiplicar, width=10)
        btn_multiplicar.place(x=160, y=90)
    
    def sumar(self):
        pass
    
    def restar(self):
        pass
    
    def multiplicar(self):
        pass

def main():
    root = tk.Tk()
    root.title('Calculadora')
    root.geometry('350x300')

    calculadora = CalculadoraAplicacion(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
