# Gestión de excepciones para acceso a elementos de una lista:

lenguajes = ['Python', 'C++', 'JavaScript', 'C#', 'Java', 'C']

print('Cantidad de elementos de la lista `lenguajes`:', len(lenguajes))

print('Primer elemento de la lista `lenguajes`:', lenguajes[0])

print()

indice = 6

try:
    print('Último elemento de la lista `lenguajes`:', lenguajes[indice])
except IndexError:
    print('El índice %i no existe en la lista `lenguajes`' % indice)

print('El programa ha finalizado.')
