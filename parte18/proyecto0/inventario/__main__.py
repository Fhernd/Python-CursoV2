import tkinter as tk

from .modelos.inventario import Inventario
from .modelos.producto import Producto
from .modelos.venta import Venta


def mostrar_menu():
    """
    Muestra el menú de las operaciones disponibles.
    """
    print('1. Registrar nuevo producto')
    print('2. Vender un producto')
    print('3. Buscar un producto por su código')
    print('4. Cambiar disponibilidad de un producto')
    print('5. Productos vendidos en un rango de fechas')
    print('6. Ver top 5 de los productos más vendidos')
    print('7. Ver top 5 de los productos menos vendidos')
    print('0. Salir')

def capturar_entero(mensaje):
    """
    Captura un número entero. Valida el ingreso de datos.

    Parameters:
    mensaje: Mensaje o texto personalizado a mostrar para la captura de un número.

    Returns:
    Número entero resultado de la captura.
    """
    while True:
        try:
            numero = int(input(f'{mensaje}: '))

            return numero
        except ValueError:
            print('ERROR: Debe digitar un número entero.')
        
        print()

def capturar_real(mensaje):
    """
    Captura un número real. Valida el ingreso de datos.

    Parameters:
    mensaje: Mensaje o texto personalizado a mostrar para la captura de un número.

    Returns:
    Número real resultado de la captura.
    """
    while True:
        try:
            numero = float(input(f'{mensaje}: '))

            return numero
        except ValueError:
            print('ERROR: Debe digitar un número real.')
        
        print()

def capturar_cadena(mensaje):
    """
    Captura una cadena de caracteres. Valida el ingreso de datos.

    Parameters:
    mensaje: Mensaje o texto personalizado a mostrar para la captura de una cadena de caracteres.

    Returns:
    Cadena de caracteres.
    """
    while True:
        cadena = input(f'{mensaje}: ').strip()

        if len(cadena):
            return cadena
        else:
            print('MENSAJE: Debe digitar una cadena de caracteres con texto.')
        
        print()

def listar_productos(productos):
    """
    Muestra un listado de productos.

    Parameters:
    productos: Lista de productos.
    """
    for p in productos:
        print(f"{p.codigo} - {p.nombre}")

def continuar():
    """
    Muestra mensaje de continuación en la consola.
    """
    print()
    print('Presione Enter para continuar...', end='')
    input()
    print()

def cargar_inventario():
    while True:
        print('¿Desea cargar los datos del inventario y las ventas desde el archivo `inventario.pickle`?:')
        print('1. Sí')
        print('2. No')
        opcion = capturar_entero('Digite la opción')

        if opcion == 1 or opcion == 2:
            break
    
    if opcion == 1:
        with open('inventario/inventario.pickle', 'rb') as f:
            inventario = pickle.load(f)
            return inventario
    
    return None

def guardar_datos(inventario):
    while True:
        print('¿Desea guardar los datos de productos y ventas en el archivo `inventario.pickle`?:')
        print('1. Sí')
        print('2. No')
        opcion = capturar_entero('Digite la opción')

        if opcion == 1 or opcion == 2:
            break
    
    if opcion == 1:
        with open('inventario/inventario.pickle', 'wb') as f:

            pickle.dump(inventario, f)

        return True
    else:
        return False


import tkinter as tk

class MDIParent(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana MDI")
        self.menu_bar = tk.Menu(self)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Salir", command=self.quit)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        self.product_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.product_menu.add_command(label="Registrar")
        self.product_menu.add_command(label="Vender")
        self.product_menu.add_command(label="Buscar")
        self.product_menu.add_command(label="Cambiar disponibilidad")
        self.menu_bar.add_cascade(label="Productos", menu=self.product_menu)
        self.report_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.report_menu.add_command(label="Ventas en un rango de fechas")
        self.report_menu.add_command(label="Top 5 de productos más vendidos")
        self.report_menu.add_command(label="Top 5 de productos menos vendidos")
        self.menu_bar.add_cascade(label="Reportes", menu=self.report_menu)
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Acerca de")
        self.menu_bar.add_cascade(label="Ayuda", menu=self.help_menu)
        self.config(menu=self.menu_bar)
        
if __name__ == "__main__":
    app = MDIParent()
    app.mainloop()



def main():
    """
    Punto de entrada a la aplicación.
    """
    


if __name__ == '__main__':
    main()
