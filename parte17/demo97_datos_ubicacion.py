# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo97_datos_ubicacion.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DatosUbicacion(object):
    def setupUi(self, DatosUbicacion):
        DatosUbicacion.setObjectName("DatosUbicacion")
        DatosUbicacion.resize(362, 235)
        DatosUbicacion.setMinimumSize(QtCore.QSize(362, 235))
        DatosUbicacion.setMaximumSize(QtCore.QSize(362, 235))
        self.wdg_principal = QtWidgets.QWidget(DatosUbicacion)
        self.wdg_principal.setObjectName("wdg_principal")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.wdg_principal)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 361, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 10, 10, 0)
        self.lay_ver_principal.setSpacing(10)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lay_frm_datos = QtWidgets.QFormLayout()
        self.lay_frm_datos.setHorizontalSpacing(54)
        self.lay_frm_datos.setObjectName("lay_frm_datos")
        self.lbl_nombre_ubicacion = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_nombre_ubicacion.setObjectName("lbl_nombre_ubicacion")
        self.lay_frm_datos.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_nombre_ubicacion)
        self.txt_nombre_ubicacion = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_nombre_ubicacion.setObjectName("txt_nombre_ubicacion")
        self.lay_frm_datos.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_nombre_ubicacion)
        self.btn_buscar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_buscar.setObjectName("btn_buscar")
        self.lay_frm_datos.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btn_buscar)
        self.lay_ver_principal.addLayout(self.lay_frm_datos)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lbl_ciudad = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_ciudad.setObjectName("lbl_ciudad")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_ciudad)
        self.txt_ciudad = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_ciudad.setReadOnly(True)
        self.txt_ciudad.setObjectName("txt_ciudad")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_ciudad)
        self.lbl_nombre_completo_ubicacion = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_nombre_completo_ubicacion.setObjectName("lbl_nombre_completo_ubicacion")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_nombre_completo_ubicacion)
        self.txt_nombre_completo_ubicacion = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_nombre_completo_ubicacion.setReadOnly(True)
        self.txt_nombre_completo_ubicacion.setObjectName("txt_nombre_completo_ubicacion")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_nombre_completo_ubicacion)
        self.lbl_latitud = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_latitud.setObjectName("lbl_latitud")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_latitud)
        self.txt_latitud = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_latitud.setReadOnly(True)
        self.txt_latitud.setObjectName("txt_latitud")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_latitud)
        self.lbl_longitud = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_longitud.setObjectName("lbl_longitud")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_longitud)
        self.txt_longitud = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_longitud.setReadOnly(True)
        self.txt_longitud.setObjectName("txt_longitud")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_longitud)
        self.lay_ver_principal.addLayout(self.formLayout)
        DatosUbicacion.setCentralWidget(self.wdg_principal)
        self.menubar = QtWidgets.QMenuBar(DatosUbicacion)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 362, 21))
        self.menubar.setObjectName("menubar")
        DatosUbicacion.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DatosUbicacion)
        self.statusbar.setObjectName("statusbar")
        DatosUbicacion.setStatusBar(self.statusbar)

        self.retranslateUi(DatosUbicacion)
        QtCore.QMetaObject.connectSlotsByName(DatosUbicacion)

    def retranslateUi(self, DatosUbicacion):
        _translate = QtCore.QCoreApplication.translate
        DatosUbicacion.setWindowTitle(_translate("DatosUbicacion", "Datos Ubicación"))
        self.lbl_nombre_ubicacion.setText(_translate("DatosUbicacion", "Nombre ubicación:"))
        self.btn_buscar.setText(_translate("DatosUbicacion", "Buscar"))
        self.lbl_ciudad.setText(_translate("DatosUbicacion", "Ciudad:"))
        self.lbl_nombre_completo_ubicacion.setText(_translate("DatosUbicacion", "Nombre completo ubicación:"))
        self.lbl_latitud.setText(_translate("DatosUbicacion", "Latitud:"))
        self.lbl_longitud.setText(_translate("DatosUbicacion", "Longitud:"))
