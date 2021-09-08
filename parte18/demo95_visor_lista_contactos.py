import re
import tkinter as tk


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
        texto = '{}, {}'.format(contacto.apellido, contacto)

        self.lbx_contactos.insert(indice, texto)
    
    def eliminar(self, indice):
        self.lbx_contactos.delete(indice, indice)
    
    def actualizar(self, contacto, indice):
        self.eliminar(indice)
        self.insertar(contacto, indice)
    
    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lbx_contactos.curselection()[0])

        self.lbx_contactos.bind('<Double-Button-1>', handler)
