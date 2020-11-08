import tkinter as tk

class VentanaPrincipal(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.master.columnconfigure(0, minsize=300)
        self.master.rowconfigure([0, 1], minsize=150)

        lbl_etiqueta_x = tk.Label(text='X', font=('Arial', 23))
        lbl_etiqueta_x.grid(row=0, column=0, sticky='ne')

        lbl_etiqueta_y = tk.Label(text='Y', font=('Arial', 23))
        lbl_etiqueta_y.grid(row=1, column=0, sticky='sw')

def main():
    root = tk.Tk()
    root.title('Posición Etiquetas')
    root.geometry('300x300')

    ventana = VentanaPrincipal(root)
    ventana.mainloop()

if __name__ == "__main__":
    main()
