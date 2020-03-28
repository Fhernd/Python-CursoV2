# Pasar argumentos por valor y por referencia:
print('Pasar argumentos por valor y por referencia:')

# 1. Pasar argumentos por valor:
print('1. Pasar argumentos por valor:')

def duplicar(numero):
    numero *= 2 # numero = numero * 2
    print('El número duplicado es igual a:', numero)

x = 2
print('El valor de la variable `x` antes de su duplicación:', x)

duplicar(x)

print('El valor de la variable `x` después de su duplicación:', x)
