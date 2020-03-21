# Ejercicio 9.2: Capturar una palabra o frase del usuario e invertirla.

frase = input('Escriba una frase o palabra: ')

print('La frase original es:', frase)

# Python => nohtyP

# Solución 1:

frase_invertada = ''

for i in range(len(frase) - 1, -1, -1):
    frase_invertada += frase[i]

print('Frase invertida:', frase_invertada)

print()

frase_invertada = frase[::-1]
print('Frase invertida:', frase_invertada)
