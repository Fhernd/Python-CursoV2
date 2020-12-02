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
        
        img_logo_python_2 = Image.open('parte18/python-logo-file-black.png')
        img_logo_python_2 = ImageTk.PhotoImage(img_logo_python_2)
        lbl_logo_python_2 = tk.Label(self.master, image=img_logo_python_2)
        lbl_logo_python_2.image = img_logo_python_2
        lbl_logo_python_2.place(x=170, y=50)
        
        img_logo_python_3 = Image.open('parte18/python-logo-name-black.png')
        img_logo_python_3 = ImageTk.PhotoImage(img_logo_python_3)
        lbl_logo_python_3 = tk.Label(self.master, image=img_logo_python_3)
        lbl_logo_python_3.image = img_logo_python_3
        lbl_logo_python_3.place(x=30, y=350)


def main():
    master = tk.Tk()
    master.title('Imágenes')
    master.geometry('500x500')
    
    ventana = Imagenes(master)
    master.mainloop()

if __name__ == "__main__":
    main()
