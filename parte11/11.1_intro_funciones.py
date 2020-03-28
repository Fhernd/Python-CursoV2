# Introducción a las funciones - Unidades de reutilización y encapsulación de información:

# 1. Creación de una función:
print('1. Creación de una función:')

def sumar(numero_1, numero_2):
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
