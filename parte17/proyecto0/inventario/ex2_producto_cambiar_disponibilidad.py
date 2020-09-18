# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ex2_producto_cambiar_disponibilidad.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProductoCambiarDisponiblidad(object):
    def setupUi(self, ProductoCambiarDisponiblidad):
        ProductoCambiarDisponiblidad.setObjectName("ProductoCambiarDisponiblidad")
        ProductoCambiarDisponiblidad.resize(320, 110)
        ProductoCambiarDisponiblidad.setMinimumSize(QtCore.QSize(320, 110))
        ProductoCambiarDisponiblidad.setMaximumSize(QtCore.QSize(320, 110))
        self.gridLayout = QtWidgets.QGridLayout(ProductoCambiarDisponiblidad)
        self.gridLayout.setObjectName("gridLayout")
        self.lay_frm_principal = QtWidgets.QFormLayout()
        self.lay_frm_principal.setHorizontalSpacing(25)
        self.lay_frm_principal.setObjectName("lay_frm_principal")
        self.lbl_codigo = QtWidgets.QLabel(ProductoCambiarDisponiblidad)
        self.lbl_codigo.setObjectName("lbl_codigo")
        self.lay_frm_principal.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_codigo)
        self.txt_codigo = QtWidgets.QLineEdit(ProductoCambiarDisponiblidad)
        self.txt_codigo.setObjectName("txt_codigo")
        self.lay_frm_principal.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_codigo)
        self.btn_buscar = QtWidgets.QPushButton(ProductoCambiarDisponiblidad)
        self.btn_buscar.setObjectName("btn_buscar")
        self.lay_frm_principal.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btn_buscar)
        self.chk_disponiblidad = QtWidgets.QCheckBox(ProductoCambiarDisponiblidad)
        self.chk_disponiblidad.setObjectName("chk_disponiblidad")
        self.lay_frm_principal.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.chk_disponiblidad)
        self.gridLayout.addLayout(self.lay_frm_principal, 0, 0, 1, 1)

        self.retranslateUi(ProductoCambiarDisponiblidad)
        QtCore.QMetaObject.connectSlotsByName(ProductoCambiarDisponiblidad)

    def retranslateUi(self, ProductoCambiarDisponiblidad):
        _translate = QtCore.QCoreApplication.translate
        ProductoCambiarDisponiblidad.setWindowTitle(_translate("ProductoCambiarDisponiblidad", "Producto - Cambiar Disponibilidad"))
        self.lbl_codigo.setText(_translate("ProductoCambiarDisponiblidad", "Código:"))
        self.btn_buscar.setText(_translate("ProductoCambiarDisponiblidad", "Buscar"))
        self.chk_disponiblidad.setText(_translate("ProductoCambiarDisponiblidad", "¿Disponible para venta?"))
