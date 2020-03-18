# Realizar aumento sobre los ahorros dependiendo de la cantidad ahorrada:

ahorro = float(input('Escriba la cantidad actual de dinero que tiene en ahorros:'))

if ahorro > 0:
    if ahorro < 1000000:
        ahorro *= 1.10
    elif ahorro < 3000000:
        ahorro *= 1.07
    elif ahorro < 10000000:
        ahorro *= 1.05
    else:
        ahorro *= 1.03
    
    print('El ahorro se ha incremando a {}'.format(ahorro))
else:
    print('Ud. ha digitado una cantidad negativa o igual a cero.')

print()

print('El programa ha finalizado.')
