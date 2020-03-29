# Ejercicio 11.6: Usar una función para contar minúsculas y mayúsculas en una cadena.

def contador_minusculas_mayusculas(texto):
    """
    Cuenta la cantidad de minúsculas y mayúsculas que hay en un texto.

    Parameters:
    texto: Cadena de caracteres con el texto.

    Returns:
    Tupla con la cantidad de minúsculas y mayúsculas.
    """
    if isinstance(texto, str):
        minusculas = 0
        mayusculas = 0

        for c in texto:
            if c.isalpha():
                if c.islower():
                    minusculas += 1
                elif c.isupper():
                    mayusculas += 1
        
        return minusculas, mayusculas

    raise TypeError('El argumento `texto` debe ser una cadena de caracteres.')


frase = 'Python es tremendo'
try:
    resultado = contador_minusculas_mayusculas(frase)
    print('Cantidad minúsculas:', resultado[0])
    print('Cantidad mayúsculas:', resultado[1])
except TypeError as e:
    print('ERROR:', e)
