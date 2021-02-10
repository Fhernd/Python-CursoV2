from tkinter import Tk

class Aplicacion(Tk):
    def __init__(self):
        super().__init__()
        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Aplicación Pantalla Completa')
        self.attributes('-fullscreen', True)
    
def main():
    app = Aplicacion()
    app.mainloop()

if __name__ == '__main__':
    main()
