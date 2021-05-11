import tkinter as tk


class FormularioRegistro(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Formulario Registro')
        self.geometry('300x300')

        campos = ['Primer nombre', 'Primer apellido', 'Teléfono', 'Email']
        lbl_campos = [tk.Label(self, text=c) for c in campos]
        txt_campos = [tk.Entry(self) for _ in campos]

        self.componentes = list(zip(lbl_campos, txt_campos))

        btn_guardar = tk.Button(self, text='Guardar', command=self.guardar)
    
    def guardar(self):
        pass
