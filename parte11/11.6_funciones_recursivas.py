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

print()

# Función Fibonacci:
print('Función Fibonacci:')

# 0 1 1 2 3 5 8 13 21 34 55 89...

def fibonacci_iterativo(n):
    """
    Calcula el n-ésimo valor de la serie Fibonacci. (Enfoque iterativo.)

    Parameters:
    n: n-ésimo valor de la serie Fibonacci a calcular.

    Returns:
    Valor de la serie Fibonacci.
    """
    a = 0
    b = 1

    for i in range(n - 1):
        a, b = b, a + b
    
    return b

def fibonacci_recursivo(n):
    """
    Calcula el n-ésimo valor de la serie Fibonacci. (Enfoque recursivo.)

    Parameters:
    n: n-ésimo valor de la serie Fibonacci a calcular.

    Returns:
    Valor de la serie Fibonacci.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 2) + fibonacci_recursivo(n - 1)

resultado = fibonacci_iterativo(10)
print('Fibonacci (iterativo):', resultado)

resultado = fibonacci_recursivo(10)
print('Fibonacci (recursivo):', resultado)
