import tkinter as tk

class VentanaColores(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.inicializar_gui()

    def inicializar_gui(self):

        frm_amarillo = tk.Frame(master=self.master, width=200, height=100, bg='#FCD116')
        frm_amarillo.pack(fill=tk.Y, side=tk.LEFT)
        
        frm_azul = tk.Frame(master=self.master, width=150, height=100, bg='#003893')
        frm_azul.pack(fill=tk.Y, side=tk.LEFT)
        
        frm_rojo = tk.Frame(master=self.master, width=100, height=100, bg='#CE1126')
        frm_rojo.pack(fill=tk.Y, side=tk.LEFT)

def main():
    app = tk.Tk()
    app.title('Colores Bandera Colombia')
    app.geometry('450x300')

    ventana = VentanaColores(app)
    ventana.mainloop()

if __name__ == "__main__":
    main()
