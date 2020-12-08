import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

class GestionLenguajesProgramacion:

    def __init__(self, master):
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.lst_lenguajes = tk.Listbox(self.master, width=16, height=18)
        self.lst_lenguajes.place(x=20, y=20)

        btn_agregar_lenguaje_arriba = tk.Button(self.master, text='Agregar lenguaje parte superior')
        btn_agregar_lenguaje_arriba['command'] = self.agregar_lenguaje_arriba
        btn_agregar_lenguaje_arriba.place(x=160, y=20)

        btn_agregar_lenguaje_abajo = tk.Button(self.master, text='Agregar lenguaje parte abajo')
        btn_agregar_lenguaje_abajo['command'] = self.agregar_lenguaje_abajo
        btn_agregar_lenguaje_abajo.place(x=160, y=50)

        btn_eliminar_lenguaje_seleccionado = tk.Button(self.master, text='Eliminar lenguaje seleccionado')
        btn_eliminar_lenguaje_seleccionado['command'] = self.eliminar_lenguaje_seleccionada
        btn_eliminar_lenguaje_seleccionado.place(x=160, y=50)
    
    def agregar_lenguaje_arriba(self):
        lenguaje = simpledialog.askstring('Agregar lenguaje', 'Escriba el lenguaje de programación a agregar')

        self.lst_lenguajes.insert(0, lenguaje)

    def agregar_lenguaje_abajo(self):
        pass
    
    def eliminar_lenguaje_seleccionada(self):
        pass

def main():
    master = tk.Tk()
    master.title('Gestión Lenguajes de Programación')
    master.geometry('400x400')

    ventana = GestionLenguajesProgramacion(master)
    master.mainloop()

if __name__ == "__main__":
    main()
