from tkinter import *
from tkinter import ttk

class MesesTabs(Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Meses del año')
        self.geometry('580x100')

        self.twd_meses = ttk.Notebook(self)

        tbs_meses = [ttk.Frame(self.twd_meses) for _ in range(12)]
        meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto'
                'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

def main():
    app = MesesTabs()
    app.mainloop()

if __name__ == '__main__':
    main()
