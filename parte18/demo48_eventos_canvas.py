from tkinter import messagebox, Canvas, Tk

class EventosCanvas:

    def __init__(self, master):
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        pass

def main():
    master = Tk()
    master.title('Eventos Canvas')
    master.geometry('300x300')

    ventana = EventosCanvas(master)

    master.mainloop()

if __name__ == "__main__":
    main()
