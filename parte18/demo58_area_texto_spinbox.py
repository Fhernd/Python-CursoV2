from tkinter import Tk, INSERT, WORD
from tkinter import ttk
from tkinter import scrolledtext

class EntradaDatos(Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Spinbox + ScrolledText')
        self.minsize(400, 400)

        self.spx_numero = ttk.Spinbox(self, from_=0, to=10, command=self.capturar_nuevo_valor)
        self.spx_numero.grid(column=0, row=1)

        self.txa_numeros = scrolledtext.ScrolledText(self, width=30, height=15, wrap=WORD)
        self.txa_numeros.grid(column=1, row=1)
    
    def capturar_nuevo_valor(self):
        valor = self.spx_numero.get()
        self.txa_numeros.insert(INSERT, valor)

def main():
    app = EntradaDatos()
    app.mainloop()

if __name__ == '__main__':
    main()
