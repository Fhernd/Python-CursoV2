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

print()

resultado = saludar('Oliva', pais='España', saludo='Buenas noches')
print('Resultado:', resultado)

print()

def exponenciacion(base, exponente=2):
    """
    Calcula la exponenciación de un número base respecto a un exponente.

    Parameters:
    base: Base de la exponenciación.
    exponente: Potencia de la exponenciación (valor por defecto 2).

    Returns:
    Exponenciación de una base y un exponente.
    """
    resultado = base ** exponente

    return resultado

potencia = exponenciacion(5)
print('El resultado de la exponenciación es:', potencia)

print()

potencia = exponenciacion(10, 3)
print('El resultado de la exponenciación es:', potencia)
