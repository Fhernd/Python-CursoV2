# Ejercicio 5.2: Invertir el contenido de una tupla.

# (1, 2, 3, 4, 5)
# (5, 4, 3, 2, 1)

numeros = (1, 2, 3, 4, 5)
print(numeros)

print()

# Solución 1:
print('Solución 1:')
numeros_invertidos = []

for i in range(len(numeros) - 1, -1, -1):
    numeros_invertidos.append(numeros[i])

numeros_invertidos = tuple(numeros_invertidos)
print(numeros_invertidos)

print()

# Solución 2:
print('Solución 2:')
numeros_invertidos = tuple(reversed(numeros))
print(numeros_invertidos)
