# Ejercicio 11.9: Crear una función recursiva para comprobar si una cadena es palíndromo.

# oso => oso
# ana => ana
# lateleletal => lateleletal
# correa => aerroc

def es_palindromo(palabra):
    """
    Determina si una palabra es palíndromo.

    Parameters:
    palabra: Palabra sobre la que se realiza la comprobación.

    Returns:
    True si la palabra es palíndromo, False en caso contrario.
    """
    if len(palabra) < 1:
        return True
    else:
        if palabra[0] == palabra[-1]:
            return es_palindromo(palabra[1:-1])
        else:
            return False

print('¿oso es palíndromo?:', es_palindromo('oso'))
print('¿lateleletal es palíndromo?:', es_palindromo('lateleletal'))
print('¿perro es palíndromo?:', es_palindromo('perro'))
