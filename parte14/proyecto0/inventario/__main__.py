from .inventario_funciones import registrar_producto, realizar_venta, buscar_producto, cambiar_estado_producto, ventas_rango_fecha, top_5_mas_vendidos, top_5_menos_vendidos, mostrar_datos_producto, mostrar_datos_venta, mostrar_datos_venta_producto
import datetime

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
        print(f"{p['id_producto']} - {p['nombre']}")

def continuar():
    """
    Muestra mensaje de continuación en la consola.
    """
    print()
    print('Presione Enter para continuar...', end='')
    input()
    print()

def main():
    """
    Punto de entrada a la aplicación.
    """
    productos = []
    ventas = []

    while True:
        while True:
            try:
                mostrar_menu()
                opcion = int(input('Digite la opción: '))
                if 0 <= opcion <= 7:
                    break
                else:
                    print('MENSAJE: Debe digitar un número mayor o igual a 0 y menor o igual a 7.')
            except ValueError:
                print()
                print('ERROR: Debe digitar un número entero válido.')
            
            continuar()
        
        print()

        if opcion == 0:
            break
        elif opcion == 1:
            while True:
                id_producto = capturar_entero('Digite el ID del nuevo producto')

                if id_producto > 0:
                    producto = buscar_producto(productos, id_producto)

                    if producto is None:
                        break
                    else:
                        print()
                        print('MENSAJE: Ya existe un producto con el ID digitado.')
                else:
                    print()
                    print('MENSAJE: El ID del producto debe ser un número positivo.')
                
                continuar()
            
            nombre_producto = capturar_cadena('Digite el nombre del nuevo producto')

            while True:
                precio_producto = capturar_real('Digite el precio del nuevo producto')

                if precio_producto > 0:
                    break
                else:
                    print()
                    print('MENSAJE: Debe digitar un precio positivo para el producto.')
                
                continuar()
            
            while True:
                cantidad_producto = capturar_entero('Digite la cantidad del nuevo producto')

                if cantidad_producto > 0:
                    break
                else:
                    print()
                    print('MENSAJE: Debe digitar una cantidad positiva para el producto.')
                
                continuar()
            
            while True:
                print('1. Disponible')
                print('2. No Disponible')
                disponible = capturar_entero('Digite la opción para la disponibilidad del producto')

                if disponible == 1 or disponible == 2:
                    disponible = disponible == 1
                    break
                else:
                    print()
                    print('MENSAJE: La opción {} de disponibilidad no existe.'.format(disponible))
                
                continuar()
            
            nuevo_producto = {'id_producto': id_producto, 'nombre': nombre_producto, 'precio': precio_producto, 'cantidad': cantidad_producto, 'disponible': disponible}

            registrar_producto(productos, nuevo_producto)

            print()
            print('MENSAJE: El producto se ha creado de forma satisfactoria.')
        if opcion == 2:
            if len(productos):
                while True:
                    listar_productos(productos)
                    id_producto = capturar_entero('Digite el ID del producto')

                    producto = buscar_producto(productos, id_producto)

                    if producto:
                        break
                    else:
                        print()
                        print('MENSAJE: Debe escribir un ID de producto existente.')
                
                while True:
                    cantidad_producto = capturar_entero('Digite la cantidad del producto')

                    if cantidad_producto > 0:
                        if cantidad_producto <= producto['cantidad']:
                            break
                        else:
                            print()
                            print('MENSAJE: No existe cantidad suficiente para la venta. Sólo hay {} unidades.'.format(producto['cantidad']))
                    else:
                        print()
                        print('MENSAJE: Debe digitar una cantidad positiva para el producto.')

                    continuar()
                
                nueva_venta = {'id_producto': id_producto, 'cantidad': cantidad_producto, 'total_sin_iva': producto['precio'] * cantidad_producto}

                realizar_venta(ventas, nueva_venta)

                print('Total: $%.2f' % (nueva_venta['total_sin_iva'] * 1.19))

                print()
                print('MENSAJE: La venta se ha realizado de forma satisfactoria.')
            else:
                print()
                print('MENSAJE: Aún no ha registrado productos.')
        elif opcion == 3:
            if len(productos):
                while True:
                    listar_productos(productos)
                    id_producto = capturar_entero('Digite el ID del producto')

                    producto = buscar_producto(productos, id_producto)

                    if producto:
                        break
                    else:
                        print()
                        print('MENSAJE: Debe escribir un ID de producto existente.')
                    
                    continuar()
                
                print()
                mostrar_datos_producto(producto)
            else:
                print()
                print('MENSAJE: Aún no ha registrado productos.')
        elif opcion == 4:
            if len(productos):
                while True:
                    listar_productos(productos)
                    id_producto = capturar_entero('Digite el ID del producto')

                    producto = buscar_producto(productos, id_producto)

                    if producto:
                        break
                    else:
                        print()
                        print('MENSAJE: Debe escribir un ID de producto existente.')
                    
                    continuar()
                
                cambiar_estado_producto(producto)
                mostrar_datos_producto(producto)
            else:
                print()
                print('MENSAJE: Aún no ha registrado productos.')
        elif opcion == 5:
            if len(productos):
                if len(ventas):
                    while True:
                        try:
                            fecha_inicio = capturar_cadena('Digite la fecha de inicio (AAAA-MM-DD)')

                            fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
                            break
                        except ValueError:
                            print()
                            print('ERROR: Debe digitar una fecha válida con el formato AAAA-MM-DD.')
                        
                        print()

                    while True:
                        try:
                            fecha_final = capturar_cadena('Digite la fecha final (AAAA-MM-DD)')

                            fecha_final = datetime.datetime.strptime(fecha_final, '%Y-%m-%d')
                            break
                        except ValueError:
                            print()
                            print('ERROR: Debe digitar una fecha válida con el formato AAAA-MM-DD.')
                        
                        print()
                    
                    ventas_rango = ventas_rango_fecha(ventas, fecha_inicio, fecha_final)

                    if len(ventas_rango):
                        for v in ventas_rango:
                            mostrar_datos_venta(productos, v)
                            print()
                    else:
                        print()
                        print('MENSAJE: No hay ventas para el rango seleccionado.')
                else:
                    print()
                    print('MENSAJE: Aún no ha efectuado ninguna venta.')
            else:
                print()
                print('MENSAJE: Aún no ha registrado productos.')
        elif opcion == 6:
            if len(productos):
                if len(ventas):
                    productos_vendidos = top_5_mas_vendidos(ventas)

                    print('Top 5 de los productos más vendidos')
                    for p in productos_vendidos:
                        mostrar_datos_venta_producto(productos, p)
                        print()
                else:
                    print()
                    print('MENSAJE: Aún no ha efectuado ninguna venta.')
            else:
                print()
                print('MENSAJE: Aún no ha registrado productos.')
        elif opcion == 7:
            if len(productos):
                if len(ventas):
                    productos_vendidos = top_5_menos_vendidos(ventas)

                    print('Top 5 de los productos menos vendidos')
                    for p in productos_vendidos:
                        mostrar_datos_venta_producto(productos, p)
                        print()
                else:
                    print()
                    print('MENSAJE: Aún no ha efectuado ninguna venta.')
            else:
                print()
                print('MENSAJE: Aún no ha registrado productos.')
        
        continuar()
    print()
    print('El programa ha finalizado.')

if __name__ == '__main__':
    main()
