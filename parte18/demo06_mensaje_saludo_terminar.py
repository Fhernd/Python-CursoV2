import tkinter as tk
from tkinter import messagebox

class VentanaPrincipal(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.pack()

        self.inicilizar_gui()

    def inicilizar_gui(self):
        self.btn_saludar = tk.Button(self)
        self.btn_saludar['text'] = 'Saludar'
        self.btn_saludar['command'] = self.saludar
        self.btn_saludar.pack(side='top')

        self.btn_terminar = tk.Button(self, text='Terminar aplicación', fg='red', command=self.terminar)
        self.btn_terminar.pack(side='bottom')
    
    def saludar(self):
        messagebox.showinfo('Saludo', '¡Hola, Tkinter!')
    
    def terminar(self):
        self.master.destroy()

def main():
    app = tk.Tk()
    app.title('Ventana Principal')
    app.geometry('350x350')

    ventana = VentanaPrincipal(app)

    ventana.mainloop()

if __name__ == "__main__":
    main()
