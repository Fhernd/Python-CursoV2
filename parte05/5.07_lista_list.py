# Tipo de dato compuesto: lista
# Las listas son un tipo de dato dinámico

# 1. Creación de una lista:
numeros = [2, 4, 6, 8, 10]
print('Tipo de dato de la variable numeros:', type(numeros))
print('Cantidad de elementos:', len(numeros))
print('Contenido:', numeros)

print()

# 2. Acceso a los elementos de una lista:
dos = numeros[0]
print('El primer elemento (índice 0) de la lista es:', dos)
diez = numeros[4]
print('El último elemento (índice 4) de la lista es:', diez)

diez = numeros[-1]
print('El último elemento (índice -1) de la lista es:', diez)

print()

subseccion = numeros[1:4]
print('Tipo de dato de la variable subseccion:', type(subseccion))
print('Cantidad de elementos:', len(subseccion))
print('Contenido:', subseccion)

print()

# Acceso con desempaquetamiento:
print('Acceso a datos de una lista con desempaquetamiento:')
cuatro, seis, ocho = subseccion
print(cuatro, seis, ocho)

print()

# Acceso a un índice no existen:
# Izquierda a derecha: 0 hasta n - 1
# Derecha a izquierda: -1 hasta -n

# valor = numeros[8] # Genera ValueError
# valor = numeros[-6] # Genera ValueError

print()

# 2. Modificación de una lista:
print('2. Modificación de elementos de una lista:')
print('El primer elemento (índice 0) de la lista es:', numeros[0])
numeros[0] = 1
print('El primer elemento (índice 0) de la lista es:', numeros[0])

print()

print('El último elemento (índice -1) de la lista es:', numeros[-1])
numeros[-1] = 12
print('El último elemento (índice -1) de la lista es:', numeros[-1])

print()

# Iteración de listas:
# Iteración de lista con ciclo while:
print('Iteración de lista con ciclo while:')

i = 0
while i < len(numeros):
    print('Índice: {} - Valor: {}'.format(i, numeros[i]))
    i += 1

print()

print('Iteración de lista con ciclo while (del último elemento al primero):')

i = len(numeros) - 1
while i >= 0:
    print('Índice: {} - Valor: {}'.format(i, numeros[i]))
    i -= 1

print()

print('Iteración con índices de una lista con un ciclo for:')

for i in range(0, len(numeros)):
    print('Índice: {} - Valor: {}'.format(i, numeros[i]))

print()

print('Iteración con índices de una lista con un ciclo for (último hacia el primer elemento):')

for i in range(len(numeros) - 1, -1, -1):
    print('Índice: {} - Valor: {}'.format(i, numeros[i]))

print()

print('Iteración por elemento de una lista usando un ciclo for:')

for n in numeros:
    print('Valor: {}'.format(n))

print()

print('Iteración de lista con la función `enumerate()`:')

for i, v in enumerate(numeros):
    print('Índice: {} - Valor: {}'.format(i, v))

print()

# Operaciones sobre listas (clase `list`):

# Inserción de elementos en una lista por medio de `append()`:
print('Inserción de elementos en una lista por medio de `append()`:')

print('Cantidad actual de elementos en la lista `numeros`:', len(numeros))
numeros.append(14)
numeros.append(16)
print('Cantidad actual de elementos en la lista `numeros`:', len(numeros))
print('Contenido actual de la lista `numeros`:', numeros)

print()

print('Inserción de elementos en una lista por medio de `insert()`:')
numeros.insert(1, 2)
print('Contenido actual de la lista `numeros`:', numeros)

print()

numeros.insert(-1, 15)
print('Contenido actual de la lista `numeros`:', numeros)

print()

print('Remoción de un elemento con la función `remove()`:')
print('Cantidad actual de elementos en la lista `numeros`:', len(numeros))
numeros.remove(1)
print('Cantidad actual de elementos en la lista `numeros`:', len(numeros))
print('Contenido actual de la lista `numeros`:', numeros)

# numeros.remove(1) # Produce el error ValueError: debido a que no existe el valor en la lista.

print()

print('Remoción de elementos de una lista con el método `pop()`:')
ultimo_elemento = numeros.pop()
print(f'Se ha eliminado {ultimo_elemento} de la lista `numeros`.')

print()

ocho = numeros.pop(numeros.index(8))
print(f'Se ha eliminado {ocho} de la lista `numeros`.')
print('Contenido actual de la lista `numeros`:', numeros)

print()

ultimo_elemento = numeros.pop(-1)
print(f'Se ha eliminado {ultimo_elemento} de la lista `numeros`.')
print('Contenido actual de la lista `numeros`:', numeros)

print()

# numeros.pop(20) # Genera error IndexError.

print()

print('Uso del método `count()` para contar las ocurrencias de un elemento en una lista:')
numeros.append(14)
numeros.append(14)
numeros.append(14)
ocurrencias = numeros.count(14)
print('Cantidad de veces que se halla 14 en la lista `numeros`: %i' % ocurrencias)
print('Contenido actual de la lista `numeros`:', numeros)

print()

ocurrencias = numeros.count(0)
print('Cantidad de veces que se halla 0 en la lista `numeros`: %i' % ocurrencias)
print('Contenido actual de la lista `numeros`:', numeros)

print()

print('Inversión del contenido de una lista con la función `reverse()`:')

print('Contenido actual de la lista `numeros`:', numeros)
numeros.reverse()
print('Contenido actual de la lista `numeros`:', numeros)

print()

print('Eliminación de todos los elementos de una lista con el método `clear()`:')
print('Cantidad actual de elementos en la lista `numeros`:', len(numeros))
# numeros.clear()
del numeros[:]
print('Cantidad actual de elementos en la lista `numeros`:', len(numeros))
