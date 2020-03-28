# Lista variable de argumentos de una función:
print('Lista variable de argumentos de una función:')

# def sumar(a, b):
#     return a + b

# def sumar(a, b, c):
#     return a + b + c

# def sumar(a, b, c, d):
#     return a + b + c + d

# def sumar(a, b, c, d, e):
#     return a + b + c + d + e

def sumar(*valores):
    suma = 0

    for v in valores:
        suma += v

    return suma


resultado = sumar(1)
print('El resultado de la suma es igual:', resultado)

print()

resultado = sumar(1, 2)
print('El resultado de la suma es igual:', resultado)

print()

resultado = sumar(1, 2, 3)
print('El resultado de la suma es igual:', resultado)
