# Expresiones lambda - Funciones anónimas
print('Expresiones lambda - Funciones anónimas')

def sumar(a, b):
    resultado = a + b
    return resultado

x = 2
y = 3

print('La suma de {} + {} es igual a {}'.format(x, y, sumar(x, y)))

print()

sumar_lambda = lambda a, b: a + b
print('La suma de {} + {} es igual a {}'.format(x, y, sumar_lambda(x, y)))

print()

def cuadrado(n):
    return n ** 2

cuadrado_lambda = lambda n: n ** 2

numero = 10

print('El cuadrado de {} es igual a {}'.format(numero, cuadrado(numero)))
print('El cuadrado de {} es igual a {}'.format(numero, cuadrado_lambda(numero)))

print()

# Filtrar el contenido de una lista:
print('Filtrar el contenido de una lista:')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Contenido de la variable `numeros`:', numeros)
print('Cantidad de elementos en la lista `numeros`:', len(numeros))

def extraer_impares(lista):
    impares = []

    for n in lista:
        if n % 2 != 0:
            impares.append(n)
    
    return impares

print()

resultado = extraer_impares(numeros)

print('Contenido de la variable `resultado`:', resultado)
print('Cantidad de elementos en la lista `resultado`:', len(resultado))

print()

resultado = [n for n in numeros if n % 2 != 0]
print('Contenido de la variable `resultado`:', resultado)
print('Cantidad de elementos en la lista `resultado`:', len(resultado))

print()

resultado = list(filter(lambda n: n % 2 != 0, numeros))
print('Contenido de la variable `resultado`:', resultado)
print('Cantidad de elementos en la lista `resultado`:', len(resultado))

print()

def filtro(n):
    return n % 2 != 0

resultado = list(filter(filtro, numeros))
print('Contenido de la variable `resultado`:', resultado)
print('Cantidad de elementos en la lista `resultado`:', len(resultado))

print()

# Utilizar la función `map()` para crear un mapeo (mapping) del contenido de una lista (iterable):

def elevar_cuadrado(lista):
    cuadrados = []

    for n in lista:
        cuadrados.append(n ** 2)
    
    return cuadrados

resultado = elevar_cuadrado(numeros)
print('Contenido de la variable `numeros`:', numeros)
print('Todos los números de la lista `numeros` al cuadrado:', resultado)

print()

resultado = [n**2 for n in numeros]
print('Todos los números de la lista `numeros` al cuadrado:', resultado)

print()

resultado = list(map(lambda n: n ** 2, numeros))
print('Todos los números de la lista `numeros` al cuadrado:', resultado)
