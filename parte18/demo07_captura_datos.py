import tkinter as tk
from tkinter import messagebox

class VentanaPrincipal(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        lbl_nombre = tk.Label(self, text='Nombre:')
        lbl_nombre.grid(row=0, column=0)

        self.txt_nombre = tk.Entry(self, width=20)
        self.txt_nombre.grid(row=0, column=1)

        self.btn_saludar = tk.Button(self, text='Saludar')
        self.btn_saludar['command'] = self.saludar
        self.btn_saludar.grid(row=0, column=2)
    
    def saludar(self):
        nombre = self.txt_nombre.get().strip()

        if len(nombre):
            messagebox.showinfo('Información', f'¡Hola, {nombre}!')
        else:
            messagebox.showwarning('Mensaje', 'Debe escribir un nombre.')

def main():
    app = tk.Tk()
    app.title('Ventana Principal - Captura Datos')
    app.geometry('350x300')

    ventana = VentanaPrincipal(app)

    ventana.mainloop()

if __name__ == "__main__":
    main()
