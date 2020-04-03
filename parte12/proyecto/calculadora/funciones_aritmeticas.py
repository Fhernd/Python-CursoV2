def sumar(a, b):
    """
    Suma dos números.

    Parameters:
    a: Primer número a sumar.
    b: Segundo número a sumar.

    Returns:
    Suma de los dos números.
    """
    return a + b

def restar(a, b):
    """
    Resta dos números.

    Parameters:
    a: Primer número a restar.
    b: Segundo número a restar.

    Returns:
    Resta de los dos números.
    """
    return a - b

def multiplicar(a, b):
    """
    Multiplica dos números.

    Parameters:
    a: Primer número a multiplicar.
    b: Segundo número a multiplicar.

    Returns:
    Multiplica de los dos números.
    """
    return a * b

def dividir(a, b):
    """
    Divide dos números.

    Parameters:
    a: Primer número a dividir (dividendo).
    b: Segundo número a dividir (divisor).

    Returns:
    Divide de los dos números.
    """
    if b != 0:
        return a / b
    
    raise ZeroDivisionError('Está intentando dividir entre cero.')
