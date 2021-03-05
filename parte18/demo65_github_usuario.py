import tkinter as tk
import requests
import PIL

class GitHupUsuarioApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('GitHub Usuarios Consulta')
        self.geometry('350x450')

        frm_entrada_datos = tk.Frame(self)
        frm_entrada_datos.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.9, anchor='n')

        self.txt_usuario = tk.Entry(frm_entrada_datos, font=('Arial', 13))
        self.txt_usuario.place(relx=0, rely=0, relheight=1, relwidth=0.65)

        btn_consultar = tk.Button(frm_entrada_datos, font=('Arial', 13), text='Consultar')
        btn_consultar.place(relx=0.7, rely=0, relheight=1, relwidth=0.3)
        btn_consultar['command'] = self.consultar

        lbf_resultado = tk.LabelFrame(self, text='Resultados')
        lbf_resultado.place(relx=0.5, rely=0.25, relheight=0.9, relwidth=0.9, anchor='n')

        lbl_nombre = tk.Label(lbf_resultado, text='Nombre:', width=20)
        lbl_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.txt_nombre = tk.Entry(lbf_resultado)
        self.txt_nombre.grid(row=0, column=1, padx=10, pady=10)

    def consultar(self):
        pass

def main():
    app = GitHupUsuarioApp()
    app.mainloop()

if __name__ == '__main__':
    main()
