def main():
    nombre_archivo = 'parte14/numeros.bin'

    print('Se está creando un archivo binario...')
    with open(nombre_archivo, 'wb') as f:

        numeros = [2, 3, 5, 7, 11]
        f.write(bytearray(numeros))

    print()

    print('Este es el contenido del archivo binario `numeros.bin`:')

    with open(nombre_archivo, 'rb') as f:

        numeros = list(f.read())
        
        print()

        print(numeros)

    print()
    
    print('El programa ha terminado.')

if __name__ == "__main__":
    main()
