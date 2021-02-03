from tkinter import Entry, Label, LabelFrame, Radiobutton, StringVar, Tk
from tkinter.ttk import Style

class Apariencia(Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Tema Colores')
        self.geometry('400x300')

        self.estilo = Style(self)

        Label(self, text='Nombre').grid(column=0, row=0, padx=10, pady=10, sticky='w')

        Entry(self).grid(column=1, row=0, padx=10, pady=10, sticky='w')

def main():
    app = Apariencia()
    app.mainloop()

if __name__ == '__main__':
    main()
