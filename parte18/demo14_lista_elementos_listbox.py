import tkinter as tk

class VentanaPrincipal(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        
        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.lbx_colores = tk.Listbox(self, height='7')
        self.lbx_colores.insert(0, 'Rojo')
        self.lbx_colores.insert(1, 'Verde')
        self.lbx_colores.insert(2, 'Azul')
        self.lbx_colores.insert(3, 'Amarillo')
        self.lbx_colores.insert(4, 'Blanco')
        self.lbx_colores.bind('<Double-1>', self.cambiar_color)
        self.lbx_colores.pack()

        self.color_seleccionado = tk.StringVar()
        self.lbl_color_seleccionado = tk.Label(self, text='Blanco', textvariable=self.color_seleccionado)
        self.lbl_color_seleccionado.pack()

    def cambiar_color(self, evento):
        color_seleccionado = self.lbx_colores.curselection()

        for c in color_seleccionado:
            if c == 0:
                self.master.configure(background='red')
                self.color_seleccionado.set('Rojo')
            elif c == 1:
                self.master.configure(background='green')
                self.color_seleccionado.set('Verde')
            elif c == 2:
                self.master.configure(background='blue')
                self.color_seleccionado.set('Azul')
            elif c == 3:
                self.master.configure(background='yellow')
                self.color_seleccionado.set('Amarillo')
            elif c == 4:
                self.master.configure(background='white')
                self.color_seleccionado.set('Blanco')

def main():
    app = tk.Tk()
    app.title('Ventana principal')
    app.geometry('350x350')

    ventana = VentanaPrincipal(app)
    ventana.mainloop()

if __name__ == "__main__":
    main()
