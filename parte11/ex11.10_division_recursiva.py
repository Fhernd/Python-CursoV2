# Ejercicio 11.10: Crear una función recursiva para dividir dos números.

def dividir(dividendo, divisor):
    """
    Calcula la división de dos números.

    Parameters:
    dividendo: Dividendo de la división.
    divisor: Divisor de la división.

    Returns:
    División entre dividendo y divisor.
    """
    if divisor == 0:
        raise ZeroDivisionError('El divisor no puede ser cero (0).')
    elif dividendo == divisor:
        return 1
    elif dividendo < divisor:
        return 0
    else:
        return 1 + dividir(dividendo - divisor, divisor)


print('{}/{} = {}'.format(5, 2, dividir(5, 2)))
print('{}/{} = {}'.format(1, 2, dividir(1, 2)))

try:
    print('{}/{} = {}'.format(1, 0, dividir(1, 0)))
except ZeroDivisionError as e:
    print('ERROR:', e)
