import sqlite3
import tkinter as tk
from tkinter import messagebox

class GestorAccesoriosComputador(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Gestor Accesorios & Repuestos para Computador')
        self.geometry('550x340')

def main():

    app = GestorAccesoriosComputador()
    app.mainloop()

if __name__ == '__main__':
    main()
