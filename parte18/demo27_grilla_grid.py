import tkinter as tk

class Tabla(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        for i in range(4):
            for j in range(4):
                celda = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
                celda.grid(row=i, column=j)

                lbl_etiqueta = tk.Label(master=celda, text=f'Fila {i + 1}\nColumna {j + 1}')
                lbl_etiqueta.pack()

def main():
    app = tk.Tk()
    app.title('Organización Tabla')
    app.geometry('400x400')

    ventana = Tabla(app)
    ventana.mainloop()

if __name__ == "__main__":
    main()
