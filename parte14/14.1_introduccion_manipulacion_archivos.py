def main():
    # Introducción a la Manipulación de Archivos de Texto
    print('Introducción a la Manipulación de Archivos de Texto')

    print()

    # Apertura de un archivo de texto:
    print('Apertura de un archivo de texto:')

    nombre_archivo = 'parte14/lenguajes.txt'

    archivo = open(nombre_archivo, 'r')

    for l in archivo.readlines():
        print(l, end='')
    
    archivo.close()

    print()

    # Apertura de un archivo con un manejador de contexto:
    print('Apertura de un archivo con un manejador de contexto:')

    nombre_archivo = 'parte14/lenguajes.txt'

    with open(nombre_archivo, 'r') as f:
        for l in f.readlines():
            print(l, end='')


if __name__ == "__main__":
    main()
