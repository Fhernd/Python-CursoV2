import tkinter as tk
from tkinter import scrolledtext
from tkinter.filedialog import askopenfile

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

        self.txa_contenido_archivo = scrolledtext.ScrolledText(self, width=40, height=30, wrap=tk.WORD, font=('Arial', 15))
        self.txa_contenido_archivo.pack()

    def seleccionar_archivo(self):
        archivo = askopenfile(mode='r', filetypes=[('Archivos de texto', '*.txt')])

        if archivo is not None:
            contenido = archivo.read()
            self.txa_contenido_archivo.insert(tk.INSERT, contenido)

def main():
    app = tk.Tk()
    app.title('Apertura Archivos')
    app.geometry('350x400')

    ventana = AperturaArchivo(app)

    ventana.mainloop()

if __name__ == "__main__":
    main()
