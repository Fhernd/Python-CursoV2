nombre = 'Edward'
apellido = "Ortiz"
nombre_completo = nombre + ' ' + apellido

print('Nombre:', nombre)
print('Apellido:', apellido)
print('Nombre completo:', nombre_completo)

print()

print('Tipo de dato de la variable nombre:', type(nombre))
print('Tipo de dato de la variable apellido:', type(apellido))
print('Tipo de dato de la variable nombre_completo:', type(nombre_completo))

print()

edad = 29

resultado = nombre_completo + ' tiene ' + str(edad) + ' años.'
print(resultado)

print()

resultado = '{} tiene {} años.'.format(nombre_completo, edad)
print(resultado)
