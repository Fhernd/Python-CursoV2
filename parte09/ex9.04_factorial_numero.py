# Ejercicio 9.4: Calcular el factorial de un número dado por el usuario.

# Solución:

# 0! = 1
# 1! = 1

# 5! = 1 * 2 * 3 * 4 * 5 = 120
# 6! = 720

numero = int(input('Digite un número entero positivo: '))

if numero >= 0:
    factorial = 1

    if numero == 0 or numero == 1:
        factorial = 1
    else:
        for i in range(1, numero + 1):
            factorial *= i
    
    print(f'{numero}! = {factorial}')
else:
    print('MENSAJE: Ha escrito un valor negativo. La función factorial no está definida para los números negativos.')
