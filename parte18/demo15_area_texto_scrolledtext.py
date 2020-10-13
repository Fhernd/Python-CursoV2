import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

class FormularioComentario(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.inicializar_gui()

    def inicializar_gui(self):
        tk.Label(self, text='Deje un comentario...').grid(row=0, column=0)

        self.txa_comentario = scrolledtext.ScrolledText(self, width=40, height=15, wrap=tk.WORD, font=('Arial', 17))
        self.txa_comentario.grid(column=0, padx=10, pady=10)
        self.txa_comentario.focus()

        tk.Button(self, text='Guardar comentario', command=self.guardar_comentario).grid(column=0)
    
    def guardar_comentario(self):
        comentario = self.txa_comentario.get("1.0", tk.END)

        messagebox.showinfo('Mensaje', comentario)

def main():
    app = tk.Tk()
    app.title('Comentario')
    app.geometry('550x500')

    ventana = FormularioComentario(app)
    ventana.mainloop()

if __name__ == "__main__":
    main()
