# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo82_insercion_registros.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InsercionRegistros(object):
    def setupUi(self, InsercionRegistros):
        InsercionRegistros.setObjectName("InsercionRegistros")
        InsercionRegistros.resize(320, 225)
        InsercionRegistros.setMinimumSize(QtCore.QSize(320, 225))
        InsercionRegistros.setMaximumSize(QtCore.QSize(320, 225))
        self.verticalLayoutWidget = QtWidgets.QWidget(InsercionRegistros)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 10, 10, 0)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lay_frm_base_datos = QtWidgets.QFormLayout()
        self.lay_frm_base_datos.setObjectName("lay_frm_base_datos")
        self.lbl_nombre_base_datos = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_nombre_base_datos.setObjectName("lbl_nombre_base_datos")
        self.lay_frm_base_datos.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_nombre_base_datos)
        self.txt_nombre_base_datos = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_nombre_base_datos.setObjectName("txt_nombre_base_datos")
        self.lay_frm_base_datos.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_nombre_base_datos)
        self.btn_conectar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_conectar.setObjectName("btn_conectar")
        self.lay_frm_base_datos.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btn_conectar)
        self.lay_ver_principal.addLayout(self.lay_frm_base_datos)
        self.lay_frm_registro = QtWidgets.QFormLayout()
        self.lay_frm_registro.setHorizontalSpacing(57)
        self.lay_frm_registro.setObjectName("lay_frm_registro")
        self.lbl_nombre_tabla = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_nombre_tabla.setObjectName("lbl_nombre_tabla")
        self.lay_frm_registro.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_nombre_tabla)
        self.txt_nombre_tabla = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_nombre_tabla.setReadOnly(True)
        self.txt_nombre_tabla.setObjectName("txt_nombre_tabla")
        self.lay_frm_registro.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_nombre_tabla)
        self.lbl_documento = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_documento.setObjectName("lbl_documento")
        self.lay_frm_registro.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_documento)
        self.txt_documento = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_documento.setReadOnly(True)
        self.txt_documento.setObjectName("txt_documento")
        self.lay_frm_registro.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_documento)
        self.lbl_nombre_completo = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_nombre_completo.setObjectName("lbl_nombre_completo")
        self.lay_frm_registro.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_nombre_completo)
        self.txt_nombre_completo = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_nombre_completo.setReadOnly(True)
        self.txt_nombre_completo.setObjectName("txt_nombre_completo")
        self.lay_frm_registro.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_nombre_completo)
        self.lbl_ahorros = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_ahorros.setObjectName("lbl_ahorros")
        self.lay_frm_registro.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_ahorros)
        self.txt_ahorros = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_ahorros.setReadOnly(True)
        self.txt_ahorros.setObjectName("txt_ahorros")
        self.lay_frm_registro.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_ahorros)
        self.btn_insertar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_insertar.setEnabled(False)
        self.btn_insertar.setObjectName("btn_insertar")
        self.lay_frm_registro.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.btn_insertar)
        self.lay_ver_principal.addLayout(self.lay_frm_registro)

        self.retranslateUi(InsercionRegistros)
        QtCore.QMetaObject.connectSlotsByName(InsercionRegistros)

    def retranslateUi(self, InsercionRegistros):
        _translate = QtCore.QCoreApplication.translate
        InsercionRegistros.setWindowTitle(_translate("InsercionRegistros", "Inserción Registros"))
        self.lbl_nombre_base_datos.setText(_translate("InsercionRegistros", "Nombre de la base de datos:"))
        self.btn_conectar.setText(_translate("InsercionRegistros", "Conectar"))
        self.lbl_nombre_tabla.setText(_translate("InsercionRegistros", "Nombre tabla:"))
        self.lbl_documento.setText(_translate("InsercionRegistros", "Documento:"))
        self.lbl_nombre_completo.setText(_translate("InsercionRegistros", "Nombre completo:"))
        self.lbl_ahorros.setText(_translate("InsercionRegistros", "Ahorros"))
        self.btn_insertar.setText(_translate("InsercionRegistros", "Insertar"))
