from tkinter import Canvas, Tk

class Dibujo(object):

    def __init__(self, master):
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        canvas = Canvas(bg='white', height=300, width=300)
        canvas.pack()

        canvas.bind('<ButtonPress-1>', self.iniciar_dibujo)
        canvas.bind('<B1-Motion>', self.dibujar)
        canvas.bind('<Double-1>', self.limpiar)
        canvas.bind('<ButtonPress-3>', self.mover)

        self.tipos_figuras = [canvas.create_oval, canvas.create_rectangle]
        self.dibujo = None
    
    def iniciar_dibujo(self, evento):
        self.figura = self.tipos_figuras[0]
        self.tipos_figuras = self.tipos_figuras[1:] + self.tipos_figuras[:1]
        self.dibujo = None

    def dibujar(self, evento):
        pass

    def limpiar(self, evento):
        pass

    def mover(self, evento):
        pass

def main():
    master = Tk()
    master.title('Dibujo')
    master.geometry('300x300')

    ventana = Dibujo(master)

    master.mainloop()

if __name__ == "__main__":
    main()
