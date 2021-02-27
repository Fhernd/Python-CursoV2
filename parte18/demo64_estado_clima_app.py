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

        canvas = tk.Canvas(self, height=500, width=600)
        canvas.pack()

        img_cielo = PIL.Image.open('parte18/demo64_cielo.jpg')
        img_cielo = PIL.ImageTk.PhotoImage(img_cielo)
        lbl_cielo = tk.Label(self, image=img_cielo)
        lbl_cielo.place(relx=0, rely=0, relheight=1, relwidth=1)

        frm_componentes = tk.Frame(self, bg='#88B7B5', bd=5)
        frm_componentes.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor='n')

        self.txt_ciudad = tk.Entry(frm_componentes, font=('Arial', 17))
        self.txt_ciudad.place(relx=0, rely=0, relheight=1, relwidth=0.65)

def main():
    app = EstadoClimaApp()
    app.mainloop()

if __name__ == '__main__':
    main()
