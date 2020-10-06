import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox

class VentanaPrincipal(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.pack()
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        lbl_seleccion = tk.Label(self, text='Seleccione lenguaje favorito:')
        lbl_seleccion.grid(row=0, column=0)

        self.cbx_lenguajes = Combobox(self)
        lenguajes = ['Python', 'Java', 'JavaScript', 'C++', 'Go', 'Kotlin']
        self.cbx_lenguajes['values'] = tuple(lenguajes)
        self.cbx_lenguajes.current(1)
        self.cbx_lenguajes.grid(row=0, column=1)

        btn_mostrar_seleccion = tk.Button(self, text='Mostrar selección')
        btn_mostrar_seleccion['command'] = self.mostrar_seleccion
        btn_mostrar_seleccion.grid(row=0, column=2)
    
    def mostrar_seleccion(self):
        lenguaje = self.cbx_lenguajes.get()

        messagebox.showinfo('Información', f'Su lenguaje de programación favorito es: {lenguaje}')

def main():
    app = tk.Tk()
    app.title('Lenguaje Favorito')
    app.geometry('350x300')

    ventana = VentanaPrincipal(app)

    ventana.mainloop()

if __name__ == "__main__":
    main()
