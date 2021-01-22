from tkinter import Canvas, Scale, Tk, VERTICAL

class Flecha:

    def __init__(self, master):
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        canvas = Canvas(self.master, width=50, height=50, bd=0, highlightthickness=0)

        canvas.create_polygon(0, 0, 1, 1, 2, 2, fill='blue', tags='flecha')
        canvas.create_line(0, 0, 1, 1, 2, 2, 0, 0, fill='black', tags='linea')

        self.escala = Scale(self.master,
                            orient=VERTICAL,
                            length=285,
                            from_=0,
                            to=250,
                            tickinterval=50,
                            command=lambda h, c=canvas:establecerAltura(c, h))

        self.escala.grid(row=0, column=0, sticky='NE')
        canvas.grid(row=0, column=1, sticky='NWSE')

        self.escala.set(100)

def establecerAltura(canvas, altura):
    altura = int(altura)
    altura = altura + 21

    y = altura - 30
    if y < 21:
        y = 21
    
    canvas.coords('flecha', 15, 20, 35, 20, 35, y, 45, y, 25, altura,5, y,15, y, 15, 20)
    canvas.coords('linea', 15, 20, 35, 20, 35, y, 45, y, 25, altura, 5, y, 15, y, 15, 20)

def main():
    app = Tk()
    app.title('Flecha - Escalar')
    app.geometry('200x300')
    
    ventana = Flecha(app)

    app.mainloop()

if __name__ == "__main__":
    main()
