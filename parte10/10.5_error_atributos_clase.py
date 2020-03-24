# Error al intentar acceder a un atributo inexistente en una clase:

class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio


computador = Producto(1001, 'Computador', 799)

print('Código:', computador.codigo)
print('Nombre:', computador.nombre)
print('Precio:', computador.precio)

try:
    print('Cantidad:', computador.cantidad)
except AttributeError as e:
    print('Se está tratando de acceder a una propiedad/atributo inexistente')
    print('ERROR:', e)
