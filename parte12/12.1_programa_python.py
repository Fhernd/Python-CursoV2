# Parte 12 - Programa Python:

def saludar(mensaje):
    print(mensaje)

class Persona:
    def __init__(self, documento, nombre):
        self.documento = documento
        self.nombre = nombre

edward = Persona(123456789, 'Edward Ortiz')

saludo = f'Hola, mi nombre es {edward.nombre}.'

saludar(saludo)
