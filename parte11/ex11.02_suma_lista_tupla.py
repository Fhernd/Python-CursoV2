# Ejercicio 11.2: Crear una función para sumar todos los números en una lista o tupla.

def sumar(valores):
    """
    Suma el conjunto o grupo de valores de una lista o tupla:

    Parameters:
    valores: Lista o tupla con los valores a sumar.

    Returns:
    Suma de los valores en la lista o tupla.
    """
    if isinstance(valores, (list, tuple)):
        acumulador = 0

        for v in valores:
            acumulador += v
        
        return acumulador
    else:
        raise ValueError('Ha pasado un argumento que ni es lista ni tupla.')

edades = [19, 29, 31, 21]
try:
    resultado = sumar(edades)
    print('El resultado de sumar las edades {} es igual a {}.'.format(edades, resultado))
except ValueError as e:
    print('ERROR:', e)

print()

precios = (999.9, 59.9, 27.5)

try:
    resultado = sumar(precios)
    print('El resultado de sumar los precios {} es igual a {}.'.format(precios, resultado))
except ValueError as e:
    print('ERROR:', e)

print()

numeros = 1000

try:
    resultado = sumar(numeros)
    print('El resultado de sumar los numeros {} es igual a {}.'.format(numeros, resultado))
except ValueError as e:
    print('ERROR:', e)
