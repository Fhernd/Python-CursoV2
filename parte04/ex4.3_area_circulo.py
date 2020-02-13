'''
Ejercicio 4.3: Solicitar al usuario el radio de un círculo y calcular su área.
'''
import math

radio = float(input('Digite el radio del círculo: '))

# pi * r ^ 2
area = math.pi * radio ** 2

print('El área es igual a:', area)
