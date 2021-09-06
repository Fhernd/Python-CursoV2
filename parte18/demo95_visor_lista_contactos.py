import re

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
        pass
