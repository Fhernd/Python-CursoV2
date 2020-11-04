import tkinter as tk

class Bandera(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        frm_amarillo = tk.Frame(master=self.master, width=450, height=300, bg='#FCD116')
        frm_amarillo.pack(fill=tk.BOTH, side=tk.TOP, expand=1)

        frm_azul = tk.Frame(master=self.master, width=450, height=150, bg='#003893')
        frm_azul.pack(fill=tk.BOTH, side=tk.TOP, expand=1)

        frm_rojo = tk.Frame(master=self.master, width=450, height=150, bg='#CE1126')
        frm_rojo.pack(fill=tk.BOTH, side=tk.TOP, expand=1)

def main():
    root = tk.Tk()
    root.title('Bandera Colombia')
    root.geometry('450x600')

    ventana = Bandera(root)
    ventana.mainloop()

if __name__ == "__main__":
    main()
