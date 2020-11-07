import tkinter as tk


class TablaAutoajustable(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        for i in range(4):
            self.master.columnconfigure(i, weight=1, minsize=80)
            self.master.rowconfigure(i, weight=1, minsize=55)

            for j in range(4):
                celda = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
                celda.grid(row=i, column=j, padx=5, pady=5)

                lbl_etiqueta = tk.Label(master=celda, text=f'Fila {i + 1}\nColumna {j + 1}')
                lbl_etiqueta.pack(padx=5, pady=5)

def main():
    app = tk.Tk()
    app.title('Organización Tabla')
    app.geometry('400x400')

    ventana = TablaAutoajustable(app)
    ventana.mainloop()

if __name__ == "__main__":
    main()

