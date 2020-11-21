import tkinter as tk

class VisualizacionImagen:

    def __init__(self, master):
        self.master = master

        self.inicializar_gui()

    def inicializar_gui(self):
        canvas = tk.Canvas(self.master, width=920, height=500)
        canvas.pack()

        img_logo_python = tk.PhotoImage(file='parte18/python-logo.png')
        canvas.create_image(0, 0, anchor=tk.NW, image=img_logo_python)
        canvas.image = img_logo_python

def main():
    root = tk.Tk()
    root.title('Logo Python')

    ventana = VisualizacionImagen(root)

    root.mainloop()

if __name__ == "__main__":
    main()
