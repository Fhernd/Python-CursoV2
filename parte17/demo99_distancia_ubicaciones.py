# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo99_distancia_ubicaciones.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DistanciaUbicaciones(object):
    def setupUi(self, DistanciaUbicaciones):
        DistanciaUbicaciones.setObjectName("DistanciaUbicaciones")
        DistanciaUbicaciones.resize(319, 209)
        DistanciaUbicaciones.setMinimumSize(QtCore.QSize(319, 209))
        DistanciaUbicaciones.setMaximumSize(QtCore.QSize(319, 209))
        self.wdg_principal = QtWidgets.QWidget(DistanciaUbicaciones)
        self.wdg_principal.setObjectName("wdg_principal")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.wdg_principal)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 30, 10, 0)
        self.lay_ver_principal.setSpacing(10)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lay_frm_datos = QtWidgets.QFormLayout()
        self.lay_frm_datos.setObjectName("lay_frm_datos")
        self.lbl_primera_ubicacion = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_primera_ubicacion.setObjectName("lbl_primera_ubicacion")
        self.lay_frm_datos.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_primera_ubicacion)
        self.txt_primera_ubicacion = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_primera_ubicacion.setObjectName("txt_primera_ubicacion")
        self.lay_frm_datos.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_primera_ubicacion)
        self.lbl_segunda_ubicacion = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_segunda_ubicacion.setObjectName("lbl_segunda_ubicacion")
        self.lay_frm_datos.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_segunda_ubicacion)
        self.txt_segunda_ubicacion = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_segunda_ubicacion.setObjectName("txt_segunda_ubicacion")
        self.lay_frm_datos.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_segunda_ubicacion)
        self.btn_calcular = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_calcular.setObjectName("btn_calcular")
        self.lay_frm_datos.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btn_calcular)
        self.lay_ver_principal.addLayout(self.lay_frm_datos)
        self.lay_frm_resultado = QtWidgets.QFormLayout()
        self.lay_frm_resultado.setHorizontalSpacing(56)
        self.lay_frm_resultado.setObjectName("lay_frm_resultado")
        self.lbl_distancia = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_distancia.setObjectName("lbl_distancia")
        self.lay_frm_resultado.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_distancia)
        self.txt_distancia = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_distancia.setReadOnly(True)
        self.txt_distancia.setObjectName("txt_distancia")
        self.lay_frm_resultado.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_distancia)
        self.lay_ver_principal.addLayout(self.lay_frm_resultado)
        DistanciaUbicaciones.setCentralWidget(self.wdg_principal)
        self.mbr_principal = QtWidgets.QMenuBar(DistanciaUbicaciones)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 319, 21))
        self.mbr_principal.setObjectName("mbr_principal")
        DistanciaUbicaciones.setMenuBar(self.mbr_principal)
        self.stt_principal = QtWidgets.QStatusBar(DistanciaUbicaciones)
        self.stt_principal.setObjectName("stt_principal")
        DistanciaUbicaciones.setStatusBar(self.stt_principal)

        self.retranslateUi(DistanciaUbicaciones)
        QtCore.QMetaObject.connectSlotsByName(DistanciaUbicaciones)

    def retranslateUi(self, DistanciaUbicaciones):
        _translate = QtCore.QCoreApplication.translate
        DistanciaUbicaciones.setWindowTitle(_translate("DistanciaUbicaciones", "Distancia entre Dos Ubicaciones"))
        self.lbl_primera_ubicacion.setText(_translate("DistanciaUbicaciones", "Primera ubicación:"))
        self.lbl_segunda_ubicacion.setText(_translate("DistanciaUbicaciones", "Segunda ubicación:"))
        self.btn_calcular.setText(_translate("DistanciaUbicaciones", "Calcular"))
        self.lbl_distancia.setText(_translate("DistanciaUbicaciones", "Distancia:"))
