# Ejercicio 9.1: Construir un patrón con el carácter asterisco.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

for i in range(9):
    if i <= 4:
        for j in range(i + 1):
            print('*', end=' ')
    else:
        for j in range(9 - i):
            print('*', end=' ')
    print()
