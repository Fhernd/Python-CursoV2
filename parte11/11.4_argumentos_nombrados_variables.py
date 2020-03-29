# Parámetros/argumentos nombrados variables - keywords:
print('Parámetros/argumentos nombrados variables - keywords:')

def mostrar_identidad(**identificacion):
    resultado = ''

    if identificacion.get('documento'):
        resultado += 'Documento: ' + identificacion.get('documento') + '\n'
    if identificacion.get('nombre'):
        resultado += 'Nombre: ' + identificacion.get('nombre') + '\n'
    if identificacion.get('apellido'):
        resultado += 'Apellido: ' + identificacion.get('apellido') + '\n'
    
    return resultado

persona = mostrar_identidad(nombre='John', apellido='Ortiz')
print('Identificación:', persona)

print()

persona = mostrar_identidad(nombre='John', apellido='Ortiz', documento='123456789')
print('Identificación:', persona)
