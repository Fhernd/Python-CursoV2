import tkinter as tk
from tkinter import messagebox

class VentanaPrincipal(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        lbl_nombre = tk.Label(self, 'Nombre: ')
        lbl_nombre.grid(row=0, column=0)
        self.txt_nombre = tk.Entry(self)
        self.txt_nombre.grid(row=0, column=1)

        lbl_correo = tk.Label(self, 'Correo: ')
        lbl_correo.grid(row=1, column=0)
        self.txt_correo = tk.Entry(self)
        self.txt_correo.grid(row=1, column=1)

        self.registro_valido = tk.IntVar()
        self.chk_registro_valido = tk.Checkbutton(self, text='¿Está de acuerdo con los términos y condiciones?', variable=self.registro_valido)
        self.chk_registro_valido.grid(row=2, column=0)

        btn_validar_registro = tk.Button(self, text='Validar registro')
        btn_validar_registro['command'] = self.validar_registro
        btn_validar_registro.grid(row=3, column=0)
    
    def validar_registro(self):
        nombre = self.txt_correo.get().strip()
        correo = self.txt_correo.get().strip()

        if len(nombre) == 0:
            messagebox.showwarning('Mensaje', 'El campo Nombre es obligatorio.')
            return
