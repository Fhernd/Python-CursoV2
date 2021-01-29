from tkinter import Canvas, PhotoImage, Tk, BOTH, NW

class DibujoImagen:

    def __init__(self, master):
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        canvas = Canvas(self.master, bg='white', height=500, width=500)
        canvas.pack(fill=BOTH)

        imagen = PhotoImage(file='parte18/python-logo-black.png')

        canvas.create_image(2, 2, image=imagen, anchor=NW)
        canvas.image = imagen

def main():
    master = Tk()
    master.title('Dibujo Imagen')
    master.geometry('500x500')

    ventana = DibujoImagen(master)

    master.mainloop()

if __name__ == '__main__':
    main()
