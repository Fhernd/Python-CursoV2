from .modelos.inventario import Inventario
from .modelos.producto import Producto
from .modelos.venta import Venta
import datetime
import os
import pickle

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QWidget
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from PyQt5.QtCore import QDateTime

from .ex2_gestor_inventario import Ui_GestorInventario
from .ex2_producto_crear import Ui_ProductoCrear
from .ex2_producto_vender import Ui_ProductoVender
from .ex2_producto_buscar import Ui_ProductoBuscar
from .ex2_producto_cambiar_disponibilidad import Ui_ProductoCambiarDisponiblidad
from .ex2_reporte_ventas_rango_fechas import Ui_ReporteVentasRangoFechas
from .ex2_reporte_top_5 import Ui_ReporteTop5

class GestorInventarioAplicacion(QMainWindow):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
        self.cargar_inventario()
    
    def closeEvent(self, event):
        respuesta = QMessageBox.question(self, 'Confirmación', '¿Desea guardar los datos de la aplicación antes de salir?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if respuesta == QMessageBox.Yes:
            guardar_datos(self.inventario)
        
        event.accept()
    
    def cargar_inventario(self):

        if os.path.isfile('inventario/inventario.pickle'):
            respuesta = QMessageBox.question(self, 'Confirmación', '¿Desea cargar los datos desde el archivo inventario?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            
            self.inventario = Inventario()

            if respuesta == QMessageBox.Yes:
                with open('inventario/inventario.pickle', 'rb') as f:
                    resultado = pickle.load(f)
                
                if resultado:
                    self.inventario.productos = resultado.productos
                    self.inventario.ventas = resultado.ventas

    def inicializar_gui(self):
        self.ui = Ui_GestorInventario()
        self.ui.setupUi(self)

        self.ui.mni_producto_registrar.triggered.connect(self.registrar_producto)
        self.ui.mni_producto_vender.triggered.connect(self.vender_producto)
        self.ui.mni_producto_buscar.triggered.connect(self.buscar_producto)
        self.ui.mni_producto_cambiar_disponibilidad.triggered.connect(self.cambiar_disponibilidad)

        self.ui.mni_reporte_rango_fechas.triggered.connect(self.generar_reporte_rango_fechas)
        self.ui.mni_reporte_productos_mas_vendidos.triggered.connect(self.generar_reporte_mas_vendidos)
        self.ui.mni_reporte_productos_menos_vendidos.triggered.connect(self.generar_reporte_menos_vendidos)

        self.ui.mni_acerca_de.triggered.connect(self.acerca_de)

        self.show()
    
    def registrar_producto(self):
        gui = ProductoCrear(self.inventario)
        self.ui.mdi_principal.addSubWindow(gui)
        gui.show()
    
    def vender_producto(self):
        gui = ProductoVender(self.inventario)
        self.ui.mdi_principal.addSubWindow(gui)
        gui.show()
    
    def buscar_producto(self):
        gui = ProductoBuscar(self.inventario)
        self.ui.mdi_principal.addSubWindow(gui)
        gui.show()
    
    def cambiar_disponibilidad(self):
        gui = ProductoCambioDisponibilidad(self.inventario)
        self.ui.mdi_principal.addSubWindow(gui)
        gui.show()
    
    def generar_reporte_rango_fechas(self):
        gui = ReporteVentasRangoFechas(self.inventario)
        self.ui.mdi_principal.addSubWindow(gui)
        gui.show()
    
    def generar_reporte_mas_vendidos(self):
        gui = ReporteTop5(self.inventario)
        self.ui.mdi_principal.addSubWindow(gui)
        gui.show()
    
    def generar_reporte_menos_vendidos(self):
        gui = ReporteTop5MenosVendidos(self.inventario)
        self.ui.mdi_principal.addSubWindow(gui)
        gui.show()
    
    def acerca_de(self):
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle('Acerca de...')
        mensaje.setIcon(QMessageBox.Information)
        mensaje.setText('Gestor Inventario v. 1.0.0')
        mensaje.exec_()

class ProductoCrear(QWidget):
    def __init__(self, inventario):
        super().__init__()
        self.inventario = inventario

        self.inicializar_gui()
    
    def inicializar_gui(self):

        self.ui = Ui_ProductoCrear()
        self.ui.setupUi(self)

        self.mensaje = QMessageBox(self)
        self.mensaje.setWindowTitle('Mensaje')
        
        self.ui.btn_registrar.clicked.connect(self.producto_crear)
        self.ui.txt_codigo.setValidator(QIntValidator(1, 1000000, self))
        self.ui.txt_precio.setValidator(QDoubleValidator(1, 10000000, 2))
        self.ui.sbx_cantidad.setMinimum(1)
    
    def producto_crear(self):
        codigo = int(self.ui.txt_codigo.text())

        if self.inventario.buscar_producto(codigo):
            self.mensaje.setText('Ya existe un producto con el código especificado.')
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.exec_()
            return
        
        nombre = self.ui.txt_nombre.text().strip()

        if len(nombre) == 0:
            self.mensaje.setText('El campo Nombre es obligatorio.')
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.exec_()
            return
        
        precio = float(self.ui.txt_precio.text())
        cantidad = int(self.ui.sbx_cantidad.value())
        disponible = self.ui.chk_disponible.isChecked()

        nuevo_producto = Producto(codigo, nombre, precio, cantidad, disponible)
        self.inventario.registrar_producto(nuevo_producto)

        self.mensaje.setText('El producto se ha creado de forma satisfactoria.')
        self.mensaje.setIcon(QMessageBox.Information)
        self.mensaje.exec_()

        self.ui.txt_codigo.setText('')
        self.ui.txt_nombre.setText('')
        self.ui.txt_precio.setText('1')
        self.ui.sbx_cantidad.setValue(1)
        self.ui.chk_disponible.setCheckState(False)

class ProductoVender(QWidget):

    def __init__(self, inventario):
        super().__init__()

        self.inventario = inventario

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_ProductoVender()
        self.ui.setupUi(self)

        self.mensaje = QMessageBox(self)
        self.mensaje.setWindowTitle('Mensaje')

        self.ui.btn_vender.clicked.connect(self.vender)

        self.ui.txt_codigo.setValidator(QIntValidator(1, 1000000, self))
        self.ui.sbx_cantidad.setMinimum(1)
        self.ui.sbx_cantidad.setMaximum(1000)
    
    def vender(self):
        try:
            codigo = int(self.ui.txt_codigo.text())
        except:
            self.mensaje.setText('El campo Código es obligatorio.')
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.exec_()
            return

        producto = self.inventario.buscar_producto(codigo)

        if producto is None:
            self.mensaje.setText('No existe un producto con el código especificado.')
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.exec_()
            return
        
        cantidad = self.ui.sbx_cantidad.value()

        if cantidad == 0:
            self.mensaje.setText('Debe especificar al menos una unidad del producto para la venta.')
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.exec_()
            return

        venta = Venta(codigo, cantidad, producto.precio * cantidad)

        self.inventario.realizar_venta(venta)

        self.mensaje.setText('La venta se ha realizado de forma satisfactoria.')
        self.mensaje.setIcon(QMessageBox.Information)
        self.mensaje.exec_()

class ProductoBuscar(QWidget):

    def __init__(self, inventario):
        super().__init__()
        self.inventario = inventario

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_ProductoBuscar()
        self.ui.setupUi(self)

        self.mensaje = QMessageBox(self)
        self.mensaje.setWindowTitle('Mensaje')

        self.ui.btn_buscar.clicked.connect(self.buscar_producto)

        self.ui.txt_codigo.setValidator(QIntValidator(1, 1000000, self))
        self.ui.chk_disponible.setEnabled(False)
    
    def buscar_producto(self):
        codigo = self.ui.txt_codigo.text()

        if len(codigo) == 0:
            self.mensaje.setText('El campo Código es obligatorio.')
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.exec_()
            return
        
        codigo = int(codigo)

        producto = self.inventario.buscar_producto(codigo)

        if producto is None:
            self.mensaje.setText('No se ha encontrado un producto con el código especificado.')
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.exec_()
            return
        
        self.ui.txt_nombre.setText(producto.nombre)
        self.ui.txt_precio.setText(str(producto.precio))
        self.ui.txt_cantidad.setText(str(producto.cantidad))
        self.ui.chk_disponible.setCheckState(producto.disponible)

class ProductoCambioDisponibilidad(QWidget):

    def __init__(self, inventario):
        super().__init__()
        self.inventario = inventario
        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_ProductoCambiarDisponiblidad()
        self.ui.setupUi(self)

        self.mensaje = QMessageBox(self)
        self.mensaje.setWindowTitle('Mensaje')

        self.ui.btn_buscar.clicked.connect(self.cambiar_disponibilidad)
        self.ui.txt_codigo.setValidator(QIntValidator(1, 1000000, self))

        self.ui.chk_disponiblidad.setEnabled(False)
    
    def cambiar_disponibilidad(self):
        codigo = self.ui.txt_codigo.text()

        if len(codigo) == 0:
            self.mensaje.setText('El campo Código es obligatorio.')
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.exec_()
            return
        
        codigo = int(codigo)

        self.producto = self.inventario.buscar_producto(codigo)

        if self.producto is None:
            self.mensaje.setText('No se ha encontrado un producto con el código especificado.')
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.exec_()
            return
        
        self.ui.chk_disponiblidad.setEnabled(True)
        self.ui.chk_disponiblidad.setChecked(self.producto.disponible)

        self.ui.chk_disponiblidad.stateChanged.connect(self.cambiar_disponibilidad_producto)
    
    def cambiar_disponibilidad_producto(self):
        self.producto.disponible = not self.producto.disponible

class ReporteVentasRangoFechas(QWidget):

    def __init__(self, inventario):
        super().__init__()

        self.inventario = inventario

        self.inicializar_gui()

    def inicializar_gui(self):
        self.ui = Ui_ReporteVentasRangoFechas()
        self.ui.setupUi(self)

        self.mensaje = QMessageBox(self)
        self.mensaje.setWindowTitle('Mensaje')

        self.ui.btn_buscar.clicked.connect(self.buscar_ventas)
        self.ui.dat_fecha_inicio.setMaximumDateTime(QDateTime.currentDateTime())
        self.ui.dat_fecha_final.setMaximumDateTime(QDateTime.currentDateTime())
    
    def buscar_ventas(self):
        fecha_inicio = self.ui.dat_fecha_inicio.date()
        fecha_final = self.ui.dat_fecha_final.date()

        if fecha_inicio > fecha_final:
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.setText('La fecha de inicio no puede ser mayor a la fecha final.')
            self.mensaje.exec_()
            return
        
        fecha_inicio = fecha_inicio.toString('yyyy-MM-dd')
        fecha_final = fecha_final.toString('yyyy-MM-dd')

        fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
        fecha_final = datetime.datetime.strptime(fecha_final, '%Y-%m-%d')
        fecha_final.replace(hour=23, minute=59, second=59, microsecond=999999)

        ventas = self.inventario.ventas_rango_fecha(fecha_inicio, fecha_final)

        for v in ventas:
            numero_fila = self.ui.tbl_ventas.rowCount()
            self.ui.tbl_ventas.insertRow(numero_fila)

            self.ui.tbl_ventas.setItem(numero_fila, 0, QTableWidgetItem(str(v.codigo_producto)))
            self.ui.tbl_ventas.setItem(numero_fila, 1, QTableWidgetItem(v.fecha.strftime('%Y-%m-%d')))
            self.ui.tbl_ventas.setItem(numero_fila, 2, QTableWidgetItem(str(v.cantidad)))
            total = v.total_sin_iva * 1.13
            self.ui.tbl_ventas.setItem(numero_fila, 3, QTableWidgetItem('{:.2f}'.format(total)))

class ReporteTop5(QWidget):

    def __init__(self, inventario):
        super().__init__()

        self.inventario = inventario

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_ReporteTop5()
        self.ui.setupUi(self)

        self.setWindowTitle('Reporte - Top 5 Productos Más Vendidos')

        self.cargar_reporte_top_5_mas_vendidos()

    def cargar_reporte_top_5_mas_vendidos(self):
        productos_vendidos = self.inventario.top_5_mas_vendidos()

        for p in productos_vendidos:
            producto = self.inventario.buscar_producto(p[0])
            cantidad = p[1]
            total = cantidad * producto.precio

            numeroFila = self.ui.tbl_top_5.rowCount()
            self.ui.tbl_top_5.insertRow(numeroFila)

            self.ui.tbl_top_5.setItem(numeroFila, 0, QTableWidgetItem(str(p[0])))
            self.ui.tbl_top_5.setItem(numeroFila, 1, QTableWidgetItem(producto.nombre))
            self.ui.tbl_top_5.setItem(numeroFila, 2, QTableWidgetItem(str(producto.precio)))
            self.ui.tbl_top_5.setItem(numeroFila, 3, QTableWidgetItem(str(cantidad)))
            self.ui.tbl_top_5.setItem(numeroFila, 4, QTableWidgetItem(str(total)))

class ReporteTop5MenosVendidos(QWidget):
    def __init__(self, inventario):
        super().__init__()

        self.inventario = inventario

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_ReporteTop5()
        self.ui.setupUi(self)

        self.setWindowTitle('Reporte - Top 5 Productos Menos Vendidos')

        self.cargar_reporte_top_5_menos_vendidos()

    def cargar_reporte_top_5_menos_vendidos(self):
        productos_vendidos = self.inventario.top_5_menos_vendidos()

        for p in productos_vendidos:
            producto = self.inventario.buscar_producto(p[0])
            cantidad = p[1]
            total = cantidad * producto.precio

            numeroFila = self.ui.tbl_top_5.rowCount()
            self.ui.tbl_top_5.insertRow(numeroFila)

            self.ui.tbl_top_5.setItem(numeroFila, 0, QTableWidgetItem(str(p[0])))
            self.ui.tbl_top_5.setItem(numeroFila, 1, QTableWidgetItem(producto.nombre))
            self.ui.tbl_top_5.setItem(numeroFila, 2, QTableWidgetItem(str(producto.precio)))
            self.ui.tbl_top_5.setItem(numeroFila, 3, QTableWidgetItem(str(cantidad)))
            self.ui.tbl_top_5.setItem(numeroFila, 4, QTableWidgetItem(str(total)))

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
        print(f"{p.codigo} - {p.nombre}")

def continuar():
    """
    Muestra mensaje de continuación en la consola.
    """
    print()
    print('Presione Enter para continuar...', end='')
    input()
    print()

def cargar_inventario():
    with open('inventario/inventario.pickle', 'rb') as f:
        inventario = pickle.load(f)
        return inventario

def guardar_datos(inventario):
    with open('inventario/inventario.pickle', 'wb') as f:
        pickle.dump(inventario, f)

def main():

    app = QApplication(sys.argv)
    ventana = GestorInventarioAplicacion()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
