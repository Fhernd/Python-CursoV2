# Tipo de dato compuesto string

nombre = 'Edward Ortiz'
email = "edward@mail.co"
direccion = '''Carrera 1 # 13A-29
Bogotá - Colombia
GMT-05
'''

print(type(nombre))
print(nombre)

print()

mensaje = 'Bienvenido(a), ' + nombre + '. Correo: ' + email
print(type(mensaje))
print(mensaje)

print()
# Interpolación:
mensaje = f'Bienvenido(a), {nombre}. Correo: {email}'
print(mensaje)

# format() de la clase str:
mensaje = 'Bienvenido(a), {}. Correo: {}'.format(nombre, email)
print(mensaje)

# Formato con %:
mensaje = 'Bienvenido(a), %s. Correo: %s' % (nombre, email)
print(mensaje)

print()

# Inmutabilidad de cadenas de caracteres (str):
lenguaje = "Python"
print(lenguaje)
print(lenguaje[0])
print(lenguaje[1])
print(lenguaje[2])
print(lenguaje[3])
print(lenguaje[4])
print(lenguaje[5])

print()

# lenguaje[0] = 'p' # TypeError

lenguaje = 'p' + lenguaje[1:]
print(lenguaje)

# Inmutables... se dicen que son estáticos

print(id('python') == id('python'))

lenguaje = 'Python'.lower()
print(lenguaje)

print()

# Uso del método str.split()
valores = '2,3,5,7,11'
numeros = valores.split(',')
print(len(numeros))
print(numeros)
print(type(numeros[0]))

print()

# Uso del método str.find()
indice = valores.find('2')
print('El índice del elemento "2" es igual a', indice)
indice = valores.find('1')
print('El índice del elemento "1" es igual a', indice)
indice = valores.find('8')
print('El índice del elemento "8" es igual a', indice)

print()

# Creación de una función (proceso) personalizado para buscar una cadena dentro de otra:

def encontrar(cadena, caracter):
    indice = -1
    for i in range(0, len(cadena)):
        if caracter == cadena[i]:
            indice = i
            break
    
    return indice

indice = encontrar(valores, '2')
print('El índice del elemento "2" es igual a', indice)
indice = encontrar(valores, '8')
print('El índice del elemento "8" es igual a', indice)
