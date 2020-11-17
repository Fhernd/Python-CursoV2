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
        
        btn_dividir = tk.Button(self.root, text='Dividir', command=self.dividir, width=10)
        btn_dividir.place(x=245, y=90)

        lbl_resultado = tk.Label(self.root, text='Resultado: ')
        lbl_resultado.place(x=20, y=170)

        self.txt_resultado = tk.Entry(self.root)
        self.txt_resultado.place(x=200, y=170)
    
    def sumar(self):
        try:
            primer_numero = float(self.txt_primer_numero.get())
        except Exception:
            messagebox.showwarning('Mensaje', 'El campo Primer número debe ser un valor numérico.')
        
        try:
            segundo_numero = float(self.txt_segundo_numero.get())
        except Exception:
            messagebox.showwarning('Mensaje', 'El campo Segundo número debe ser un valor numérico.')

        suma = primer_numero + segundo_numero

        self.txt_resultado.delete(0, tk.END)
        self.txt_resultado.insert(tk.END, str(suma))
    
    def restar(self):
        try:
            primer_numero = float(self.txt_primer_numero.get())
        except Exception:
            messagebox.showwarning('Mensaje', 'El campo Primer número debe ser un valor numérico.')
        
        try:
            segundo_numero = float(self.txt_segundo_numero.get())
        except Exception:
            messagebox.showwarning('Mensaje', 'El campo Segundo número debe ser un valor numérico.')

        resta = primer_numero - segundo_numero

        self.txt_resultado.delete(0, tk.END)
        self.txt_resultado.insert(tk.END, str(resta))
    
    def multiplicar(self):
        try:
            primer_numero = float(self.txt_primer_numero.get())
        except Exception:
            messagebox.showwarning('Mensaje', 'El campo Primer número debe ser un valor numérico.')
        
        try:
            segundo_numero = float(self.txt_segundo_numero.get())
        except Exception:
            messagebox.showwarning('Mensaje', 'El campo Segundo número debe ser un valor numérico.')

        multiplicacion = primer_numero * segundo_numero

        self.txt_resultado.delete(0, tk.END)
        self.txt_resultado.insert(tk.END, str(multiplicacion))

    def dividir(self):
        try:
            primer_numero = float(self.txt_primer_numero.get())
        except Exception:
            messagebox.showwarning('Mensaje', 'El campo Primer número debe ser un valor numérico.')
        
        try:
            segundo_numero = float(self.txt_segundo_numero.get())
        except Exception:
            messagebox.showwarning('Mensaje', 'El campo Segundo número debe ser un valor numérico.')

        if segundo_numero != 0:
            division = primer_numero / segundo_numero

            self.txt_resultado.delete(0, tk.END)
            self.txt_resultado.insert(tk.END, str(division))
        else:
            messagebox.showwarning('Mensaje', 'El campo Segundo número no puede ser cero (0).')

def main():
    root = tk.Tk()
    root.title('Calculadora')
    root.geometry('350x250')

    calculadora = CalculadoraAplicacion(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
