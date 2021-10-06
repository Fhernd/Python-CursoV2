import csv
import re
import tkinter as tk
from tkinter import messagebox as mb
import sqlite3


def dato_obligatorio(dato, mensaje):
    if not dato:
        raise ValueError(mensaje)
    
    return dato


def coincide(dato, regex, mensaje):
    if dato and not regex.match(dato):
        raise ValueError(mensaje)
    
    if not dato:
        dato_obligatorio(dato, mensaje)
    
    return dato

class Contacto(object):
    regex_email = re.compile(r'[^@]+@[^@]+\.[^@]+')
    regex_telefono = re.compile(r'[1-9][0-9]{9}')

    def __init__(self, apellido, nombre, email, telefono):
        self.apellido = apellido
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, valor):
        self._apellido = dato_obligatorio(valor, 'El apellido es un campo obligatorio.')
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, valor):
        self._email = coincide(valor, self.regex_email, 'Formato inválido para el email.')


class ListaContactos(tk.Frame):

    def __init__(self, root, **kwargs):
        super().__init__(root)

        self.lbx_contactos = tk.Listbox(self, **kwargs)
        scl_contactos = tk.Scrollbar(self, command=self.lbx_contactos.yview)

        self.lbx_contactos.config(yscrollcommand=scl_contactos.set)
        scl_contactos.pack(side=tk.RIGHT, fill=tk.Y)
        self.lbx_contactos.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    
    def insertar(self, contacto, indice=tk.END):
        texto = '{}, {}'.format(contacto.apellido, contacto.nombre)

        self.lbx_contactos.insert(indice, texto)
    
    def eliminar(self, indice):
        self.lbx_contactos.delete(indice, indice)
    
    def actualizar(self, contacto, indice):
        self.eliminar(indice)
        self.insertar(contacto, indice)
    
    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lbx_contactos.curselection()[0])

        self.lbx_contactos.bind('<Double-Button-1>', handler)


class FormularioContacto(tk.LabelFrame):
    campos = ('Apellido', 'Nombre', 'Email', 'Teléfono')

    def __init__(self, root, **kwargs):
        super().__init__(root, text='Contacto', padx=10, pady=10, **kwargs)

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.frm_contacto = tk.Frame(self)
        self.campos_entradas = list(map(self.crear_campo, enumerate(self.campos)))

        self.frm_contacto.pack()
    
    def crear_campo(self, campo):
        posicion, texto = campo

        lbl_campo = tk.Label(self.frm_contacto, text=texto)
        lbl_campo.grid(row=posicion, column=0)

        txt_campo = tk.Entry(self.frm_contacto, width=25)
        txt_campo.grid(row=posicion, column=1)

        return txt_campo

    def cargar_datos(self, contacto):
        valores = (contacto.apellido, contacto.nombre, contacto.email, contacto.telefono)

        for campo, valor in zip(self.campos_entradas, valores):
            campo.delete(0, tk.END)
            campo.insert(0, valor)
    
    def obtener_detalles(self):
        valores = [e.get() for e in self.campos_entradas]

        try:
            return Contacto(*valores)
        except ValueError as e:
            mb.showwarning('Error de validación', str(e), parent=self)
    
    def limpiar(self):
        for e in self.campos_entradas:
            e.delete(0, tk.END)


class AplicacionVisorListaContactos(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Visor Lista Contactos')
        self.lista_contactos = ListaContactos(self, height=12)
        self.formulario_contacto = FormularioContacto(self)

        self.contactos = self.cargar_contactos()

        for c in self.contactos:
            self.lista_contactos.insertar(c)
        
        self.lista_contactos.pack(side=tk.LEFT, padx=10, pady=10)
        self.formulario_contacto.pack(side=tk.LEFT, padx=10, pady=10)

        self.lista_contactos.bind_doble_click(self.mostrar_contacto)
    
    def cargar_contactos(self):
        sql = 'SELECT rowid, apellidos, nombres, email, telefono FROM contacto'
        
        contactos = []
        
        with sqlite3.connect('parte18/demo96_contactos.db') as conexion:
            for r in conexion.execute(sql):
                contacto = Contacto(*r[1:])
                contactos.append(contacto)
        
        return contactos

    
    def mostrar_contacto(self, indice):
        contacto = self.contactos[indice]

        self.formulario_contacto.cargar_datos(contacto)


def main():
    app = AplicacionVisorListaContactos()
    app.mainloop()


if __name__ == '__main__':
    main()
