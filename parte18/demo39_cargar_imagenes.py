from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

class SelectorImagenes:

    def __init__(self, master):
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        btn_seleccionar_imagen = Button(self.master, text='Seleccionar imagen...', command=self.seleccionar_imagen)
        btn_seleccionar_imagen.grid(row=0, columnspan=4)
    
    def seleccionar_imagen(self):
        pass

def main():
    master = Tk()
    master.title('Selector Imágenes')
    master.geometry('550x550')
    master.resizable(width=True, height=True)

    ventana = SelectorImagenes(master)
    master.mainloop()

if __name__ == "__main__":
    main()
