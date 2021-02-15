from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class ComentariosApp(Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Comentarios App')
        self.configure(background='gray')
        self.minsize(400, 400)

        self.estilo = ttk.Style()
        self.estilo.configure('TFrame', background='black')
        self.estilo.configure('TButton', background='#95A3B3')
        self.estilo.configure('TLabel', background='#1E152A', font=('Arial', 13))
        self.estilo.configure('Encabezado.TLabel', font=('Arial', 18, 'bold'))

        self.frm_encabezado = ttk.Frame(self)
        self.frm_encabezado.pack()

        self.img_logo = PhotoImage(file='parte18/python-logo.png')

        lbl_logo = ttk.Label(self.frm_encabezado, image=self.img_logo)
        lbl_logo.grid(column=0, row=0, rowspan=2)

        lbl_nombre_app = ttk.Label(self.frm_encabezado, text='ComentariosApp', style='Encabezado.TLabel')
        lbl_nombre_app.grid(column=1, row=0)

        lbl_indicaciones = ttk.Label(self.frm_encabezado, wraplength=300,
                    text=(
                        'Ingrese los datos a registrar:\nNombre, correo-e, y el texto del comentario.'
                    ))
        lbl_indicaciones.grid(column=1, row=1)

        self.frm_principal = ttk.Frame(self)
        self.frm_principal.pack()

        lbl_nombre = ttk.Label(self.frm_principal, text='Nombre:')
        lbl_nombre.grid(column=0, row=0, padx=5, sticky='sw')
        
        lbl_email = ttk.Label(self.frm_principal, text='Email:')
        lbl_email.grid(column=1, row=0, padx=5, sticky='sw')
        
        lbl_comentario = ttk.Label(self.frm_principal, text='Comentario:')
        lbl_comentario.grid(column=1, row=0, padx=5, sticky='sw')

        self.txt_nombre = ttk.Entry(self.frm_principal, width=25, font=('Arial', 11))
        self.txt_nombre.grid(column=0, row=1, padx=5)


def main():
    app = ComentariosApp()
    app.mainloop()

if __name__ == '__main__':
    main()
