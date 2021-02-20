import re
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class FormularioRegistro(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
        self.definir_patrones_validaciones()
    
    def inicializar_gui(self):
        self.title('Validación Datos')
        self.minsize(400, 350)

        lbl_titulo = tk.Label(self, text='FORMULARIO DE REGISTRO')
        lbl_titulo.grid(row=0, column=1, pady=10)

        frm_principal = tk.Frame(self, bd=7, relief='groove')
        frm_principal.grid(row=1, column=1, padx=10, pady=10)

        lbl_nombre = tk.Label(frm_principal, text='Nombre:', justify=tk.LEFT)
        lbl_nombre.grid(row=0, column=0, sticky=tk.W)
        self.txt_nombre = tk.Entry(frm_principal, width=20)
        self.txt_nombre.grid(row=0, column=1)
        
        lbl_contrasegnia = tk.Label(frm_principal, text='Contraseña:')
        lbl_contrasegnia.grid(row=1, column=0, sticky=tk.W)
        self.txt_contrasegnia = tk.Entry(frm_principal, width=20)
        self.txt_contrasegnia.grid(row=1, column=1)
        
        lbl_contrasegnia_repetir = tk.Label(frm_principal, text='Contraseña repetir:')
        lbl_contrasegnia_repetir.grid(row=2, column=0, sticky=tk.W)
        self.txt_contrasegnia_repetir = tk.Entry(frm_principal, width=20)
        self.txt_contrasegnia_repetir.grid(row=2, column=1)
        
        lbl_email = tk.Label(frm_principal, text='Email:')
        lbl_email.grid(row=3, column=0, sticky=tk.W)
        self.txt_email = tk.Entry(frm_principal, width=20)
        self.txt_email.grid(row=3, column=1)
        
        lbl_documento = tk.Label(frm_principal, text='Documento:')
        lbl_documento.grid(row=4, column=0, sticky=tk.W)
        self.txt_documento = tk.Entry(frm_principal, width=20)
        self.txt_documento.grid(row=4, column=1)
        
        lbl_pais = tk.Label(frm_principal, text='País:')
        lbl_pais.grid(row=5, column=0, sticky=tk.W)
        self.cbx_pais = ttk.Combobox(frm_principal, width=20)
        paises = ('Colombia', 'Chile', 'Venezuela', 'México', 'Brasil', 'Uruguay')
        self.cbx_pais['values'] = paises
        self.cbx_pais.current(0)
        self.cbx_pais.grid(row=5, column=1)

        lbl_ahorros = tk.Label(frm_principal, text='Ahorros:')
        lbl_ahorros.grid(row=6, column=0, sticky=tk.W)
        self.txt_ahorros = tk.Entry(frm_principal, width=20)
        self.txt_ahorros.grid(row=6, column=1)

        btn_guardar = tk.Button(frm_principal, text='Guardar', command=self.guardar)
        btn_guardar.grid(row=7, column=2)
        
        btn_limpiar = tk.Button(frm_principal, text='Limpiar', command=self.limpiar)
        btn_limpiar.grid(row=7, column=3)
        
        btn_salir = tk.Button(frm_principal, text='Salir', command=self.salir)
        btn_salir.grid(row=7, column=4)
    
    def definir_patrones_validaciones(self):
        patron_nombre = r'^[^\s]+( [^\s]+)+$'
        self.regex_nombre = re.compile(patron_nombre)

        patron_contrasegnia = r'^[a-zA-Z0-9]{8,16}$'
        self.regex_contrasegnia = re.compile(patron_contrasegnia)

        patron_email = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        self.regex_email = re.compile(patron_email)

        patron_documento = r'^[0-9]{7,10}$'
        self.regex_documento = re.compile(patron_documento)

        patron_ahorros = r'^\b(([1-9][0-9]*)?[0-9]\.[0-9]+)\b$'
        self.regex_ahorros = re.compile(patron_ahorros)

    
    def guardar(self):
        nombre = self.txt_nombre.get().strip()
        
        if re.match(self.regex_nombre, nombre) is None:
            messagebox.showwarning('Mensaje', 'El campo Nombre debe incluir Nombre y Apellido')
            return
        
        contrasegnia = self.txt_contrasegnia.get().strip()
        if re.match(self.regex_contrasegnia, contrasegnia) is None:
            messagebox.showwarning('Mensaje', 'El campo Contraseña debe tener mínimo 8 caracteres, máximo 16.')
            return
        
        contrasegnia_repetir = self.txt_contrasegnia_repetir.get()
        if re.match(self.regex_contrasegnia, contrasegnia_repetir) is None:
            messagebox.showwarning('Mensaje', 'El campo Contraseña Repetir debe tener mínimo 8 caracteres, máximo 16.')
            return
        
        if contrasegnia != contrasegnia_repetir:
            messagebox.showwarning('Mensaje', 'Las contraseñas deben ser iguales.')
            return
        
        email = self.txt_email.get().strip()
        if re.match(self.regex_email, email) is None:
            messagebox.showwarning('Mensaje', 'El campo Email no es válido.')
            return
        
        documento = self.txt_documento.get().strip()
        if re.match(self.regex_documento, documento) is None:
            messagebox.showwarning('Mensaje', 'El campo Documento debe ser un número con mínimo 7 dígitos, máximo 10.')
            return
        
        ahorros = self.txt_ahorros.get().strip()
        if re.match(self.regex_ahorros, ahorros) is None:
            messagebox.showwarning('Mensaje', 'El campo Ahorros debe ser un número real (e.g., 1000.53).')
            return
        
        messagebox.showinfo('Mensaje', 'Los datos se guardaron de forma satisfactoria.')
        
        self.limpiar()

    def limpiar(self):
        self.txt_nombre.delete(0, 'end')
        self.txt_contrasegnia.delete(0, 'end')
        self.txt_contrasegnia_repetir.delete(0, 'end')
        self.txt_email.delete(0, 'end')
        self.txt_documento.delete(0, 'end')
        self.cbx_pais.current(0)
        self.txt_ahorros.delete(0, 'end')

    def salir(self):
        self.destroy()

def main():
    app = FormularioRegistro()
    app.mainloop()

if __name__ == '__main__':
    main()
