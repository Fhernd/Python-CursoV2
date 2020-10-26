import tkinter as tk

class Aplicacion(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        mbr_principal = tk.Menu(self.master)
        mnu_archivo = tk.Menu(mbr_principal)

        mnu_archivo.add_command(label='Abrir')
        mnu_archivo.add_command(label='Guardar')
        mnu_archivo.add_command(label='Salir', command=self.salir)
        mbr_principal.add_cascade(label='Archivo', menu=mnu_archivo)

        self.master.config(menu=mbr_principal)
    
    def salir(self):
        self.master.destroy()

def main():
    ventana_principal = tk.Tk()
    ventana_principal.title('Barra de menu')
    ventana_principal.geometry('350x300')

    app = Aplicacion(ventana_principal)
    app.mainloop()

if __name__ == "__main__":
    main()
