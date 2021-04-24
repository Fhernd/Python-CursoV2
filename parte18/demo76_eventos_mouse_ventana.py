import tkinter as tk
from tkinter import messagebox


class VentanaEventosMouse(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Eventos Mouse sobre Ventana')
        self.geometry('400x400')

        frm_principal = tk.Frame(self, bg='green', height=400, width=400)

        frm_principal.bind('<Button-1>', self.mostrar_datos)
        frm_principal.bind('<Double-Button-1>', self.mostrar_datos)
        frm_principal.bind('<ButtonRelease-1>', self.mostrar_datos)
        frm_principal.bind('<B1-Motion>', self.mostrar_datos)
        # frm_principal.bind('<Enter>', self.mostrar_datos)
        # frm_principal.bind('<Leave>', self.mostrar_datos)

        frm_principal.pack(padx=50, pady=50)
    
    def mostrar_datos(self, evento):
        posicion = f'(x={evento.x}, y={evento.y})'

        mensaje = f'Nombre del evento: {evento.type} - Posición: {posicion}'

        messagebox.showinfo('Evento', mensaje)


def main():
    app = VentanaEventosMouse()
    app.mainloop()


if __name__ == '__main__':
    main()
