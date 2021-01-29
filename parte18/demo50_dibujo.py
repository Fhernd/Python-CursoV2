from tkinter import Canvas, Tk

class Dibujo(object):

    def __init__(self, master):
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.canvas = Canvas(bg='white', height=300, width=300)
        self.canvas.pack()

        self.canvas.bind('<ButtonPress-1>', self.iniciar_dibujo)
        self.canvas.bind('<B1-Motion>', self.dibujar)
        self.canvas.bind('<Double-1>', self.limpiar)
        self.canvas.bind('<ButtonPress-3>', self.mover)

        self.tipos_figuras = [self.canvas.create_oval, self.canvas.create_rectangle]
        self.dibujo = None
    
    def iniciar_dibujo(self, evento):
        self.figura = self.tipos_figuras[0]
        self.tipos_figuras = self.tipos_figuras[1:] + self.tipos_figuras[:1]
        self.inicio = evento
        self.dibujo = None

    def dibujar(self, evento):
        canvas = evento.widget
        
        if self.dibujo:
            self.canvas.delete(self.dibujo)
        
        id_figura = self.figura(self.inicio.x, self.inicio.y, evento.x, evento.y)

        self.dibujo = id_figura

    def limpiar(self, evento):
        evento.widget.delete('all')

    def mover(self, evento):
        if self.dibujo:
            canvas = evento.widget
            diferencia_x = evento.x - self.inicio.x
            diferencia_y = evento.y - self.inicio.y

            canvas.move(self.dibujo, diferencia_x, diferencia_y)

            self.inicio = evento

def main():
    master = Tk()
    master.title('Dibujo')
    master.geometry('300x300')

    ventana = Dibujo(master)

    master.mainloop()

if __name__ == "__main__":
    main()
