# Ejercicio 5.7: Seleccionar de forma aleatoria un elemento de una lista.

import random

numeros = list(range(1, 7))

numero = random.choice(numeros)

print('Se ha seleccionado de forma aleatoria el valor:', numero)
