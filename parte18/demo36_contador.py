import tkinter as tk

class Contador:

    def __init__(self, master):
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.master.rowconfigure(0, minsize=50, weight=1)
        self.master.columnconfigure([0, 1, 2], minsize=50, weight=1)

        btn_reducir = tk.Button(self.master, text='-', command=self.reducir)
        btn_reducir.grid(row=0, column=0, sticky='nsew')

        self.lbl_contador = tk.Label(master=self.master, text='0')
        self.lbl_contador.grid(row=0, column=1)

        btn_aumentar = tk.Button(master=self.master, text='+', command=self.aumentar)
        btn_aumentar.grid(row=0, column=2, sticky='nsew')
    
    def reducir(self):
        valor = int(self.lbl_contador['text'])
        self.lbl_contador['text'] = f'{valor - 1}'

    def aumentar(self):
        valor = int(self.lbl_contador['text'])
        self.lbl_contador['text'] = f'{valor + 1}'

def main():
    root = tk.Tk()
    root.title('Controles Reducción/Aumento')
    root.geometry('300x100')
    
    contador = Contador(root)
    root.mainloop()

if __name__ == "__main__":
    main()
