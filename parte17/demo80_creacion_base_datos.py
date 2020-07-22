# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo80_creacion_base_datos.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreacionBaseDatos(object):
    def setupUi(self, CreacionBaseDatos):
        CreacionBaseDatos.setObjectName("CreacionBaseDatos")
        CreacionBaseDatos.resize(320, 160)
        CreacionBaseDatos.setMinimumSize(QtCore.QSize(320, 160))
        CreacionBaseDatos.setMaximumSize(QtCore.QSize(320, 160))
        self.verticalLayoutWidget = QtWidgets.QWidget(CreacionBaseDatos)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 10, 10, 0)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lay_frm_entrada = QtWidgets.QFormLayout()
        self.lay_frm_entrada.setObjectName("lay_frm_entrada")
        self.lbl_nombre_base_datos = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_nombre_base_datos.setObjectName("lbl_nombre_base_datos")
        self.lay_frm_entrada.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_nombre_base_datos)
        self.txt_nombre_base_datos = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_nombre_base_datos.setObjectName("txt_nombre_base_datos")
        self.lay_frm_entrada.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_nombre_base_datos)
        self.btn_crear_base_datos = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_crear_base_datos.setObjectName("btn_crear_base_datos")
        self.lay_frm_entrada.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btn_crear_base_datos)
        self.lay_ver_principal.addLayout(self.lay_frm_entrada)
        self.lbl_resultado = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_resultado.setObjectName("lbl_resultado")
        self.lay_ver_principal.addWidget(self.lbl_resultado)

        self.retranslateUi(CreacionBaseDatos)
        QtCore.QMetaObject.connectSlotsByName(CreacionBaseDatos)

    def retranslateUi(self, CreacionBaseDatos):
        _translate = QtCore.QCoreApplication.translate
        CreacionBaseDatos.setWindowTitle(_translate("CreacionBaseDatos", "Creación Base Datos"))
        self.lbl_nombre_base_datos.setText(_translate("CreacionBaseDatos", "Nombre de la base de datos:"))
        self.btn_crear_base_datos.setText(_translate("CreacionBaseDatos", "Crear base de datos"))
        self.lbl_resultado.setText(_translate("CreacionBaseDatos", "Resultado:"))
