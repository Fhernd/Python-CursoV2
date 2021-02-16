from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class ComentariosApp(Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Comentarios App')
        self.configure(background='white')
        self.minsize(400, 400)

        self.estilo = ttk.Style()
        self.estilo.configure('TFrame', background='white')
        self.estilo.configure('TButton', background='#95A3B3')
        self.estilo.configure('TLabel', background='#FFFFFF', font=('Arial', 13))
        self.estilo.configure('Encabezado.TLabel', font=('Arial', 18, 'bold'))

        self.frm_encabezado = ttk.Frame(self)
        self.frm_encabezado.pack()

        self.img_logo = PhotoImage(file='parte18/python-logo-black.png')

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
        lbl_comentario.grid(column=0, row=2, padx=5, sticky='sw')

        self.txt_nombre = ttk.Entry(self.frm_principal, width=25, font=('Arial', 11))
        self.txt_nombre.grid(column=0, row=1, padx=5)
        
        self.txt_email = ttk.Entry(self.frm_principal, width=25, font=('Arial', 11))
        self.txt_email.grid(column=1, row=1, padx=5)

        self.txt_comentario = Text(self.frm_principal, width=50, height=7, font=('Arial', 11))
        self.txt_comentario.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

        btn_guardar_comentario = ttk.Button(self.frm_principal, text='Guardar')
        btn_guardar_comentario['command'] = self.guardar_comentario
        btn_guardar_comentario.grid(column=0, row=4, padx=5, pady=5, sticky='e')
        
        btn_limpiar = ttk.Button(self.frm_principal, text='Limpiar')
        btn_limpiar['command'] = self.limpiar
        btn_limpiar.grid(column=1, row=4, padx=5, pady=5, sticky='w')
    
    def guardar_comentario(self):
        nombre = self.txt_nombre.get().strip()

        if len(nombre) == 0:
            messagebox.showwarning('Mensaje', 'El campo Nombre es obligatorio.')
            return
        
        email = self.txt_email.get().strip()
        if len(email) == 0:
            messagebox.showwarning('Mensaje', 'El campo Email es obligatorio.')
            return
        
        comentario = self.txt_comentario.get(1.0, 'end')
        if len(comentario) == 0:
            messagebox.showwarning('Mensaje', 'El campo Comentario es obligatorio.')
            return
        
        with open('parte18/demo59_comentarios.txt', 'at', encoding='utf-8') as f:
            f.write(f'{nombre};{email};{comentario}')

            messagebox.showinfo('Mensaje', 'El comentario se ha guardado de forma satisfactoria.')

            self.limpiar()

    def limpiar(self):
        self.txt_nombre.delete(0, 'end')
        self.txt_email.delete(0, 'end')
        self.txt_comentario.delete(1.0, 'end')


def main():
    app = ComentariosApp()
    app.mainloop()

if __name__ == '__main__':
    main()
