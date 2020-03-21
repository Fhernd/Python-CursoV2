# Ejercicio 9.6: Encontrar todos los números pares que hay en el rango 100 a 400.

# Solución:

pares = []

for i in range(100, 401):
    if i % 2 == 0:
        pares.append(i)

print('Cantidad de elementos en la lista `pares`:', len(pares))
print('Contenido de la variable `pares`:', pares)
