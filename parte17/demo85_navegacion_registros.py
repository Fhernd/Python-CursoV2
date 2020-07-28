# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo85_navegacion_registros.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NavegacionRegistros(object):
    def setupUi(self, NavegacionRegistros):
        NavegacionRegistros.setObjectName("NavegacionRegistros")
        NavegacionRegistros.resize(420, 200)
        NavegacionRegistros.setMinimumSize(QtCore.QSize(420, 200))
        NavegacionRegistros.setMaximumSize(QtCore.QSize(420, 200))
        self.verticalLayoutWidget = QtWidgets.QWidget(NavegacionRegistros)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 431, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 20, 20, 40)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lay_frm_datos = QtWidgets.QFormLayout()
        self.lay_frm_datos.setObjectName("lay_frm_datos")
        self.lbl_documento = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_documento.setObjectName("lbl_documento")
        self.lay_frm_datos.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_documento)
        self.txt_documento = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_documento.setReadOnly(True)
        self.txt_documento.setObjectName("txt_documento")
        self.lay_frm_datos.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_documento)
        self.lbl_nombre_completo = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_nombre_completo.setObjectName("lbl_nombre_completo")
        self.lay_frm_datos.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_nombre_completo)
        self.txt_nombre_completo = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_nombre_completo.setReadOnly(True)
        self.txt_nombre_completo.setObjectName("txt_nombre_completo")
        self.lay_frm_datos.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_nombre_completo)
        self.lbl_ahorros = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_ahorros.setObjectName("lbl_ahorros")
        self.lay_frm_datos.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_ahorros)
        self.txt_ahorros = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_ahorros.setReadOnly(True)
        self.txt_ahorros.setObjectName("txt_ahorros")
        self.lay_frm_datos.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_ahorros)
        self.lay_ver_principal.addLayout(self.lay_frm_datos)
        self.lay_hor_botones = QtWidgets.QHBoxLayout()
        self.lay_hor_botones.setObjectName("lay_hor_botones")
        self.btn_primero = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_primero.setObjectName("btn_primero")
        self.lay_hor_botones.addWidget(self.btn_primero)
        self.btn_anterior = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_anterior.setObjectName("btn_anterior")
        self.lay_hor_botones.addWidget(self.btn_anterior)
        self.btn_siguiente = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_siguiente.setObjectName("btn_siguiente")
        self.lay_hor_botones.addWidget(self.btn_siguiente)
        self.btn_ultimo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_ultimo.setObjectName("btn_ultimo")
        self.lay_hor_botones.addWidget(self.btn_ultimo)
        self.lay_ver_principal.addLayout(self.lay_hor_botones)

        self.retranslateUi(NavegacionRegistros)
        QtCore.QMetaObject.connectSlotsByName(NavegacionRegistros)

    def retranslateUi(self, NavegacionRegistros):
        _translate = QtCore.QCoreApplication.translate
        NavegacionRegistros.setWindowTitle(_translate("NavegacionRegistros", "Navegación Registros"))
        self.lbl_documento.setText(_translate("NavegacionRegistros", "Documento:"))
        self.lbl_nombre_completo.setText(_translate("NavegacionRegistros", "Nombre completo:"))
        self.lbl_ahorros.setText(_translate("NavegacionRegistros", "Ahorros:"))
        self.btn_primero.setText(_translate("NavegacionRegistros", "Primero"))
        self.btn_anterior.setText(_translate("NavegacionRegistros", "Anterior"))
        self.btn_siguiente.setText(_translate("NavegacionRegistros", "Siguiente"))
        self.btn_ultimo.setText(_translate("NavegacionRegistros", "Último"))
