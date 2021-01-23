from tkinter import Canvas, Frame, RAISED, Tk, X

class Ovalos:
    def __init__(self, master):
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        frm_principal = Frame(self.master, width=500, height=400, bd=1)
        frm_principal.pack()

        frm_canvas = Frame(frm_principal, bd=2, relief=RAISED)
        frm_canvas.pack(expand=1, fill=X, padx=5, pady=10)

        canvas = Canvas(frm_canvas, bg='white', height=100, width=340)
        canvas.pack()

def main():
    master = Tk()
    master.title('Óvalos')

    ventana = Ovalos(master)

    master.mainloop()

if __name__ == "__main__":
    main()
