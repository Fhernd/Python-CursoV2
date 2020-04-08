import json

def main():
    # Creación de un archivo binario:
    print('Creación de un archivo binario:')

    nombre_archivo = 'parte14/numeros.bin'

    archivo = open(nombre_archivo, 'wb')

    numeros = [2, 3, 5, 7, 11]

    archivo.write(bytearray(numeros))

    archivo.close()

    print('El programa ha terminado.')

if __name__ == "__main__":
    main()
