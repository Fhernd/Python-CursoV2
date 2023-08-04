from datetime import datetime
from collections import Counter

from .venta import Venta

from .producto import Producto

class Inventario:
    """
    Clase que contiene las funciones del inventario.
    """

    def __init__(self):
        """
        Constructor de la clase.
        """
        pass

    def recibir_conexion_bd(self, conexion):
        """
        Recibe la conexión con la base de datos.

        Parameters:
        conexion: Conexión con la base de datos.
        """
        self.conexion = conexion
    
    def registrar_producto(self, producto):
        """
        Registrar un nuevo producto en el inventario.

        Parameters:
        producto: producto a agregar al inventario
        """
        sql = """
            INSERT INTO producto (codigo, nombre, precio, cantidad, disponible) 
            VALUES (?, ?, ?, ?, ?)
        """

        cursor = self.conexion.cursor()

        cursor.execute(sql, (producto.codigo, producto.nombre, producto.precio, producto.cantidad, producto.disponible))

        self.conexion.commit()

        cursor.close()

    def realizar_venta(self, venta):
        """
        Crea una nueva venta

        Parameters:
        venta: venta recién realizada
        """
        venta.fecha = venta.fecha.strftime('%Y-%m-%d %H:%M:%S')
        
        sql = """
            INSERT INTO venta (codigo_producto, fecha, cantidad, total_sin_iva) 
            VALUES (?, ?, ?, ?)
        """

        cursor = self.conexion.cursor()

        cursor.execute(sql, (venta.codigo_producto, venta.fecha, venta.cantidad, venta.total_sin_iva))

        self.conexion.commit()

        cursor.close()

    def buscar_producto_por_codigo(self, codigo):
        """
        Busca un producto a partir de su ID.

        Parameters:
        codigo: Código del producto a buscar.

        Returns:
        El producto encontrado, si no se encuentra None.
        """
        sql = """
            SELECT * FROM producto WHERE codigo = ?
        """

        cursor = self.conexion.cursor()

        cursor.execute(sql, (codigo,))

        producto = cursor.fetchone()

        if producto is not None:
            return Producto(**producto)
        else:
            return None

    def cambiar_estado_producto(self, codigo, disponible):
        """
        Cambia el estado de un producto.

        Parameters:
        codigo: Código del producto a cambiar su estado.
        disponible: Nuevo estado del producto.
        """
        sql = """
            UPDATE producto SET disponible = ? WHERE codigo = ?
        """

        cursor = self.conexion.cursor()

        cursor.execute(sql, (disponible, codigo))

        cursor.close()

    def ventas_rango_fechas(self, fecha_inicio, fecha_final):
        """
        Obtiene las ventas que se han realizado en un rango de fecha.

        Parameters:
        fecha_inicio: fecha de inicio del rango.
        fecha_final: fecha final del rango.

        Returns:
        Lista de ventas realizadas en el rango especificado.
        """
        sql = """
            SELECT * FROM venta WHERE fecha BETWEEN ? AND ?
        """

        cursor = self.conexion.cursor()

        cursor.execute(sql, (fecha_inicio, fecha_final))

        ventas = cursor.fetchall()

        if len(ventas) > 0:
            ventas = [Venta(**v) for v in ventas]
            cursor.close()

            return ventas
        else:
            cursor.close()
            return []

    def top_5_mas_vendidos(self):
        """
        Obtiene el top 5 de los productos más vendidos.

        Parameters:
        ventas: lista de las ventas realizadas hasta el momento.

        Returns:
        Lista de tuplas (id, cantidad_total_venta) de los 5 productos más vendidos.
        """
        conteo_ventas = {}

        sql = """
            SELECT * FROM venta
        """

        cursor = self.conexion.cursor()

        cursor.execute(sql)

        ventas = cursor.fetchall()

        cursor.close()

        for v in ventas:
            if v['codigo_producto'] in conteo_ventas:
                conteo_ventas[v['codigo_producto']] += v['cantidad']
            else:
                conteo_ventas[v['codigo_producto']] = v['cantidad']

        conteo_ventas = {k: v for k, v in sorted(conteo_ventas.items(), key=lambda item: item[1], reverse=True)}

        contador = Counter(conteo_ventas)

        return contador.most_common(5)

    def top_5_menos_vendidos(self):
        """
        Obtiene el top 5 de los productos menos vendidos.

        Returns:
        Lista de tuplas (id, cantidad_total_venta) de los 5 productos menos vendidos.
        """
        conteo_ventas = {}

        sql = """
            SELECT * FROM venta
        """

        cursor = self.conexion.cursor()

        cursor.execute(sql)

        ventas = cursor.fetchall()

        cursor.close()

        for v in ventas:
            if v['codigo_producto'] in conteo_ventas:
                conteo_ventas[v['codigo_producto']] += v['cantidad']
            else:
                conteo_ventas[v['codigo_producto']] = v['cantidad']

        conteo_ventas = {k: v for k, v in sorted(conteo_ventas.items(), key=lambda item: item[1])}

        contador = Counter(conteo_ventas)

        return contador.most_common()[:-6:-1]

    def mostrar_datos_producto(self, producto):
        """
        Muestra los datos particulares de un producto.

        Parameters:
        producto: Producto a consultar sus datos.
        """
        print('ID: %i' % producto.codigo)
        print('Nombre: %s' % producto.nombre)
        print('Precio: $%.2f' % producto.precio)
        print('Cantidad: %i' % producto.cantidad)
        print('¿Disponible?: %s' % ('Sí' if producto.disponible else 'No'))

    def mostrar_datos_venta(self, productos, venta):
        """
        Muestra los datos particulares de una venta.

        Parameters:
        venta: Venta a consultar sus datos.
        """
        print('ID Producto: %i' % venta.codigo_producto)
        print('Fecha: %s' % venta.fecha)
        print('Cantidad: %i' % venta.cantidad)
        print('Total sin IVA: $%.2f' % venta.total_sin_iva)
        print('Total:: $%.2f' % (venta.total_sin_iva * 1.19))
        print()
        print('Datos del producto:')
        self.mostrar_datos_producto(self.buscar_producto_por_codigo(venta.codigo_producto))

    def mostrar_datos_venta_producto(self, datos_venta):
        """
        Muestra los datos particulares de una venta.

        Parameters:
        datos_venta: tupla con los datos de la venta.
        """
        producto = self.buscar_producto_por_codigo(datos_venta[0])
        self.mostrar_datos_producto(producto)
        print('Cantidad vendida: %i' % datos_venta[1])
