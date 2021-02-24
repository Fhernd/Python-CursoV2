from tkinter import *
from tkinter import ttk

class MesesTabs(Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Meses del año')
        self.geometry('650x100')

        self.twd_meses = ttk.Notebook(self)

        tbs_meses = [ttk.Frame(self.twd_meses) for _ in range(12)]
        meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto',
                'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
        
        for i in range(len(meses)):
            print(meses[i])
            self.twd_meses.add(tbs_meses[i], text=meses[i])
        
        frases_meses = ('Enero (Jano), dios de los portales',
                        'Febrero (Febrau), mes de las hogueras purificatorias',
                        'Marzo (Marte), dios de la guerra',
                        'Abril (Aprilis), Apertura de las flores',
                        'Mayo (Maia), diosa de la abundancia',
                        'Junio (Juno), diosa del hogar y la familia',
                        'Julio (Julio Cesar)',
                        'Agosto (Octavio Augusto)',
                        'Septiembre, Séptimo mes del año',
                        'Octubre, Noveno mes del año',
                        'Noviembre, Décimo mes del año',
                        'Diciembre, Undécimo mes del año')
        
        for i in range(len(tbs_meses)):
            Label(tbs_meses[i], text=frases_meses[i]).grid(column=8,row=8)
        
        self.twd_meses.pack(expand=1, fill='both')

def main():
    app = MesesTabs()
    app.mainloop()

if __name__ == '__main__':
    main()
