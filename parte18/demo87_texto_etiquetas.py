import tkinter as tk
import webbrowser


class TextoEtiqueta(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Texto Etiquetas')
        self.geometry('350x350')
        self.resizable(0, 0)

        self.txa_contenido = tk.Text(self, width=60, height=15)

        self.btn_agregar_enlace = tk.Button(self, text='Agregar enlace')
        self.btn_agregar_enlace['command'] = self.agregar_enlace

        self.txa_contenido.tag_config('link', foreground='blue', underline=1)
        self.txa_contenido.tag_bind('link', '<Button-1>', self.abrir_enlace)
        self.txa_contenido.tag_bind('link', '<Enter>', lambda _: self.txa_contenido.config(cursor='hand2'))
        self.txa_contenido.tag_bind('link', '<Leave>', lambda _: self.txa_contenido.config(cursor=''))

        self.txa_contenido.pack()
        self.btn_agregar_enlace.pack(expand=True)
    
    def agregar_enlace(self):
        seleccion = self.txa_contenido.tag_ranges(tk.SEL)
        if seleccion:
            self.txa_contenido.tag_add('link', *seleccion)

    def abrir_enlace(self, evento):
        posicion = '@{},{} + 1c'.format(evento.x, evento.y)
        indice = self.txa_contenido.index(posicion)
        resultado = self.txa_contenido.tag_prevrange('link', indice)
        url = self.txa_contenido.get(*resultado)
        webbrowser.open(url)


def main():
    app = TextoEtiqueta()
    app.mainloop()


if __name__ == '__main__':
    main()
