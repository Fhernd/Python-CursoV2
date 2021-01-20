from tkinter import Button, Canvas, Tk

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
    
    def salir(self):
        self.master.quit()

def main():
    app = Tk()
    ventana = Plot(app)
    app.mainloop()

if __name__ == "__main__":
    main()
