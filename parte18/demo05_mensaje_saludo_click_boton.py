import tkinter as tk
from tkinter import messagebox

class VentanaPrincipal(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.btn_saludar = tk.Button(self)
        self.btn_saludar['text'] = 'Saludar'
        self.btn_saludar['command'] = self.saludar
        self.btn_saludar.pack(side='top')
    
    def saludar(self):
        messagebox.showinfo('Saludo', '¡Hola, Usuario!')

def main():
    aplicacion = tk.Tk()
    aplicacion.title('Ventana Principal')
    aplicacion.geometry('300x300')

    ventana = VentanaPrincipal(aplicacion)
    ventana.mainloop()

if __name__ == "__main__":
    main()
