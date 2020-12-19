from tkinter import *

class CalculadoraApp:

    def __init__(self, master):
        self.master = master
        self.master.title('Calculadora App')
        self.master.geometry('312x324')
        self.master.resizable(0, 0)

        self.inicializar_gui()

    def inicializar_gui(self):
        pass

def main():
    app = Tk()
    ventana = CalculadoraApp(app)
    app.mainloop()

if __name__ == "__main__":
    main()
