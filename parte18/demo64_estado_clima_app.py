import tkinter as tk
import requests
import PIL.Image
import PIL.ImageTk

class EstadoClimaApp(tk.Tk):

    def __init___(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Estado del Clima')

def main():
    app = EstadoClimaApp()
    app.mainloop()

if __name__ == '__main__':
    main()
