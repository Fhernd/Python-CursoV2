from datetime import datetime

class Venta:
    def __init__(self, codigo_producto, cantidad, total_sin_iva):
        self.codigo_producto = codigo_producto
        self.fecha = datetime.now()
        self.cantidad = cantidad
        self.total_sin_iva = total_sin_iva
