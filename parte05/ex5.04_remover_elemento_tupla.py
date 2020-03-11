# Ejercicio 5.4: Remover un elemento (valor) de una tupla.

lenguajes = ('Python', 'JavaScript', 'Perl', 'C++', 'Java')
print('Contenido actual de la tupla `lenguajes`:', lenguajes)
print('Cantidad de elementos de la tupla `lenguajes`:', len(lenguajes))

lenguaje = 'Perl'

if lenguaje in lenguajes:
    
    # NOTA IMPORTANTE: Las tuplas no se pueden modificar. Las tuplas son inmutables.
    lenguajes = lenguajes[0:2] + lenguajes[3:]

    print()

    print('Contenido actual de la tupla `lenguajes`:', lenguajes)
    print('Cantidad de elementos de la tupla `lenguajes`:', len(lenguajes))

else:
    print('No existe un nombre de lenguaje con:', lenguaje)
