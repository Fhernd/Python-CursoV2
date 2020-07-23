# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo84_busqueda_datos.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BusquedaDatos(object):
    def setupUi(self, BusquedaDatos):
        BusquedaDatos.setObjectName("BusquedaDatos")
        BusquedaDatos.resize(320, 145)
        BusquedaDatos.setMinimumSize(QtCore.QSize(320, 145))
        BusquedaDatos.setMaximumSize(QtCore.QSize(320, 145))
        self.verticalLayoutWidget = QtWidgets.QWidget(BusquedaDatos)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 126))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 15, 10, 0)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lay_frm_documento = QtWidgets.QFormLayout()
        self.lay_frm_documento.setHorizontalSpacing(33)
        self.lay_frm_documento.setObjectName("lay_frm_documento")
        self.lbl_documento = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_documento.setObjectName("lbl_documento")
        self.lay_frm_documento.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_documento)
        self.txt_documento = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_documento.setObjectName("txt_documento")
        self.lay_frm_documento.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_documento)
        self.btn_buscar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_buscar.setObjectName("btn_buscar")
        self.lay_frm_documento.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btn_buscar)
        self.lay_ver_principal.addLayout(self.lay_frm_documento)
        self.lay_frm_datos = QtWidgets.QFormLayout()
        self.lay_frm_datos.setObjectName("lay_frm_datos")
        self.lbl_nombre_completo = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_nombre_completo.setObjectName("lbl_nombre_completo")
        self.lay_frm_datos.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_nombre_completo)
        self.txt_nombre_completo = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_nombre_completo.setReadOnly(True)
        self.txt_nombre_completo.setObjectName("txt_nombre_completo")
        self.lay_frm_datos.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_nombre_completo)
        self.lbl_ahorros = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_ahorros.setObjectName("lbl_ahorros")
        self.lay_frm_datos.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_ahorros)
        self.txt_ahorros = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_ahorros.setReadOnly(True)
        self.txt_ahorros.setObjectName("txt_ahorros")
        self.lay_frm_datos.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_ahorros)
        self.lay_ver_principal.addLayout(self.lay_frm_datos)

        self.retranslateUi(BusquedaDatos)
        QtCore.QMetaObject.connectSlotsByName(BusquedaDatos)

    def retranslateUi(self, BusquedaDatos):
        _translate = QtCore.QCoreApplication.translate
        BusquedaDatos.setWindowTitle(_translate("BusquedaDatos", "Busqueda Datos"))
        self.lbl_documento.setText(_translate("BusquedaDatos", "Documento:"))
        self.btn_buscar.setText(_translate("BusquedaDatos", "Buscar"))
        self.lbl_nombre_completo.setText(_translate("BusquedaDatos", "Nombre completo:"))
        self.lbl_ahorros.setText(_translate("BusquedaDatos", "Ahorros:"))
