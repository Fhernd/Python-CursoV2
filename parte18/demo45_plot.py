from tkinter import Button, Canvas, E, N, Tk

class Plot(object):

    def __init__(self, master):
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        canvas = Canvas(self.master, width=450, height=300, bg='white')
        canvas.pack()

        btn_salir = Button(self.master, text='Salir')
        btn_salir['command'] = self.salir
        btn_salir.pack()

        canvas.create_line(100, 250, 400, 250, width=2)
        canvas.create_line(100, 250, 100, 50, width=2)

        for i in range(11):
            x = 100 + (i * 30)
            canvas.create_line(x, 250, x, 245, width=2)
            canvas.create_text(x, 254, text='%d' % (10.0 * i), anchor=N)

        for i in range(6):
            y = 250 - (i * 40)
            canvas.create_line(100, y, 105, y, width=2)
            canvas.create_text(96, y, text='%5.1f' % (50.0 * i), anchor=E)

        escalado = []
        puntos = [(12, 56), (20, 94), (33, 98), (45, 120), (61, 180), (75, 160), (98, 223)]

        for x, y in puntos:
            escalado.append((100 + 3 * x, 250 - (4*y)/5))

        canvas.create_line(escalado, fill='black', smooth=1)

        for x, y in escalado:
            canvas.create_oval(x - 6, y - 6, x + 6, y + 6, width=1, outline='black', fill='yellow')
    
    def salir(self):
        self.master.quit()

def main():
    app = Tk()
    ventana = Plot(app)
    app.mainloop()

if __name__ == "__main__":
    main()
