import datetime

import flet as ft
from flet import AppBar, Page, PopupMenuButton, Text, View, colors

from modelos.inventario import Inventario
from modelos.producto import Producto
from modelos.venta import Venta
from conexion import conectar


class InventarioApp:
    """
    Clase principal del gestor de inventario.
    """

    def __init__(self):
        """
        Constructor de la clase.
        """
        self.producto = None
    
    def main(self, page: Page):
        inventario = Inventario()
        page.title = "Gestor Inventario - Dispositivos s.a.s. - Por: OrtizOL"

        def close_dlg(e):
            dlg_modal.open = False
            page.update()
        
        def on_confirmar_cierre(e):
            page.window_close()

        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text('Mensaje'),
            content=ft.Text(''),
            actions_alignment=ft.MainAxisAlignment.END
        )

        def mostrar_mensaje(mensaje):
            """
            Muestra un mensaje de advertencia en un diálogo modal.

            Parameters:
            mensaje: mensaje a mostrar en el diálogo modal.
            """
            dlg_modal.content = ft.Text(mensaje)
            dlg_modal.actions = [
                ft.TextButton("Aceptar", on_click=close_dlg),
            ]
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()

        def on_click_salir(e):
            dlg_modal.content = ft.Text("¿Desea salir de la aplicación?")
            dlg_modal.actions = [
                ft.TextButton("Sí", on_click=on_confirmar_cierre),
                ft.TextButton("No", on_click=close_dlg),
            ]
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()

        def on_click_nav_producto_registrar(e):
            page.go('/producto/registrar')
        
        def on_click_nav_producto_vender(e):
            page.go('/producto/vender')

        def on_click_nav_producto_buscar(e):
            page.go('/producto/buscar')

        def on_click_nav_producto_cambiar_disponibilidad(e):
            page.go('/producto/cambiar_disponibilidad')

        def on_click_nav_ventas_rango_fechas(e):
            page.go('/ventas/rango_fechas')

        def on_click_nav_producto_top_5_mas_vendidos(e):
            page.go('/producto/top_5_mas_vendidos')

        def on_click_nav_producto_top_5_menos_vendidos(e):
            page.go('/producto/top_5_menos_vendidos')

        def on_click_acerca_de(e):
            mostrar_mensaje("Desarrollado por: John Ortiz Ordoñez\n" + \
                "Versión: 1.0.0\n" + \
                "Sitio Web: https://ortizol.blogspot.com")

        def on_click_registrar_producto(e):
            codigo = self.text_codigo.current.value.strip()
            nombre = self.txt_nombre.current.value.strip()
            precio = self.txt_precio.current.value.strip()
            cantidad = self.txt_cantidad.current.value.strip()
            disponible = self.chk_disponible_venta.current.value

            if len(codigo) == 0 and len(nombre) == 0 and len(precio) == 0 and len(cantidad) == 0:
                mostrar_mensaje("Todos los campos son obligatorios. Los valores numéricos deben ser mayores a 0.")
                return
            
            try:
                codigo = int(codigo)
            except ValueError:
                mostrar_mensaje("El código debe ser numérico.")
                return
            
            if codigo <= 0:
                mostrar_mensaje("El código debe ser positivo.")
                return

            try:
                precio = float(precio)
            except ValueError:
                mostrar_mensaje("El precio debe ser numérico.")
                return

            if precio <= 0:
                mostrar_mensaje("El precio debe ser positivo.")
                return

            try:
                cantidad = int(cantidad)
            except ValueError:
                mostrar_mensaje("La cantidad debe ser numérica.")
                return

            if cantidad <= 0:
                mostrar_mensaje("La cantidad debe ser positiva.")
                return
            
            conexion = conectar('inventario/inventario.db')
            inventario.recibir_conexion_bd(conexion)
            producto = inventario.buscar_producto_por_codigo(codigo)

            if producto:
                mostrar_mensaje("Ya existe un producto con el código especificado.")
                return

            nuevo_producto = Producto(codigo, nombre, precio, cantidad, disponible)

            inventario.registrar_producto(nuevo_producto)

            mostrar_mensaje("El producto se ha creado de forma satisfactoria.")

            self.text_codigo.current.value = ''
            self.txt_nombre.current.value = ''
            self.txt_precio.current.value = ''
            self.txt_cantidad.current.value = ''
            self.chk_disponible_venta.current.value = True

            conexion.close()

        self.text_codigo = ft.Ref[ft.TextField]()
        self.txt_nombre = ft.Ref[ft.TextField]()
        self.txt_precio = ft.Ref[ft.TextField]()
        self.txt_cantidad = ft.Ref[ft.TextField]()
        self.chk_disponible_venta = ft.Ref[ft.Checkbox]()
        self.ref_txt_fecha_inicio = ft.Ref[ft.TextField]()
        self.ref_txt_fecha_fin = ft.Ref[ft.TextField]()
        self.ref_tbl_ventas = ft.Ref[ft.DataTable]()

        def on_change_cambiar_disponibilidad_producto(e):
            estado_disponibilidad = self.chk_disponible_venta.current.value

            self.producto.disponible = estado_disponibilidad

            conexion = conectar('inventario/inventario.db')
            inventario.recibir_conexion_bd(conexion)

            inventario.cambiar_estado_producto(producto.codigo, estado_disponibilidad)

            conexion.commit()

            conexion.close()

            mostrar_mensaje("El estado del producto se ha cambiado de forma satisfactoria.")

            page.update()

        def on_click_vender_producto(e):
            codigo = self.text_codigo.current.value.strip()
            cantidad = self.txt_cantidad.current.value.strip()

            if len(codigo) == 0 or len(cantidad) == 0:
                mostrar_mensaje("Todos los campos son obligatorios. Los valores numéricos deben ser mayores a 0.")
                return
            
            try:
                codigo = int(codigo)
            except ValueError:
                mostrar_mensaje("El código debe ser numérico.")
                return
            
            if codigo <= 0:
                mostrar_mensaje("El código debe ser positivo.")
                return
            
            try:
                cantidad = int(cantidad)
            except ValueError:
                mostrar_mensaje("La cantidad debe ser numérica.")
                return

            if cantidad <= 0:
                mostrar_mensaje("La cantidad debe ser positiva.")
                return
            
            conexion = conectar('inventario/inventario.db')
            inventario.recibir_conexion_bd(conexion)

            producto = inventario.buscar_producto_por_codigo(codigo)

            if not producto:
                mostrar_mensaje("El producto no existe. Intente con otro código")
                return
            
            if not producto.disponible:
                mostrar_mensaje("El producto no está disponible para la venta.")
                return
            
            if cantidad > producto.cantidad:
                mostrar_mensaje("La cantidad solicitada es mayor a la cantidad disponible.")
                return
            
            total_sin_iva = producto.precio * cantidad

            venta = Venta(codigo, cantidad, total_sin_iva)

            conexion = conectar('inventario/inventario.db')
            inventario.recibir_conexion_bd(conexion)

            inventario.realizar_venta(venta)

            mostrar_mensaje("La venta se ha realizado de forma satisfactoria.")

            self.text_codigo.current.value = ''
            self.txt_cantidad.current.value = ''
            
        def on_click_buscar_producto(e):
            codigo = self.text_codigo.current.value.strip()

            if len(codigo) == 0:
                mostrar_mensaje("Todos los campos son obligatorios. Los valores numéricos deben ser mayores a 0.")
                return
            
            try:
                codigo = int(codigo)
            except ValueError:
                mostrar_mensaje("El código debe ser numérico.")
                return
            
            if codigo <= 0:
                mostrar_mensaje("El código debe ser positivo.")
                return
            
            conexion = conectar('inventario/inventario.db')
            inventario.recibir_conexion_bd(conexion)

            producto = inventario.buscar_producto_por_codigo(codigo)

            conexion.close()

            if not producto:
                mostrar_mensaje("El producto no existe.")
                self.txt_nombre.current.value = ''
                self.txt_precio.current.value = ''
                self.txt_cantidad.current.value = ''
                return

            self.txt_nombre.current.value = producto.nombre
            self.txt_precio.current.value = producto.precio
            self.txt_cantidad.current.value = producto.cantidad
            self.chk_disponible_venta.current.value = producto.disponible

            page.update()

        def on_click_buscar_producto_cambiar_disponibilidad(e):
            global producto
            
            codigo = self.text_codigo.current.value.strip()

            if len(codigo) == 0:
                mostrar_mensaje("Todos los campos son obligatorios. Los valores numéricos deben ser mayores a 0.")
                return
            
            try:
                codigo = int(codigo)
            except ValueError:
                mostrar_mensaje("El código debe ser numérico.")
                return
            
            if codigo <= 0:
                mostrar_mensaje("El código debe ser positivo.")
                return
            
            conexion = conectar('inventario/inventario.db')
            inventario.recibir_conexion_bd(conexion)

            self.producto = inventario.buscar_producto_por_codigo(codigo)

            conexion.close()

            if not producto:
                mostrar_mensaje("El producto no existe.")
                self.chk_disponible_venta.current.value = False
                self.chk_disponible_venta.current.disabled = True
                return
            
            self.chk_disponible_venta.current.disabled = False
            self.chk_disponible_venta.current.value = bool(producto.disponible)
            self.chk_disponible_venta.current.update()

            page.update()

        def on_click_generar_reporte_ventas_rango_fechas(e):
            fecha_inicio = self.ref_txt_fecha_inicio.current.value.strip()
            fecha_fin = self.ref_txt_fecha_fin.current.value.strip()

            if len(fecha_inicio) == 0 or len(fecha_fin) == 0:
                mostrar_mensaje("Todos los campos son obligatorios.")
                return
            
            try:
                fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%d/%m/%Y')
            except ValueError:
                mostrar_mensaje("El formato de la fecha de inicio es incorrecto. Debe ser dd/mm/aaaa.")
                return
            
            try:
                fecha_fin = datetime.datetime.strptime(fecha_fin, '%d/%m/%Y')
            except ValueError:
                mostrar_mensaje("El formato de la fecha final es incorrecto. Debe ser dd/mm/aaaa.")
                return
            
            if fecha_fin < fecha_inicio:
                mostrar_mensaje("La fecha final debe ser mayor o igual a la fecha de inicio.")
                return

            conexion = conectar('inventario/inventario.db')
            inventario.recibir_conexion_bd(conexion)

            ventas = inventario.ventas_rango_fechas(fecha_inicio, fecha_fin)

            conexion.close()

            if len(ventas) == 0:
                mostrar_mensaje("No se encontraron ventas en el rango de fechas especificado.")
                self.ref_tbl_ventas.current.rows = []
                self.ref_tbl_ventas.current.update()
                return

            rows = []

            for venta in ventas:
                cells = []
                cells.append(ft.DataCell(ft.Text(venta.codigo_producto)))
                cells.append(ft.DataCell(ft.Text(venta.fecha)))
                cells.append(ft.DataCell(ft.Text(venta.cantidad)))
                cells.append(ft.DataCell(ft.Text(venta.total_sin_iva * 1.19)))

                rows.append(ft.DataRow(cells=cells))

            self.ref_tbl_ventas.current.rows = rows
                
            self.ref_tbl_ventas.current.update()

        def generar_tabla():
            columnas = ('Código Producto', 'Fecha', 'Cantidad', 'Total')

            # Cree una lista de lista con 5 filas y 4 columnas:
            datos = [
                ['', '', '', ''],
            ]

            rows = []

            for fila in datos:
                cells = []

                for columna in fila:
                    cells.append(ft.DataCell(ft.Text(columna)))

                rows.append(ft.DataRow(cells=cells))

            return ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text(d)) for d in columnas
                ],
                rows=rows,
            )

        def generar_vista_producto_registrar():

            row_codigo = ft.ResponsiveRow([
                ft.Container(
                    ft.TextField(
                        label="Código",
                        hint_text="Ingrese el código del producto",
                        ref=self.text_codigo
                    ),
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )
            
            row_nombre = ft.ResponsiveRow([
                ft.Container(
                    ft.TextField(
                        label="Nombre",
                        hint_text="Ingrese el nombre del producto",
                        ref=self.txt_nombre
                    ),
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )

            row_precio = ft.ResponsiveRow([
                ft.Container(
                    ft.TextField(
                        label="Precio",
                        hint_text="Ingrese el precio del producto",
                        ref=self.txt_precio
                    ),
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )

            row_cantidad = ft.ResponsiveRow([
                ft.Container(
                    ft.TextField(
                        label="Cantidad",
                        hint_text="Ingrese la cantidad del producto",
                        ref=self.txt_cantidad
                    ),
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )

            row_disponible_venta = ft.ResponsiveRow([
                ft.Container(
                    ft.Checkbox(label="¿Disponible para venta?", value=True, ref=self.chk_disponible_venta),
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )

            row_crear = ft.ResponsiveRow([
                ft.Container(
                    ft.FilledButton(text='Crear', on_click=on_click_registrar_producto),
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )

            return ft.Column(
                [
                    row_codigo,
                    row_nombre,
                    row_precio,
                    row_cantidad,
                    row_disponible_venta,
                    row_crear
                ],
                spacing=2
            )

        def generar_vista_producto_vender():
            row_codigo = ft.ResponsiveRow([
                ft.Container(
                    ft.TextField(
                        label="Código",
                        hint_text="Ingrese el código del producto",
                        ref=self.text_codigo
                    ),
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )

            row_cantidad = ft.ResponsiveRow([
                ft.Container(
                    ft.TextField(
                        label="Cantidad",
                        hint_text="Ingrese la cantidad del producto",
                        ref=self.txt_cantidad
                    ),
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )

            row_vender = ft.ResponsiveRow([
                ft.Container(
                    ft.FilledButton(text='Vender', on_click=on_click_vender_producto),
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )

            return ft.Column(
                [
                    row_codigo,
                    row_cantidad,
                    row_vender
                ],
                spacing=2
            )
            
        def generar_vista_producto_buscar():
            row_codigo = ft.ResponsiveRow([
                ft.Container(
                    ft.TextField(
                        label="Código",
                        hint_text="Ingrese el código del producto a buscar",
                        ref=self.text_codigo
                    ),
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )
            
            row_nombre = ft.ResponsiveRow([
                ft.Container(
                    ft.TextField(
                        label="Nombre",
                        ref=self.txt_nombre,
                        read_only=True
                    ),
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )

            row_precio = ft.ResponsiveRow([
                ft.Container(
                    ft.TextField(
                        label="Precio",
                        ref=self.txt_precio,
                        read_only=True
                    ),
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )

            row_cantidad = ft.ResponsiveRow([
                ft.Container(
                    ft.TextField(
                        label="Cantidad",
                        ref=self.txt_cantidad,
                        read_only=True
                    ),
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )

            row_disponible_venta = ft.ResponsiveRow([
                ft.Container(
                    ft.Checkbox(label="¿Disponible para venta?", value=True, ref=self.chk_disponible_venta),
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )

            row_buscar = ft.ResponsiveRow([
                ft.Container(
                    ft.FilledButton(text='Buscar', on_click=on_click_buscar_producto),
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )

            return ft.Column(
                [
                    row_codigo,
                    row_buscar,
                    row_nombre,
                    row_precio,
                    row_cantidad,
                    row_disponible_venta
                ],
                spacing=2
            )

        def generar_vista_producto_cambiar_disponibilidad():
            row_codigo = ft.ResponsiveRow([
                ft.Container(
                    ft.TextField(
                        label="Código",
                        hint_text="Ingrese el código del producto a buscar",
                        ref=self.text_codigo
                    ),
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )

            row_buscar = ft.ResponsiveRow([
                ft.Container(
                    ft.FilledButton(text='Buscar', on_click=on_click_buscar_producto_cambiar_disponibilidad),
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )

            row_disponible_venta = ft.ResponsiveRow([
                ft.Container(
                    ft.Checkbox(
                        label="¿Disponible para venta?", 
                        value=False, 
                        ref=self.chk_disponible_venta,
                        disabled=True,
                        on_change=on_change_cambiar_disponibilidad_producto
                        ),
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )

            return ft.Column(
                [
                    row_codigo,
                    row_buscar,
                    row_disponible_venta
                ],
                spacing=2
            )

        def generar_vista_reporte_ventas_rango_fechas():
            row_fecha_inicio = ft.ResponsiveRow([
                ft.Container(
                    ft.TextField(
                        label="Fecha inicio",
                        hint_text="Ingrese la fecha de inicio",
                        ref=self.ref_txt_fecha_inicio
                    ),
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )
            
            row_fecha_fin = ft.ResponsiveRow([
                ft.Container(
                    ft.TextField(
                        label="Fecha fin",
                        hint_text="Ingrese la fecha fin",
                        ref=self.ref_txt_fecha_fin
                    ),
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )

            row_buscar = ft.ResponsiveRow([
                ft.Container(
                    ft.FilledButton(text='Buscar', on_click=on_click_generar_reporte_ventas_rango_fechas),
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )

            self.ref_tbl_ventas.current = generar_tabla()

            row_ventas = ft.ResponsiveRow([
                ft.Container(
                    self.ref_tbl_ventas.current,
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )

            return ft.Column(
                [
                    row_fecha_inicio,
                    row_fecha_fin,
                    row_buscar,
                    row_ventas
                ],
                spacing=2
            )

        def generar_vista_reporte_top_5(orden='descendete'):
            rows = []

            conexion = conectar('inventario/inventario.db')
            inventario.recibir_conexion_bd(conexion)

            if orden == 'descendete':
                productos = inventario.top_5_mas_vendidos()
            else:
                productos = inventario.top_5_menos_vendidos()

            for p in productos:
                producto = inventario.buscar_producto_por_codigo(p[0])

                cells = []

                cells.append(ft.DataCell(ft.Text(producto.codigo)))
                cells.append(ft.DataCell(ft.Text(producto.nombre)))
                cells.append(ft.DataCell(ft.Text(producto.precio)))
                cells.append(ft.DataCell(ft.Text(p[1])))

                total = producto.precio * p[1] * 1.19
                cells.append(ft.DataCell(ft.Text(total)))

                rows.append(ft.DataRow(cells=cells))

            conexion.close()
            
            self.ref_tbl_ventas.current = ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Código Producto")),
                    ft.DataColumn(ft.Text("Nombre Producto")),
                    ft.DataColumn(ft.Text("Precio")),
                    ft.DataColumn(ft.Text("Cantidad vendida")),
                    ft.DataColumn(ft.Text("Total")),
                ],
                rows=rows,
            )

            row_ventas = ft.ResponsiveRow([
                ft.Container(
                    self.ref_tbl_ventas.current,
                    col={"sm": 12, "md": 12, "xl": 12},
                )
                ],
            )

            return ft.Column(
                [
                    row_ventas
                ],
                spacing=2
            )

        def on_route_change(e):
            page.views.clear()

            mnu_archivo = PopupMenuButton(
                content=Text('Archivo'),
                items=[
                    ft.PopupMenuItem(text='Salir', on_click=on_click_salir)
                ]
            )

            mnu_productos = PopupMenuButton(
                content=ft.Text('Productos'),
                items=[
                    ft.PopupMenuItem(text='Registrar', on_click=on_click_nav_producto_registrar),
                    ft.PopupMenuItem(text='Vender', on_click=on_click_nav_producto_vender),
                    ft.PopupMenuItem(text='Buscar', on_click=on_click_nav_producto_buscar),
                    ft.PopupMenuItem(text='Cambiar disponibilidad', on_click=on_click_nav_producto_cambiar_disponibilidad)
                ]
            )
            
            mnu_reportes = PopupMenuButton(
                content=Text('Reportes'),
                items=[
                    ft.PopupMenuItem(text='Ventas en un rango de fechas', on_click=on_click_nav_ventas_rango_fechas),
                    ft.PopupMenuItem(text='Top 5 productos más vendidos', on_click=on_click_nav_producto_top_5_mas_vendidos),
                    ft.PopupMenuItem(text='Top 5 productos menos vendidos', on_click=on_click_nav_producto_top_5_menos_vendidos),
                ]
            )
            
            mnu_ayuda = PopupMenuButton(
                content=Text('Ayuda'),
                items=[
                    ft.PopupMenuItem(text='Acerca de...', on_click=on_click_acerca_de),
                ]
            )

            mbr_principal = ft.ResponsiveRow([
                ft.Container(
                    mnu_archivo,
                    col={"sm": 2, "md": 2, "xl": 2},
                ),
                ft.Container(
                    mnu_productos,
                    col={"sm": 2, "md": 2, "xl": 2},
                ),
                ft.Container(
                    mnu_reportes,
                    col={"sm": 2, "md": 2, "xl": 2},
                ),
                ft.Container(
                    mnu_ayuda,
                    col={"sm": 2, "md": 2, "xl": 2},
                ),
            ],
            )

            page.views.append(
                View(
                    "/",
                    [
                        AppBar(title=Text('Gestión Inventario - Dispositivos S.a.s.')),
                        mbr_principal
                    ],
                )
            )

            if page.route == "/producto/registrar":
                page.views.append(
                    View(
                        "/producto/registrar",
                        [
                            AppBar(title=Text("Producto - Registrar"), bgcolor=colors.SURFACE_VARIANT),
                            generar_vista_producto_registrar()
                        ]
                    )
                )
            
            if page.route == "/producto/vender":
                page.views.append(
                    View(
                        "/producto/vender",
                        [
                            AppBar(title=Text("Producto - Vender"), bgcolor=colors.SURFACE_VARIANT),
                            generar_vista_producto_vender()
                        ]
                    )
                )
            
            if page.route == "/producto/buscar":
                page.views.append(
                    View(
                        "/producto/buscar",
                        [
                            AppBar(title=Text("Producto - Buscar"), bgcolor=colors.SURFACE_VARIANT),
                            generar_vista_producto_buscar()
                        ]
                    )
                )
            
            if page.route == "/producto/cambiar_disponibilidad":
                page.views.append(
                    View(
                        "/producto/cambiar_disponibilidad",
                        [
                            AppBar(title=Text("Producto - Cambiar Disponibilidad"), bgcolor=colors.SURFACE_VARIANT),
                            generar_vista_producto_cambiar_disponibilidad()
                        ]
                    )
                )
            
            if page.route == '/ventas/rango_fechas':
                page.views.append(
                    View(
                        '/ventas/rango_fechas',
                        [
                            AppBar(title=Text("Reporte - Ventas en un rango de fechas"), bgcolor=colors.SURFACE_VARIANT),
                            generar_vista_reporte_ventas_rango_fechas()
                        ]
                    )
                )
            
            if page.route == '/producto/top_5_mas_vendidos':
                page.views.append(
                    View(
                        '/producto/top_5_mas_vendidos',
                        [
                            AppBar(title=Text("Reporte - Top 5 Productos Más Vendidos"), bgcolor=colors.SURFACE_VARIANT),
                            generar_vista_reporte_top_5()
                        ]
                    )
                )
            
            if page.route == '/producto/top_5_menos_vendidos':
                page.views.append(
                    View(
                        '/producto/top_5_menos_vendidos',
                        [
                            AppBar(title=Text("Reporte - Top 5 Productos Menos Vendidos"), bgcolor=colors.SURFACE_VARIANT),
                            generar_vista_reporte_top_5('ascendente')
                        ]
                    )
                )
        
            page.update()

        def view_pop(e):
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

        page.on_route_change = on_route_change
        page.on_view_pop = view_pop

        page.go(page.route)


if __name__ == "__main__":
    app = InventarioApp()
    ft.app(target=app.main)
