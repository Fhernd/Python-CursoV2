# Ejercicio 8.9. Comprobar si un número es capicúa.

# 1001
# 999
# 808
# 807
# 103

numero = int(input('Digite un número entero positivo: '))

if numero >= 0:
    
    if str(numero) == str(numero)[::-1]:
        print('%i es capicúa.' % numero)
    else:
        print('%i no es capicúa.' % numero)

else:
    print('El número debe ser positivo.')
