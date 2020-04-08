import pickle

def main():
    # Uso del módulo `pickle` para serializar y des-serializar objetos Python:
    print('Uso del módulo `pickle` para serializar y des-serializar objetos Python:')

    paises_capitales = {'Colombia': 'Bogotá', 'Ecuador': 'Quito', 'Argentina': 'Buenos'}

    nombre_archivo = 'parte14/paises_capitales.pickle'

    with open(nombre_archivo, 'wb') as f:
        pickle.dump(paises_capitales, f)
    
    print()

    print('El programa ha terminado.')

if __name__ == "__main__":
    main()
