# Tipo de dato compuesto - tupla - estático:

punto = (2, 5)
print('Tipo de dato:', type(punto))
print('Contenido de la variable punto:', punto)
print('Cantidad elementos de la tupla punto:', len(punto))

print()

# Acceso a los elementos de una tupla:
x = punto[0]
y = punto[1]
print('El valor en x es igual a:', x)
print('El valor en y es igual a:', y)

print()

# Desempaquetamiento:
abscisa, ordenada = punto
print('El valor en x es igual a:', abscisa)
print('El valor en y es igual a:', ordenada)

print()

# Acceso con índices negativos (de derecha a izquierda):

penultimo_elemento = punto[-2]
ultimo_elemento = punto[-1]
print('El valor en x es igual a:', penultimo_elemento)
print('El valor en y es igual a:', ultimo_elemento)

print()

# Concepto de inmutabilidad en una tupla:
# punto[0] = 3 # Generar error TypeError
# punto[1] = 7 # Generar error TypeError

punto = (3, 7)
x = punto[0]
y = punto[1]
print('El valor en x es igual a:', x)
print('El valor en y es igual a:', y)

print()

# Iteración de un objeto tipo tupla (tuple):
numeros_primos = (2, 3, 5, 7, 11, 13, 17, 19)

print('Cantidad elementos de la tupla numeros_primos:', len(numeros_primos))

# Iteración con un ciclo while:
i = 0
print('Iteración con un ciclo while:')
while i < len(numeros_primos):
    print(f'El valor del elemento en el índice {i} es igual a {numeros_primos[i]}.')
    i = i + 1

print()

# Iteración con un ciclo for:
print('Iteración con un ciclo for:')
for i in range(len(numeros_primos)):
    print(f'El valor del elemento en el índice {i} es igual a {numeros_primos[i]}.')

print()

# Iteración un ciclo for mejorado:
print('Iteración con un ciclo for mejorado:')
for p in numeros_primos:
    print('Valor:', p)
