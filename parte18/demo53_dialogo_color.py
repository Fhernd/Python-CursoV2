from tkinter import colorchooser, Button, Tk

class SeleccionColor:

    def __init__(self, master):
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        Button(self.master, text='Seleccionar color...', command=self.seleccionar_color).pack(expand=True)
    
    def seleccionar_color(self):
        colores = colorchooser.askcolor(title='Seleccione su color favorito...')

        self.master.configure(bg=colores[1])

def main():
    master = Tk()
    master.title('Selección Color')
    master.geometry('300x300')

    ventana = SeleccionColor(master)

    master.mainloop()

if __name__ == '__main__':
    main()
