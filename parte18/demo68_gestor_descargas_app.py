import tkinter as tk
import threading

class GestorDescargasApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Gestor Descargas')
        self.geometry('640x200')
        self.resizable(0, 0)


def main():
    app = GestorDescargasApp()
    app.mainloop()

if __name__ == '__main__':
    main()
