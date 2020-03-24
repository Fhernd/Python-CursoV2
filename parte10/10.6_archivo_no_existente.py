# Error al intentar abrir/acceder un archivo del sistema de almacenamiento:
print('Error al intentar abrir/acceder un archivo del sistema de almacenamiento:')

nombre_archivo = 'python.txt'

try:
    with open(nombre_archivo, 'r') as f:
        for l in f.readlines():
            print(l)
except FileNotFoundError as e:
    print('ERROR:', e)
