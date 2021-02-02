from tkinter import E, W, Button, Tk
from tkinter.ttk import Progressbar

class Proceso:
    def __init__(self, master):
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        pbr_proceso = Progressbar(self.master, orient='horizontal', mode='indeterminate', length=300)
        pbr_proceso.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

        btn_iniciar = Button(self.master, text='Iniciar', command=pbr_proceso.start)
        btn_iniciar.grid(row=1, column=0, padx=10, pady=10, sticky=E)

        btn_detener = Button(self.master, text='Detener', command=pbr_proceso.stop)
        btn_detener.grid(row=1, column=1, padx=10, pady=10, sticky=W)


def main():
    master = Tk()
    master.title('Proceso')
    master.geometry('320x150')

    proceso = Proceso(master)

    master.mainloop()

if __name__ == '__main__':
    main()
