import tkinter as tk
from tkinter import messagebox

class VentanaPrincipal(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.inicializar_gui()

    def inicializar_gui(self):
        self.lenguaje_seleccionado = tk.IntVar()
        self.rbn_python = tk.Radiobutton(self, text='Python', value=1, variable=self.lenguaje_seleccionado)
        self.rbn_python.grid(row=0, column=0)

        self.rbn_java = tk.Radiobutton(self, text='Java', value=2, variable=self.lenguaje_seleccionado)
        self.rbn_java.grid(row=0, column=1)

        self.rbn_javascript = tk.Radiobutton(self, text='JavaScript', value=3, variable=self.lenguaje_seleccionado)
        self.rbn_javascript.grid(row=0, column=2)

        self.btn_seleccionar_lenguaje = tk.Button(self, text='Seleccionar lenguaje')
        self.btn_seleccionar_lenguaje['command'] = self.seleccionar_lenguaje
        self.btn_seleccionar_lenguaje.grid(row=1, column=0)
    
    def seleccionar_lenguaje(self):
        lenguaje_seleccionado = None
        if self.lenguaje_seleccionado.get() == 1:
            lenguaje_seleccionado = 'Python'
        elif self.lenguaje_seleccionado.get() == 2:
            lenguaje_seleccionado = 'Java'
        else:
            lenguaje_seleccionado = 'JavaScript'
        
        messagebox.showinfo('Mensaje', f'Su lenguaje de programación favorito es: {lenguaje_seleccionado}.')

def main():
    app = tk.Tk()
    app.title('Lenguaje Favorito')
    app.geometry('400x250')

    ventana = VentanaPrincipal(app)
    ventana.mainloop()
    
if __name__ == "__main__":
    main()
