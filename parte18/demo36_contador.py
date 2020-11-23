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
    
    def reducir(self):
        pass

def main():
    root = tk.Tk()
    root.title('Controles Reducción/Aumento')
    
    contador = Contador(root)
    root.mainloop()

if __name__ == "__main__":
    main()
