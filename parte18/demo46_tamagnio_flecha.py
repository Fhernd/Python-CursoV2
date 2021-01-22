from tkinter import Canvas, Scale, Tk
import string

class Flecha:

    def __init__(self, master):
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        canvas = Canvas(self.master, width=50, height=50, bd=0, highlightthickness=0)

        canvas.create_polygon(0, 0, 1, 1, 2, 2, fill='blue', tags='flecha')
        canvas.create_line(0, 0, 1, 1, 2, 2, 0, 0, fill='black', tags='linea')

def main():
    app = Tk()
    app.title('Flecha - Escalar')
    app.geometry('200x300')
    
    ventana = Flecha(app)

    app.mainloop()

if __name__ == "__main__":
    main()
