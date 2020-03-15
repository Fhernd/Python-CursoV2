# Precedencia (jerarquía) de operadores:

from math import sqrt

resultado = 5/2 + 4
print('El contenido de la variable `resultado` es:', resultado)

print()

resultado = 4 + 5/2
print('El contenido de la variable `resultado` es:', resultado)

print()

resultado = 5/(2 + 4)
print('El contenido de la variable `resultado` es:', resultado)

print()

resultado = 5/(2 + 4) + sqrt(25)
print('El contenido de la variable `resultado` es:', resultado)

print()

resultado = 25 ** 1 / 2
print('El contenido de la variable `resultado` es:', resultado)

print()

resultado = 25 ** (1 / 2)
print('El contenido de la variable `resultado` es:', resultado)
