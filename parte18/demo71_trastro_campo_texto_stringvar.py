import tkinter as tk
from tkinter import messagebox


class AplicacionStringVar(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Uso de StringVar')
        self.geometry('200x200')

        self.nombre = tk.StringVar(self)

        self.txt_nombre = tk.Entry(self, textvariable=self.nombre)
        self.txt_nombre.pack()

        btn_mostrar_nombre = tk.Button(self, text='Mostrar nombre')
        btn_mostrar_nombre['command'] = self.mostrar_nombre
        btn_mostrar_nombre.pack()

    def mostrar_nombre(self):
        texto = self.nombre.get()

        messagebox.showinfo('Mensaje', f'Ud. ha escrito el nombre: {texto}')


def main():
    app = AplicacionStringVar()
    app.mainloop()


if __name__ == '__main__':
    main()
