# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ex2_producto_buscar.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProductoBuscar(object):
    def setupUi(self, ProductoBuscar):
        ProductoBuscar.setObjectName("ProductoBuscar")
        ProductoBuscar.resize(320, 185)
        ProductoBuscar.setMinimumSize(QtCore.QSize(320, 185))
        ProductoBuscar.setMaximumSize(QtCore.QSize(320, 185))
        self.gridLayout = QtWidgets.QGridLayout(ProductoBuscar)
        self.gridLayout.setObjectName("gridLayout")
        self.lay_ver_principal = QtWidgets.QVBoxLayout()
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lay_frm_busqueda = QtWidgets.QFormLayout()
        self.lay_frm_busqueda.setHorizontalSpacing(27)
        self.lay_frm_busqueda.setObjectName("lay_frm_busqueda")
        self.lbl_codigo = QtWidgets.QLabel(ProductoBuscar)
        self.lbl_codigo.setObjectName("lbl_codigo")
        self.lay_frm_busqueda.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_codigo)
        self.txt_codigo = QtWidgets.QLineEdit(ProductoBuscar)
        self.txt_codigo.setObjectName("txt_codigo")
        self.lay_frm_busqueda.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_codigo)
        self.btn_buscar = QtWidgets.QPushButton(ProductoBuscar)
        self.btn_buscar.setObjectName("btn_buscar")
        self.lay_frm_busqueda.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btn_buscar)
        self.lay_ver_principal.addLayout(self.lay_frm_busqueda)
        self.lay_frm_resultados = QtWidgets.QFormLayout()
        self.lay_frm_resultados.setHorizontalSpacing(20)
        self.lay_frm_resultados.setObjectName("lay_frm_resultados")
        self.lbl_nombre = QtWidgets.QLabel(ProductoBuscar)
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.lay_frm_resultados.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_nombre)
        self.txt_nombre = QtWidgets.QLineEdit(ProductoBuscar)
        self.txt_nombre.setReadOnly(True)
        self.txt_nombre.setObjectName("txt_nombre")
        self.lay_frm_resultados.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_nombre)
        self.lbl_precio = QtWidgets.QLabel(ProductoBuscar)
        self.lbl_precio.setObjectName("lbl_precio")
        self.lay_frm_resultados.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_precio)
        self.txt_precio = QtWidgets.QLineEdit(ProductoBuscar)
        self.txt_precio.setReadOnly(True)
        self.txt_precio.setObjectName("txt_precio")
        self.lay_frm_resultados.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_precio)
        self.lbl_cantidad = QtWidgets.QLabel(ProductoBuscar)
        self.lbl_cantidad.setObjectName("lbl_cantidad")
        self.lay_frm_resultados.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_cantidad)
        self.txt_cantidad = QtWidgets.QLineEdit(ProductoBuscar)
        self.txt_cantidad.setReadOnly(True)
        self.txt_cantidad.setObjectName("txt_cantidad")
        self.lay_frm_resultados.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_cantidad)
        self.chk_disponible = QtWidgets.QCheckBox(ProductoBuscar)
        self.chk_disponible.setObjectName("chk_disponible")
        self.lay_frm_resultados.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.chk_disponible)
        self.lay_ver_principal.addLayout(self.lay_frm_resultados)
        self.gridLayout.addLayout(self.lay_ver_principal, 0, 0, 1, 1)

        self.retranslateUi(ProductoBuscar)
        QtCore.QMetaObject.connectSlotsByName(ProductoBuscar)

    def retranslateUi(self, ProductoBuscar):
        _translate = QtCore.QCoreApplication.translate
        ProductoBuscar.setWindowTitle(_translate("ProductoBuscar", "Producto - Buscar"))
        self.lbl_codigo.setText(_translate("ProductoBuscar", "Código:"))
        self.btn_buscar.setText(_translate("ProductoBuscar", "Buscar"))
        self.lbl_nombre.setText(_translate("ProductoBuscar", "Nombre:"))
        self.lbl_precio.setText(_translate("ProductoBuscar", "Precio:"))
        self.lbl_cantidad.setText(_translate("ProductoBuscar", "Cantidad:"))
        self.chk_disponible.setText(_translate("ProductoBuscar", "¿Disponible para venta?"))
