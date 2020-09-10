# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ex2_producto_crear.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProductoCrear(object):
    def setupUi(self, ProductoCrear):
        ProductoCrear.setObjectName("ProductoCrear")
        ProductoCrear.resize(320, 200)
        ProductoCrear.setMinimumSize(QtCore.QSize(320, 200))
        ProductoCrear.setMaximumSize(QtCore.QSize(320, 200))
        self.gridLayout = QtWidgets.QGridLayout(ProductoCrear)
        self.gridLayout.setObjectName("gridLayout")
        self.lay_frm_principal = QtWidgets.QFormLayout()
        self.lay_frm_principal.setHorizontalSpacing(20)
        self.lay_frm_principal.setObjectName("lay_frm_principal")
        self.lbl_codigo = QtWidgets.QLabel(ProductoCrear)
        self.lbl_codigo.setObjectName("lbl_codigo")
        self.lay_frm_principal.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_codigo)
        self.txt_codigo = QtWidgets.QLineEdit(ProductoCrear)
        self.txt_codigo.setObjectName("txt_codigo")
        self.lay_frm_principal.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_codigo)
        self.lbl_nombre = QtWidgets.QLabel(ProductoCrear)
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.lay_frm_principal.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_nombre)
        self.txt_nombre = QtWidgets.QLineEdit(ProductoCrear)
        self.txt_nombre.setObjectName("txt_nombre")
        self.lay_frm_principal.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_nombre)
        self.lbl_precio = QtWidgets.QLabel(ProductoCrear)
        self.lbl_precio.setObjectName("lbl_precio")
        self.lay_frm_principal.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_precio)
        self.txt_precio = QtWidgets.QLineEdit(ProductoCrear)
        self.txt_precio.setObjectName("txt_precio")
        self.lay_frm_principal.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_precio)
        self.lbl_cantidad = QtWidgets.QLabel(ProductoCrear)
        self.lbl_cantidad.setObjectName("lbl_cantidad")
        self.lay_frm_principal.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_cantidad)
        self.chk_disponible = QtWidgets.QCheckBox(ProductoCrear)
        self.chk_disponible.setObjectName("chk_disponible")
        self.lay_frm_principal.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.chk_disponible)
        self.btn_registrar = QtWidgets.QPushButton(ProductoCrear)
        self.btn_registrar.setObjectName("btn_registrar")
        self.lay_frm_principal.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.btn_registrar)
        self.sbx_cantidad = QtWidgets.QSpinBox(ProductoCrear)
        self.sbx_cantidad.setObjectName("sbx_cantidad")
        self.lay_frm_principal.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sbx_cantidad)
        self.gridLayout.addLayout(self.lay_frm_principal, 0, 0, 1, 1)

        self.retranslateUi(ProductoCrear)
        QtCore.QMetaObject.connectSlotsByName(ProductoCrear)
        ProductoCrear.setTabOrder(self.txt_codigo, self.txt_nombre)
        ProductoCrear.setTabOrder(self.txt_nombre, self.txt_precio)
        ProductoCrear.setTabOrder(self.txt_precio, self.sbx_cantidad)
        ProductoCrear.setTabOrder(self.sbx_cantidad, self.chk_disponible)
        ProductoCrear.setTabOrder(self.chk_disponible, self.btn_registrar)

    def retranslateUi(self, ProductoCrear):
        _translate = QtCore.QCoreApplication.translate
        ProductoCrear.setWindowTitle(_translate("ProductoCrear", "Producto - Crear"))
        self.lbl_codigo.setText(_translate("ProductoCrear", "Código:"))
        self.lbl_nombre.setText(_translate("ProductoCrear", "Nombre:"))
        self.lbl_precio.setText(_translate("ProductoCrear", "Precio:"))
        self.lbl_cantidad.setText(_translate("ProductoCrear", "Cantidad:"))
        self.chk_disponible.setText(_translate("ProductoCrear", "¿Disponible para venta?"))
        self.btn_registrar.setText(_translate("ProductoCrear", "Crear"))
