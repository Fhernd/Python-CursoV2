from tkinter import Canvas, Tk

class Dibujo(object):

    def __init__(self, master):
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        pass


def main():
    master = Tk()
    master.title('Dibujo')
    master.geometry('300x300')

    ventana = Dibujo(master)

    master.mainloop()

if __name__ == "__main__":
    main()
