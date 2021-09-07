import re


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
