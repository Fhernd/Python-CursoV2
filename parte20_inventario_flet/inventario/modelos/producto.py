class Producto:
    """
    Representa un producto del inventario.
    """
    def __init__(self, codigo, nombre, precio, cantidad, disponible):
        """
        Constructor de la clase.

        Parameters:
        codigo: Código del producto.
        nombre: Nombre del producto.
        precio: Precio del producto.
        cantidad: Cantidad del producto.
        disponible: ¿Está disponible el producto?
        """
        
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.disponible = disponible
    
    def __str__(self):
        """
        Representación en cadena de texto del producto.

        Returns:
        Representación en cadena de texto del producto.
        """
        return f'ID: {self.codigo}\nNombre: {self.nombre}\nPrecio: {self.precio}\nCantidad: {self.cantidad}\n¿Disponible?: {"Sí" if self.disponible else "No"}'
