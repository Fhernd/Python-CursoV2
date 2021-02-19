import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class FormularioRegistro(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
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
    
    def guardar(self):
        pass

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
