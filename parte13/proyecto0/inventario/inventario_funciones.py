from datetime import datetime

def registrar_producto(productos, producto):
    """
    Registrar un nuevo producto en el inventario.

    Parameters:
    productos: lista de productos en el inventario
    producto: producto a agregar al inventario
    """
    productos.append(producto)

def realizar_venta(ventas, venta):
    """
    Crea una nueva venta

    Parameters:
    ventas: lista de las ventas realizadas hasta el momento.
    venta: venta recién realizada
    """
    venta['fecha'] = datetime.now()
    ventas.append(venta)

def buscar_producto(productos, id_producto):
    """
    Busca un producto a partir de su ID.

    Parameters:
    productos: lista de productos en el inventario
    id_producto: ID del producto a buscar

    Returns:
    El producto encontrado, si no se encuentra None.
    """
    for p in productos:
        if p['id_producto'] == id_producto:
            return p
    
    return None

def cambiar_estado_producto(producto):
    """
    Cambia el estado de un producto.

    Parameters:
    producto: Producto sobre el que se cambiará su estado.
    """
    producto['disponible'] = not producto['disponible']