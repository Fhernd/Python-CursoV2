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

    os.rename(nombre_archivo, 'parte14/archivo2.txt')

    if os.path.isfile(nombre_archivo):
        print(f'El archivo {nombre_archivo} existe en disco.')
    else:
        print(f'El archivo {nombre_archivo} no existe en disco.')

if __name__ == "__main__":
    main()
    
    print('Fin del programa.')
