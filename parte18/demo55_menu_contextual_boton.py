from tkinter import W, Label, OptionMenu, StringVar, Tk

class Aplicacion(Tk):
    def __init__(self):
        super().__init__()

        self.title('Uso de OptionMenu')
        self.geometry('350x120')
        self.lenguajes = ('Python', 'Java', 'Go', 'JavaScript', 'C++', 'C#', 'Swift')

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.lenguaje_selecionado = StringVar(self)

        lbl_seleccion_lenguaje = Label(self, text='Seleccione su lenguaje de programación favorito: ')
        lbl_seleccion_lenguaje.grid(column=0, row=0, sticky=W, padx=5, pady=5)

def main():
    app = Aplicacion()
    app.mainloop()

if __name__ == '__main__':
    main()
