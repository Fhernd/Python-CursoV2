# Ejercicio 9.5: Construir un patrón con asteriscos que represente la letra A.

#   ***                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *****                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *

for i in range(7):
    if i == 0:
        for j in range(5):
            if j != 0 and j != 4:
                print('*', end='')
            else:
                print(' ', end='')
    if i == 1 or i == 2 or 4 <= i <= 6:
        for j in range(5):
            if j == 0 or j == 4:
                print('*', end='')
            else:
                print(' ', end='')
    if i == 3:
        for j in range(5):
            print('*', end='')
    print()
