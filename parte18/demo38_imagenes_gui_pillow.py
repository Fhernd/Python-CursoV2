import tkinter as tk
from tkinter.ttk import Style
from PIL import Image, ImageTk

class Imagenes:

    def __init__(self, master):
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        Style().configure('TFrame', background='#FFF')

        img_logo_python_1 = Image.open('parte18/python-logo-black.png')
        img_logo_python_1 = ImageTk.PhotoImage(img_logo_python_1)
        lbl_logo_python_1 = tk.Label(self.master, image=img_logo_python_1)
        lbl_logo_python_1.image = img_logo_python_1
        lbl_logo_python_1.place(x=10, y=10)

def main():
    master = tk.Tk()
    master.title('Imágenes')
    master.geometry('500x500')
    
    ventana = Imagenes(master)
    master.mainloop()

if __name__ == "__main__":
    main()
