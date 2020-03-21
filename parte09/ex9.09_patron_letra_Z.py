#  Ejercicio 9.9: Construir un patrón con asteriscos que represente la letra Z.

#  *******                                                                 
#      *                                                                  
#     *                                                                   
#    *                                                                    
#   *                                                                     
#  *                                                                      
# *******

for i in range(7):
    if i == 0:
        print(' ' + '*' * 7)
    elif i == 1:
        print(' ' * 5 + '*')
    elif i == 2:
        print(' ' * 4 + '*')
    elif i == 3:
        print(' ' * 3 + '*')
    elif i == 4:
        print(' ' * 2 + '*')
    elif i == 5:
        print(' ' + '*')
    else:
        print('*' * 7)
