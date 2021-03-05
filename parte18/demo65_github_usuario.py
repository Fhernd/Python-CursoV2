import tkinter as tk
import requests
import PIL

class GitHupUsuarioApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('GitHub Usuarios Consulta')

        frm_entrada_datos = tk.Frame(self)
        frm_entrada_datos.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor='n')

        self.txt_usuario = tk.Entry(frm_entrada_datos, font=('Arial', 15))
        self.txt_usuario.place(relx=0, rely=0, relheight=1, relwidth=0.65)

def main():
    app = GitHupUsuarioApp()
    app.mainloop()

if __name__ == '__main__':
    main()
