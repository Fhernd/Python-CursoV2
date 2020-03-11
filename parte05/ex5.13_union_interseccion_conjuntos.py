# Ejercicio 5.13: Realizar operaciones de unión e intersección de conjuntos.

numeros = set(list(range(1, 11)))
primos = set([2, 3, 5, 7, 11, 13, 17, 19])

print('Contenido del conjunto `numeros`:', numeros)
print('Contenido del conjunto `primos`:', primos)

print()

union = numeros.union(primos)
print('Contenido del conjunto `union`:', union)
print('Cantidad de elementos del conjunto `union`:', len(union))

print()

interseccion = primos.intersection(numeros)
print('Contenido del conjunto `interseccion`:', interseccion)
print('Cantidad de elementos del conjunto `interseccion`:', len(interseccion))
