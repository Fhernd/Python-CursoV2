# Ejercicio 8.3. Comprobar el producto de mayor precio entre tres productos.

precio_1 = float(input('Escriba el precio del primer producto: '))
precio_2 = float(input('Escriba el precio del segundo producto: '))
precio_3 = float(input('Escriba el precio del tercer producto: '))

# 100, 200, 300
# 1000, 1000, 1000
# 100, 200, 100

if precio_1 > precio_2 and precio_1 > precio_3:
    print('El producto más costoso es %f' % precio_1)
elif precio_2 > precio_1 and precio_2 > precio_3:
    print('El producto más costoso es %f' % precio_2)
elif precio_3 > precio_1 and precio_3 > precio_2:
    print('El producto más costoso es %f' % precio_3)
else:
    print('Los tres productos cuestan lo mismo.')
