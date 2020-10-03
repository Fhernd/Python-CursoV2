import tkinter as tk
from tkinter import messagebox

class VentanaPrincipal(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)

        self.master = master
        self.pack()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        messagebox.showinfo('Mensaje informativo', '¡Hola, Tkinter!')
        messagebox.showwarning('Mensaje de advertencia', 'Revise todos los campos del formulario.')
        messagebox.showerror('Mensaje de error', 'Hay problemas con la conexión a Internet.')

def main():
    app = tk.Tk()
    app.title('Mensajes de Diálogo')
    app.geometry('350x350')

    ventana = VentanaPrincipal(app)
    ventana.mainloop()

if __name__ == "__main__":
    main()
