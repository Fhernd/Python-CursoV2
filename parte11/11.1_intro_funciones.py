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

print()

# 4. Creación de una función para alternar los valores de dos variables:
print('4. Creación de una función para intercambiar los valores de dos variables:')

# a = 2, b = 3
# a = 3, b = 2

# auxiliar = 2
# a = 3
# b = 2

def intercambiar_valores(a, b):
    """
    Intercambia los valores de dos variables.

    Parameters:
    a: primer valor.
    b: segundo valor.

    Returns:
    Los valores de a y b intercambiados.
    """
    auxiliar = a
    a = b
    b = auxiliar

    return a, b


x = 2
b = 3

print('Valores de las variables `x` e `y` antes del intercambio:')
print(f'x = {x} - y = {y}')

resultado = intercambiar_valores(x, b)

x = resultado[0]
y = resultado[1]

print('Valores de las variables `x` e `y` después del intercambio:')
print(f'x = {x} - y = {y}')

print()

# 5. Uso de funcionalidad que provee en su defecto (incorporado) el lenguaje de programación:
print('5. Uso de funcionalidad que provee en su defecto (incorporado) el lenguaje de programación:')

x = 2
y = 3

resultado = x + y
print('El resultado de sumar {} y {} es igual a {}.'.format(x, y, resultado))

print()

print('Valores de las variables `x` e `y` antes del intercambio:')
print(f'x = {x} - y = {y}')

x, y = y, x

print('Valores de las variables `x` e `y` antes del intercambio:')
print(f'x = {x} - y = {y}')
