import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile

class AlmacenamientoArchivo(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.txa_contenido = ScrolledText(self, width=35, height=19, wrap=tk.WORD)
        self.txa_contenido.pack()

        btn_guardar_contenido = tk.Button(self, text='Guardar contenido...')
        btn_guardar_contenido['command'] = self.guardar_contenido
        btn_guardar_contenido.pack()
    
    def guardar_contenido(self):
        pass

def main():
    app = tk.Tk()
    app.title('Almacenamiento contenido')
    app.geometry('350x350')

    ventana = AlmacenamientoArchivo(app)
    ventana.mainloop()

if __name__ == "__main__":
    main()
