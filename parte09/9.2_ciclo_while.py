# Ciclo while

numeros = [1, 2, 3, 4, 5]

i = 0

while i < len(numeros):
    print(numeros[i])
    i += 1

print()

print('Contenido de la lista `numeros`:', numeros)

print()

# Suma de los elementos de una lista con un ciclo while:
print('Suma de los elementos de una lista con un ciclo while:')

i = 0
total = 0

while i < len(numeros):
    total += numeros[i]
    i += 1

print('Suma de los números de 1 a 5:', total)
