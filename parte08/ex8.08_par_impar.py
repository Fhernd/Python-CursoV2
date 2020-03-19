# Ejercicio 8.8. Determinar si un número dado por el usuario es par o impar.

numero = int(input('Escriba un número entero cualquiera: '))

if numero % 2 == 0:
    print('%i es un número par.' % numero)
else:
    print('%i es un número impar.' % numero)
