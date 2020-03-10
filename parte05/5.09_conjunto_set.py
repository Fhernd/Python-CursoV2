# Tipo de dato compuesto mutable y dinámico: set (conjunto)

# 1. Creación de un conjunto:
print('1. Creación de un conjunto:')

conjunto_1 = {'Juan', 'Oliva', 'Edward', 'Daniela', 'Juan', 'Juan', 'Germán'}
conjunto_2 = set(['Juan', 'Oliva', 'Edward', 'Daniela', 'Juan', 'Juan', 'Germán'])

print('Contenido de la variable `conjunto_1`:', conjunto_1)
print('Cantidad de elementos del conjunto `conjunto_1`:', len(conjunto_1))
print('El tipo de dato de la variable `conjunto_1` es:', type(conjunto_1))
print()
print('Contenido de la variable `conjunto_2`:', conjunto_2)
print('Cantidad de elementos del conjunto `conjunto_2`:', len(conjunto_2))
print('El tipo de dato de la variable `conjunto_2` es:', type(conjunto_2))

print()

# 1.2 Creación de conjuntos por medio de cadenas de caracteres:
print('1.2 Creación de conjuntos por medio de cadenas de caracteres:')
frase = 'Python es un lenguaje de programación'
caracteres = set(frase)
print('Contenido de la variable conjunto `caracteres`:', caracteres)
print('El tipo de dato de la variable `caracteres` es:', type(caracteres))
print('Cantidad de elementos del conjunto `caracteres`:', len(caracteres))
print('Cantidad de caracteres de la variable string `frase`:', len(frase))

print()

# 1.3 Creación de un conjunto por medio de una tupla (tuple):
print('1.3 Creación de un conjunto por medio de una tupla (tuple):')

primos = (7, 3, 5, 2, 7, 5, 13, 11, 19, 2, 2, 2, 5, 5)
print('Contenido de la variable `primos`:', primos)
print('Cantidad de elementos de la variable `primos`:', len(primos))
print('Tipo de dato de la variable tupla `primos`:', type(primos))

print()

primos_unicos = set(primos)
print('Contenido de la variable `primos_unicos`:', primos_unicos)
print('Cantidad de elementos de la variable `primos_unicos`:', len(primos_unicos))
print('Tipo de dato de la variable tupla `primos_unicos`:', type(primos_unicos))

print()

# 1.4 Creación del conjunto de colores del arcoiris:
print('1.4 Creación del conjunto de colores del arcoiris:')

arco_iris = {'Rojo', 'Naranja', 'Amarillo', 'Verde', 'Azul', 'Añil'}
print('Contenido de la variable `arco_iris`:', arco_iris)
print('Cantidad de elementos de la variable `arco_iris`:', len(arco_iris))
print('Tipo de dato de la variable `arco_iris`:', type(arco_iris))

print()

# 2. Agregación de elementos a un conjunto utilizando el método `add()`:
print('2. Agregación de elementos a un conjunto utilizando el método `add()`:')

arco_iris.add('Violeta')
print('Contenido de la variable `arco_iris`:', arco_iris)
print('Cantidad de elementos de la variable `arco_iris`:', len(arco_iris))
print('Tipo de dato de la variable `arco_iris`:', type(arco_iris))

print()

arco_iris.add('Violeta')
arco_iris.add('Violeta')

print('Contenido de la variable `arco_iris`:', arco_iris)
print('Cantidad de elementos de la variable `arco_iris`:', len(arco_iris))
print('Tipo de dato de la variable `arco_iris`:', type(arco_iris))

print()

# 3. Iteración de un conjunto:
print('3. Iteración de un conjunto:')

for c in arco_iris:
    print(c)
