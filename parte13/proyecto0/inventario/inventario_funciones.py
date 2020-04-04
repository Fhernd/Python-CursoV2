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
