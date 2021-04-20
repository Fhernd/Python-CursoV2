import tkinter as tk
from tkinter import messagebox


class SemanaApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Semana App')
        self.geometry('300x300')

        dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        modos_seleccion = [tk.SINGLE, tk.BROWSE, tk.MULTIPLE, tk.EXTENDED]

        self.lbx_semana = tk.Listbox(self)
        self.lbx_semana.insert(0, *dias_semana)
        self.lbx_semana.pack()

        btn_mostrar_seleccion = tk.Button(self, text='Mostrar selección')
        btn_mostrar_seleccion['command'] = self.mostrar_seleccion
        btn_mostrar_seleccion.pack()

        botones_modo_seleccion = [self.crear_boton_modo_seleccion(m) for m in modos_seleccion]

        for b in botones_modo_seleccion:
            b.pack(side=tk.LEFT)

    
    def mostrar_seleccion(self):
        seleccion = self.lbx_semana.curselection()
        resultado = [self.lbx_semana.get(i) for i in seleccion]

        messagebox.showinfo('Selección', resultado)


    def crear_boton_modo_seleccion(self, modo):
        comando = lambda: self.lbx_semana.config(selectmode=modo)

        return tk.Button(self, command=comando, text=modo.capitalize())


def main():
    app = SemanaApp()
    app.mainloop()


if __name__ == '__main__':
    main()
