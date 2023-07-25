from datetime import datetime

class Venta:
    """
    Representa una venta realizada.
    """
    def __init__(self, codigo_producto, cantidad, total_sin_iva, fecha=datetime.now()):
        """
        Constructor de la clase.

        Parameters:
        codigo_producto: Código del producto.
        fecha: Fecha de la venta.
        cantidad: Cantidad del producto.
        total_sin_iva: Total sin IVA de la venta.
        """
        self.codigo_producto = codigo_producto
        self.fecha = fecha
        self.cantidad = cantidad
        self.total_sin_iva = total_sin_iva
