import tkinter as tk
from tkinter import ttk

class Apariencia(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Tema Colores')
        self.geometry('400x300')

        self.estilo = ttk.Style(self)

        ttk.Label(self, text='Nombre:').grid(column=0, row=0, padx=10, pady=10, sticky='w')

        ttk.Entry(self).grid(column=1, row=0, padx=10, pady=10, sticky='w')

        ttk.Button(self, text='Mostrar').grid(column=2, row=0, padx=10, pady=10, sticky='w')

        self.tema_seleccionado = tk.StringVar()

        lbf_contenedor = ttk.LabelFrame(self, text='Temas')
        lbf_contenedor.grid(ipadx=20, ipady=20, padx=10, pady=10, sticky='w')

        for t in self.estilo.theme_names():
            rbn_tema = ttk.Radiobutton(
                lbf_contenedor,
                text=t,
                value=t,
                variable=self.tema_seleccionado,
                command=self.cambiar_tema
            )

            rbn_tema.pack(expand=True, fill='both')
        
    def cambiar_tema(self):
        self.estilo.theme_use(self.tema_seleccionado.get())

def main():
    app = Apariencia()
    app.mainloop()

if __name__ == '__main__':
    main()
