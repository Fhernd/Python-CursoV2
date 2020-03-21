# Ejercicio 9.10: Realizar cálculos de estadísticos básicos: media, mínimo, máximo.

numeros = [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]

suma = 0

for n in numeros:
    suma += n

print('La suma es:', suma)

minimo = numeros[0]

for i in range(1, len(numeros)):
    if numeros[i] < minimo:
        minimo = numeros[i]

print('El mínimo es:', minimo)

maximo = numeros[0]

for i in range(1, len(numeros)):
    if numeros[i] > maximo:
        maximo = numeros[i]

print('El máximo es:', maximo)
