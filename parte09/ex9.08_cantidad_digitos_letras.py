# Ejercicio 9.8: Contar la cantidad de dígitos y letras que tiene un texto.

# Solución:

cantidad_letras = 0
cantidad_digitos = 0

frase = input('Escriba una frase: ')

for c in frase:
    if c.isnumeric():
        cantidad_digitos += 1
    elif c.isalpha():
        cantidad_letras += 1

print('Cantidad de dígitos en la frase:', cantidad_digitos)
print('Cantidad de letras en la frase:', cantidad_letras)
