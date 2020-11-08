import tkinter as tk

class UbicacionBotones(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.master.rowconfigure([0, 1], minsize=150)
        self.master.columnconfigure([0, 1], minsize=150)

        btn_a = tk.Button(text='A', font=('Arial', 23))
        btn_a.grid(row=0, column=0, sticky='nw')

        btn_b = tk.Button(text='B', font=('Arial', 23))
        btn_b.grid(row=0, column=1, stick='ne')

        btn_c = tk.Button(text='C', font=('Arial', 23))
        btn_c.grid(row=1, column=0, stick='sw')

        btn_d = tk.Button(text='D', font=('Arial', 23))
        btn_d.grid(row=1, column=1, stick='se')

def main():
    root = tk.Tk()
    root.title('Posición Botones')
    root.geometry('300x300')

    ventana = UbicacionBotones(root)
    ventana.mainloop()

if __name__ == "__main__":
    main()
