# Introducción a las funciones - Unidades de reutilización y encapsulación de información:

# 1. Creación de una función:
print('1. Creación de una función:')

def sumar(numero_1, numero_2):
    """
    Suma dos números (sean enteros o punto flotante).

    Parameters:
    numero_1: primer valor a sumar.
    numero_2: segundo valor a sumar.

    Returns:
    Suma de dos números (enteros o reales).
    """
    suma = numero_1 + numero_2

    return suma

x = 2
y = 3

resultado = sumar(x, y)
print('El resultado de sumar {} y {} es igual a {}.'.format(x, y, resultado))

print()

# 2. Invocación de una función:
resultado = sumar(2, 3)
print('El resultado de sumar {} y {} es igual a {}.'.format(x, y, resultado))

print()

# 3. Obtener documentación/ayuda de una función:
print('3. Obtener documentación/ayuda de una función:')

print()

help(sumar)

print()

help(print)
