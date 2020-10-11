import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar

from time import sleep

class Proceso(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.inicializar_gui()

    def inicializar_gui(self):
        self.progreso = tk.DoubleVar()
        self.pbr_tarea = Progressbar(self, length=250, style='black.Horizontal.TProgressbar', variable=self.progreso, maximum=100)
        self.pbr_tarea['value'] = 0
        self.pbr_tarea.grid(row=0, column=0)

        tk.Button(self, text='Iniciar tarea', command=self.iniciar_tarea).grid(row=1, column=0)
    
    def iniciar_tarea(self):
        contador = 0

        while contador <= 100:
            self.progreso.set(contador)
            contador += 10
            self.master.update_idletasks()
            sleep(1)
        
        messagebox.showinfo('Mensaje', 'La tarea ha terminado')

def main():
    app = tk.Tk()
    app.title('Proceso')
    app.geometry('300x300')

    proceso = Proceso(app)
    proceso.mainloop()

if __name__ == "__main__":
    main()
