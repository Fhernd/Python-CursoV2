import os

def main():
    # Operaciones adicionales sobre archivos:
    print('Operaciones adicionales sobre archivos:')

    print()

    print('Renombrar un archivo')
    nombre_archivo = 'parte14/archivo.txt'
    
    if os.path.isfile(nombre_archivo):
        print(f'El archivo {nombre_archivo} existe en disco.')
    else:
        print(f'El archivo {nombre_archivo} no existe en disco.')
    
    print()

    print('Cambiar el nombre de un archivo:')

    nuevo_nombre_archivo = 'parte14/archivo2.txt'

    os.rename(nombre_archivo, nuevo_nombre_archivo)

    if os.path.isfile(nombre_archivo):
        print(f'El archivo {nombre_archivo} existe en disco.')
    else:
        print(f'El archivo {nombre_archivo} no existe en disco.')

    print()

    print('Eliminar un archivo')

    os.remove(nuevo_nombre_archivo)

    print()

def crear_carpetas():
    nombre_carpeta = 'parte14/código'

    if os.path.isdir(nombre_carpeta):
        print(f'La carpeta {nombre_carpeta} existe en disco.')
    else:
        print(f'La carpeta {nombre_carpeta} no existe en disco.')
    
    print()

    print('Creación de una carpeta/directorio:')

    os.mkdir(nombre_carpeta)

    if os.path.isdir(nombre_carpeta):
        print(f'La carpeta {nombre_carpeta} existe en disco.')
    else:
        print(f'La carpeta {nombre_carpeta} no existe en disco.')

if __name__ == "__main__":
    # main()
    crear_carpetas()
    
    print('Fin del programa.')
