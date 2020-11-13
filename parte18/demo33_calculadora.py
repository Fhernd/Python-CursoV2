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

def main():
    root = tk.Tk()
    root.title('Calculadora')
    root.geometry('350x300')

    calculadora = CalculadoraAplicacion(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
