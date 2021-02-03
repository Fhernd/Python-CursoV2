from tkinter import W, Label, OptionMenu, StringVar, Tk

class Aplicacion(Tk):
    def __init__(self):
        super().__init__()

        self.title('Uso de OptionMenu')
        self.geometry('390x120')
        self.lenguajes = ('Python', 'Java', 'Go', 'JavaScript', 'C++', 'C#', 'Swift')

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.lenguaje_selecionado = StringVar(self)

        lbl_seleccion_lenguaje = Label(self, text='Seleccione su lenguaje de programación favorito: ')
        lbl_seleccion_lenguaje.grid(column=0, row=0, sticky=W, padx=5, pady=5)

        opm_lenguajes = OptionMenu(self, self.lenguaje_selecionado, self.lenguajes[0], *self.lenguajes, command=self.seleccionar_lenguaje)
        
        opm_lenguajes.grid(column=1, row=0, sticky=W, padx=5, pady=5)

        self.lbl_lenguaje_seleccionado = Label(self, foreground='blue')
        self.lbl_lenguaje_seleccionado.grid(column=0, row=1, sticky=W, padx=5, pady=5)
    
    def seleccionar_lenguaje(self, *args):
        self.lbl_lenguaje_seleccionado['text'] = f'Ha seleccionado: {self.lenguaje_selecionado.get()}'

def main():
    app = Aplicacion()
    app.mainloop()

if __name__ == '__main__':
    main()
