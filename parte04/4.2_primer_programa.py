def sumar(a, b):
    suma = a + b
    return suma

numero_1 = float(input('Ingrese el primer número: '))
numero_2 = float(input('Ingrese el segundo número: '))

resultado = sumar(numero_1, numero_2)

print('La suma de {} y {} es igual {}.'.format(numero_1, numero_2, resultado))
