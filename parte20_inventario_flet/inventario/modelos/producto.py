class Producto:
    def __init__(self, codigo, nombre, precio, cantidad, disponible):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.disponible = disponible
    
    def __str__(self):
        return f'ID: {self.codigo}\nNombre: {self.nombre}\nPrecio: {self.precio}\nCantidad: {self.cantidad}\n¿Disponible?: {"Sí" if self.disponible else "No"}'
