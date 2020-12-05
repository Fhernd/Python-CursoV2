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

def main():
    master = tk.Tk()
    master.title('Gestión Lenguajes de Programación')
    master.geometry('400x400')

    ventana = GestionLenguajesProgramacion(master)
    master.mainloop()

if __name__ == "__main__":
    main()
