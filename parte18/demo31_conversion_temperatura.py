import tkinter as tk

class ConversionTemperatura(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.txt_fahrenheit = tk.Entry(self.master, width=10)
        self.txt_fahrenheit.grid(row=0, column=0, sticky='e')

        lbl_fahrenheit = tk.Label(self.master, text="\N{DEGREE FAHRENHEIT}")
        lbl_fahrenheit.grid(row=0, column=1, sticky='w')

        btn_convertir = tk.Button(self.master, text='\N{RIGHTWARDS BLACK ARROW}', command=self.convertir)
    
    def convertir(self):
        pass

def main():
    root = tk.Tk()
    root.title('Conversión Temperatura')
    root.geometry('300x100')

    ventana = ConversionTemperatura(root)
    ventana.mainloop()
