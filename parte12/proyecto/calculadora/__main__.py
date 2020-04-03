from .funciones_aritmeticas import sumar, restar, multiplicar, dividir

def menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Salir")


def main():
    while True:
        while True:
            menu()
            try:
                opcion = int(input('Escriba la operación a ejecutar: '))
                break
            except ValueError as e:
                print('ERROR: Ha digitado un valor inválido')
        print()

        if opcion == 0:
            break
        if 1 <= opcion <= 4:
            while True:
                try:
                    numero_1 = int(input('Escriba el número 1: '))
                    break
                except ValueError as e:
                    print('ERROR: Ha digitado un valor inválido')
            while True:
                try:
                    numero_2 = int(input('Escriba el número 2: '))
                    break
                except ValueError as e:
                    print('ERROR: Ha digitado un valor inválido')
        if opcion == 1:
            resultado = sumar(numero_1, numero_2)
            print(f'{numero_1} + {numero_2} = {resultado}.')
        elif opcion == 2:
            resultado = restar(numero_1, numero_2)
            print(f'{numero_1} - {numero_2} = {resultado}.')
        elif opcion == 3:
            resultado = multiplicar(numero_1, numero_2)
            print(f'{numero_1} * {numero_2} = {resultado}.')
        elif opcion == 4:
            try:
                resultado = dividir(numero_1, numero_2)
                print(f'{numero_1} / {numero_2} = {resultado}.')
            except ZeroDivisionError as e:
                print(e)
        print()
    
    print()

    print('El programa ha terminado.')


if __name__ == '__main__':
    main()
