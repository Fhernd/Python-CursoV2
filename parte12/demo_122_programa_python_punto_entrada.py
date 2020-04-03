# Programa Python con punto de entrada:

def saludar(mensaje):
    print(mensaje)

class Persona:
    def __init__(self, documento, nombre):
        self.documento = documento
        self.nombre = nombre

def main():
    edward = Persona(123456789, 'Edward Ortiz')

    saludo = f'Hola, mi nombre es {edward.nombre}.'

    saludar(saludo)

if __name__ == '__main__':
    main()
