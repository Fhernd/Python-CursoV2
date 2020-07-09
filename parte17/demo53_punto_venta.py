# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo53_punto_venta.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PuntoVenta(object):
    def setupUi(self, PuntoVenta):
        PuntoVenta.setObjectName("PuntoVenta")
        PuntoVenta.resize(555, 152)
        self.verticalLayoutWidget = QtWidgets.QWidget(PuntoVenta)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(2, 1, 551, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 10, 10, 0)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lay_hor_mouse = QtWidgets.QHBoxLayout()
        self.lay_hor_mouse.setObjectName("lay_hor_mouse")
        self.lbl_producto_mouse = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_producto_mouse.setObjectName("lbl_producto_mouse")
        self.lay_hor_mouse.addWidget(self.lbl_producto_mouse)
        self.txt_mouse_precio = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_mouse_precio.setObjectName("txt_mouse_precio")
        self.lay_hor_mouse.addWidget(self.txt_mouse_precio)
        self.sbx_mouse_cantidad = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbx_mouse_cantidad.setObjectName("sbx_mouse_cantidad")
        self.lay_hor_mouse.addWidget(self.sbx_mouse_cantidad)
        self.txt_mouse_subtotal = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_mouse_subtotal.setReadOnly(True)
        self.txt_mouse_subtotal.setObjectName("txt_mouse_subtotal")
        self.lay_hor_mouse.addWidget(self.txt_mouse_subtotal)
        self.lay_hor_mouse.setStretch(0, 2)
        self.lay_hor_mouse.setStretch(1, 1)
        self.lay_hor_mouse.setStretch(2, 1)
        self.lay_hor_mouse.setStretch(3, 1)
        self.lay_ver_principal.addLayout(self.lay_hor_mouse)
        self.lay_hor_teclado = QtWidgets.QHBoxLayout()
        self.lay_hor_teclado.setObjectName("lay_hor_teclado")
        self.lbl_producto_teclado = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_producto_teclado.setObjectName("lbl_producto_teclado")
        self.lay_hor_teclado.addWidget(self.lbl_producto_teclado)
        self.txt_teclado_precio = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_teclado_precio.setObjectName("txt_teclado_precio")
        self.lay_hor_teclado.addWidget(self.txt_teclado_precio)
        self.sbx_teclado_cantidad = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbx_teclado_cantidad.setObjectName("sbx_teclado_cantidad")
        self.lay_hor_teclado.addWidget(self.sbx_teclado_cantidad)
        self.txt_teclado_subtotal = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_teclado_subtotal.setReadOnly(True)
        self.txt_teclado_subtotal.setObjectName("txt_teclado_subtotal")
        self.lay_hor_teclado.addWidget(self.txt_teclado_subtotal)
        self.lay_hor_teclado.setStretch(0, 2)
        self.lay_hor_teclado.setStretch(1, 1)
        self.lay_hor_teclado.setStretch(2, 1)
        self.lay_hor_teclado.setStretch(3, 1)
        self.lay_ver_principal.addLayout(self.lay_hor_teclado)
        self.lbl_total = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_total.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_total.setObjectName("lbl_total")
        self.lay_ver_principal.addWidget(self.lbl_total)

        self.retranslateUi(PuntoVenta)
        QtCore.QMetaObject.connectSlotsByName(PuntoVenta)

    def retranslateUi(self, PuntoVenta):
        _translate = QtCore.QCoreApplication.translate
        PuntoVenta.setWindowTitle(_translate("PuntoVenta", "Punto de Venta"))
        self.lbl_producto_mouse.setText(_translate("PuntoVenta", "Producto Mouse HyperX:"))
        self.lbl_producto_teclado.setText(_translate("PuntoVenta", "Producto Teclado HyperX:"))
        self.lbl_total.setText(_translate("PuntoVenta", "$0.00"))
