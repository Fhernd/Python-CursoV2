from funciones_aritmeticas import sumar, restar, multiplicar, dividir

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
            except TypeError as e:
                print('ERROR: Ha digitado un valor inválido')

        if 1 <= opcion <= 4:
            while True:
                try:
                    numero_1 = int(input('Escriba el número 1: '))
                    break
                except TypeError as e:
                    print('ERROR: Ha digitado un valor inválido')
            while True:
                try:
                    numero_2 = int(input('Escriba el número 2: '))
                    break
                except TypeError as e:
                    print('ERROR: Ha digitado un valor inválido')
        if opcion == 1:
            resultado = sumar(numero_1, numero_2)
        elif opcion == 2:
            resultado = restar(numero_1, numero_2)
        
        
