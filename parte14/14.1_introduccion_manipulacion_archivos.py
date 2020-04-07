# Introducción a la Manipulación de Archivos de Texto
print('Introducción a la Manipulación de Archivos de Texto')

print()

# Apertura de un archivo de texto:
print('Apertura de un archivo de texto:')

nombre_archivo = 'parte14/lenguajes.txt'

archivo = open(nombre_archivo, 'r')

for l in archivo.readlines():
    print(l, end='')
