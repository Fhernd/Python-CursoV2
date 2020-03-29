# Ejercicio 11.4: Crear una función para invertir el contenido de una cadena de caracteres.

# Python => nohtyP

def invertir_cadena(texto):
    """
    Invierte una cadena de caracteres (texto).

    Parameters:
    texto: Cadena de caracteres (texto) a invertir.

    Returns:
    Cadena de caracteres invertida.
    """
    if isinstance(texto, str):
        resultado = ''

        for i in range(len(texto) - 1, -1, -1):
            resultado += texto[i]
        
        return resultado
    else:
        raise TypeError('No se ha especificado una cadena de caracteres como argumento.')


frase = '¡Python es tremendo!'

try:
    resultado = invertir_cadena(frase)
    print('Texto original:', frase)
    print('Texto invertido:', resultado)
except TypeError as e:
    print('ERROR:', e)

print()

frase = 1000

try:
    resultado = invertir_cadena(frase)
    print('Texto original:', frase)
    print('Texto invertido:', resultado)
except TypeError as e:
    print('ERROR:', e)

print()

frase = ['P', 'y', 't', 'h', 'o', 'n']

try:
    resultado = invertir_cadena(frase)
    print('Texto original:', frase)
    print('Texto invertido:', resultado)
except TypeError as e:
    print('ERROR:', e)
