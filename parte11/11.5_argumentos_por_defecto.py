# Argumentos por defecto en una función:
print('Argumentos por defecto en una función:')

def saludar(nombre, saludo='Hola', pais='Colombia'):
    """
    Saluda utilizando un saludo, un nombre y un país de procedencia.

    Parameters:
    nombre: Nombre de la persona.
    saludo: El tipo de saludo (e.g., Hola, Buenos días, Buenas tardes, buenas noches).
    pais: Nacionalidad de la persona.

    Returns:
    Una frase con el saludo que incluye el nombre y la nacionalidad.
    """
    frase = f'{saludo}, mi nombre es {nombre}, y soy de {pais}.'

    return frase


resultado = saludar('Edward', saludo='Buenos días')

print('Resultado:', resultado)

print()

resultado = saludar('Daniela', pais='México')
print('Resultado:', resultado)
