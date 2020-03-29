# Funciones recursivas:
print('Funciones recursivas:')

# n!
# 5! = 1 * 2 * 3 * 4 * 5 = 120

def factorial_iterativo(n):
    """
    Calcula el factorial de un número. (Enfoque iterativo.)

    Parameters:
    n: Número de factorial a calcular.

    Returns:
    Factorial
    """
    resultado = 1

    for i in range(1, n + 1):
        resultado *= i
    
    return resultado

def factorial_recursivo(n):
    """
    Calcula el factorial de un número. (Enfoque recursivo.)

    Parameters:
    n: Número de factorial a calcular.

    Returns:
    Factorial
    """
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)


resultado = factorial_iterativo(5)
print('Factorial (iterativo):', resultado)

resultado = factorial_recursivo(5)
print('Factorial (recursivo):', resultado)

