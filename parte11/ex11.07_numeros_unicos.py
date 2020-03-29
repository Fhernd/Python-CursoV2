# Ejercicio 11.7: Tomar una lista de números e identificar los números únicos.

def numeros_unicos(numeros):
    """
    Obtiene los números únicos en una tupla o lista.

    Parameters:
    numeros: Lista o tupla con números.

    Returns:
    Lista con los valores únicos.
    """
    if isinstance(numeros, (tuple, list)):
        unicos = []

        for n in numeros:
            if n not in unicos:
                unicos.append(n)
        
        return unicos

    raise TypeError('El argumento `numeros` debe ser una lista o una tupla.')


valores = [2, 5, 2, 2, 3, 7, 5, 7, 11, 13]

print('El contenido de la lista `valores` es:', valores)
print('Cantidad de elementos de la lista `valores` es:', len(valores))

try:
    resultado = numeros_unicos(valores)
    print('El contenido de la lista `resultado` es:', resultado)
    print('Cantidad de elementos de la lista `resultado` es:', len(resultado))
except TypeError as e:
    print('ERROR:', e)

print()

valores = '[2, 5, 2, 2, 3, 7, 5, 7, 11, 13]'

print('El contenido de la lista `valores` es:', valores)
print('Cantidad de elementos de la lista `valores` es:', len(valores))

try:
    resultado = numeros_unicos(valores)
    print('El contenido de la lista `resultado` es:', resultado)
    print('Cantidad de elementos de la lista `resultado` es:', len(resultado))
except TypeError as e:
    print('ERROR:', e)
