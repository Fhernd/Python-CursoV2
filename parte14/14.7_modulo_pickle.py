import pickle

def main():
    # Uso del módulo `pickle` para serializar y des-serializar objetos Python:
    print('Uso del módulo `pickle` para serializar y des-serializar objetos Python:')

    paises_capitales = {'Colombia': 'Bogotá', 'Ecuador': 'Quito', 'Argentina': 'Buenos'}

    nombre_archivo = 'parte14/paises_capitales.pickle'

    with open(nombre_archivo, 'wb') as f:
        pickle.dump(paises_capitales, f)
    
    print()

    print('Lectura del contenido de un archivo pickle:')

    with open(nombre_archivo, 'rb') as f:
        paises_capitales_recuperados = pickle.load(f)

        print('Tipo de dato de la variable `paises_capitales_recuperados`:', type(paises_capitales_recuperados))
        print('El contenido de la variable `paises_capitales_recuperados`:')
        print(paises_capitales_recuperados)

    print()
    
    print('El programa ha terminado.')

if __name__ == "__main__":
    main()
