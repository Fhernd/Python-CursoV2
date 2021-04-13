import tkinter as tk
from tkinter import messagebox

class SeleccionValoresNumericos(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Selección Valores Numéricos')
        self.geometry('300x200')

        self.spx_edad = tk.Spinbox(self, from_=18, to=60)
        self.scl_puntos = tk.Scale(self, from_=0, to=100)

        btn_mostrar_valores = tk.Button(self, text='Mostrar valores')
        btn_mostrar_valores['command'] = self.mostrar_valores

        self.spx_edad.pack()
        self.scl_puntos.pack()
        btn_mostrar_valores.pack()
    
    def mostrar_valores(self):
        edad = int(self.spx_edad.get())
        puntos = self.scl_puntos.get()

        messagebox.showinfo('Información', f'Su edad es: {edad}. Puntos: {puntos}')


def main():
    app = SeleccionValoresNumericos()
    app.mainloop()


if __name__ == '__main__':
    main()
