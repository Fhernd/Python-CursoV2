# Ciclos - for

numeros = [1, 2, 3, 4, 5]

total = 0

total = numeros[0] + numeros[1] + numeros[2] + numeros[3] + numeros[4]
print('Total de la suma de los números de 1 a 5:', total)

print()

total = 0

total += numeros[0]
total += numeros[1]
total += numeros[2]
total += numeros[3]
total += numeros[4]
# total += numeros[999]
print('Total de la suma de los números de 1 a 5:', total)

print()

numeros.append(6)
numeros.append(7)
numeros.append(8)
numeros.append(9)
numeros.append(10)

print('Contenido actual de la lista `numeros`:', numeros)

total += numeros[5]
total += numeros[6]
total += numeros[7]
total += numeros[8]
total += numeros[9]

print('Total de la suma de los números de 1 a 10:', total)

print()

# Uso explícito del ciclo for para resolver un problema que requiere iterar (recorrer) todos los elementos 
# de una colección (lista):

total = 0

for i in range(0, len(numeros)):
    total += numeros[i]

print('Total de la suma de los números de 1 a 10:', total)
