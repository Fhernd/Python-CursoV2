# Ejercicio 5.5: Remover los valores duplicados en una lista.

numeros = [1, 2, 3, 1, 1, 1, 4, 5, 6, 3, 3, 2, 5]
print('Contenido actual de la lista `numeros`:', numeros)
print('Cantidad actual de la lista `numeros`:', len(numeros))

print()

# Solución #1:
print('Solución #1:')
numeros_sin_repetir = []

for n in numeros:
    if n not in numeros_sin_repetir:
        numeros_sin_repetir.append(n)

print('Contenido actual de la lista `numeros_sin_repetir`:', numeros_sin_repetir)
print('Cantidad actual de la lista `numeros_sin_repetir`:', len(numeros_sin_repetir))

print()

# Solución #2:
print('Solución #2')
conjunto_numeros = list(set(numeros))
print('Contenido actual de `conjunto_numeros`:', conjunto_numeros)
print('Cantidad actual de conjunto_numeros`:', len(conjunto_numeros))
