import tkinter as tk

class AperturaArchivo(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.btn_seleccionar_archivo = tk.Button(self, text='Seleccionar archivo...')
        self.btn_seleccionar_archivo['command'] = self.seleccionar_archivo
        self.btn_seleccionar_archivo.pack()

        # TODO: crear área de texto

    def seleccionar_archivo(self):
        pass

def main():
    app = tk.Tk()
    app.title('Apertura Archivos')
    app.geometry('350x400')

    ventana = AperturaArchivo(app)

    ventana.mainloop()

if __name__ == "__main__":
    main()
