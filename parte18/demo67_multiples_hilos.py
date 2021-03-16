import tkinter as tk
from tkinter import messagebox
import time
import threading

class MultiplesHilosGUI(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()

    def inicializar_gui(self):
        self.title('Múltiples Hilos')
        self.geometry('200x200')

        btn_contar = tk.Button(self, text='Contar')
        btn_contar.grid(row=0, column=0)
        btn_contar['command'] = self.contar

        btn_saludar = tk.Button(self, text='Saludar')
        btn_saludar.grid(row=2, column=0)
        btn_saludar['command'] = self.saludar

    def contar(self):
        conteo = Conteo('Temporizador')
        conteo.start()
    
    def saludar(self):
        messagebox.showinfo('Saludo', 'Hola, usuario')


class Conteo(threading.Thread):

    def __init__(self, nombre):
        threading.Thread.__init__(self)
        self.name = nombre
    
    def run(self):
        for _ in range(10):
            time.sleep(1)
        
        messagebox.showinfo('Mensaje', 'El conteo ha finalizado')

def main():
    app = MultiplesHilosGUI()
    app.mainloop()

if __name__ == '__main__':
    main()
