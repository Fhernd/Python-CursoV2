import re
import tkinter as tk
from tkinter import messagebox

class VentanaPrincipal(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        patron = r'^[a-z]+@[a-z]+\.[a-z]{2,3}$'
        self.regex_correo = re.compile(patron)

        self.inicializar_gui()
    
    def inicializar_gui(self):
        lbl_nombre = tk.Label(self, text='Nombre: ')
        lbl_nombre.grid(row=0, column=0)
        self.nombre = tk.StringVar()
        self.txt_nombre = tk.Entry(self, textvariable=self.nombre)
        self.txt_nombre.grid(row=0, column=1)

        lbl_correo = tk.Label(self, text='Correo: ')
        lbl_correo.grid(row=1, column=0)
        self.correo = tk.StringVar()
        self.txt_correo = tk.Entry(self, textvariable=self.correo)
        self.txt_correo.grid(row=1, column=1)

        self.registro_valido = tk.IntVar()
        self.chk_registro_valido = tk.Checkbutton(self, text='¿Está de acuerdo con los términos y condiciones?', variable=self.registro_valido)
        self.chk_registro_valido.grid(row=2, column=0)

        btn_validar_registro = tk.Button(self, text='Validar registro')
        btn_validar_registro['command'] = self.validar_registro
        btn_validar_registro.grid(row=3, column=0)
    
    def validar_registro(self):
        nombre = self.txt_nombre.get().strip()
        correo = self.txt_correo.get().strip()
        
        if len(nombre) == 0:
            messagebox.showwarning('Mensaje', 'El campo Nombre es obligatorio.')
            return

        if len(correo) == 0:
            messagebox.showwarning('Mensaje', 'El campo Correo es obligatorio.')
            return
        
        if self.regex_correo.match(correo) is None:
            messagebox.showwarning('Mensaje', 'El campo Correo debe ser una dirección válida.')
            return
        
        if self.registro_valido.get():
            messagebox.showinfo('Mensaje', 'El registro ha sido satisfactorio.')
        else:
            messagebox.showwarning('Mensaje', 'Debe aceptar los Términos y Condiciones para completar el registro.')

def main():
    app = tk.Tk()
    app.title('Registro de Usuarios')
    app.geometry('400x300')

    ventana = VentanaPrincipal(app)
    ventana.mainloop()

if __name__ == "__main__":
    main()
