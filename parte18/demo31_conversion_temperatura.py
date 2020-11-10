import tkinter as tk
from tkinter import messagebox

class ConversionTemperatura(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.txt_fahrenheit = tk.Entry(self.master, width=10)
        self.txt_fahrenheit.grid(row=0, column=0, sticky='e', padx=10, pady=10)

        lbl_fahrenheit = tk.Label(self.master, text="\N{DEGREE FAHRENHEIT}")
        lbl_fahrenheit.grid(row=0, column=1, sticky='w', padx=10, pady=10)

        btn_convertir = tk.Button(self.master, text='\N{RIGHTWARDS BLACK ARROW}', command=self.convertir)
        btn_convertir.grid(row=0, column=2, padx=10, pady=10)

        self.lbl_celsius = tk.Label(self.master, text='\N{DEGREE CELSIUS}')
        self.lbl_celsius.grid(row=0, column=3, padx=10, pady=10)
    
    def convertir(self):
        try:
            fahrenheit = float(self.txt_fahrenheit.get())

            celsius = (5/9) * (fahrenheit - 32)

            self.lbl_celsius['text'] = f'{round(celsius, 2)} \N{DEGREE CELSIUS}'
        except:
            messagebox.showwarning('Advertencia', 'Debe escribir un número en el campo \N{DEGREE FAHRENHEIT}.')

def main():
    root = tk.Tk()
    root.title('Conversión Temperatura')
    root.geometry('300x100')

    ventana = ConversionTemperatura(root)
    ventana.mainloop()

if __name__ == "__main__":
    main()
