# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo68_registro_estudiante.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegistroEstudiante(object):
    def setupUi(self, RegistroEstudiante):
        RegistroEstudiante.setObjectName("RegistroEstudiante")
        RegistroEstudiante.resize(320, 182)
        RegistroEstudiante.setMinimumSize(QtCore.QSize(320, 182))
        RegistroEstudiante.setMaximumSize(QtCore.QSize(320, 182))
        self.formLayoutWidget = QtWidgets.QWidget(RegistroEstudiante)
        self.formLayoutWidget.setGeometry(QtCore.QRect(4, 4, 311, 171))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.lay_frm_principal = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.lay_frm_principal.setContentsMargins(10, 5, 10, 0)
        self.lay_frm_principal.setObjectName("lay_frm_principal")
        self.lbl_identidad = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_identidad.setObjectName("lbl_identidad")
        self.lay_frm_principal.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_identidad)
        self.txt_identidad = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_identidad.setObjectName("txt_identidad")
        self.lay_frm_principal.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_identidad)
        self.lbl_nombre_completo = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_nombre_completo.setObjectName("lbl_nombre_completo")
        self.lay_frm_principal.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_nombre_completo)
        self.txt_nombre_completo = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_nombre_completo.setObjectName("txt_nombre_completo")
        self.lay_frm_principal.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_nombre_completo)
        self.lbl_telefono = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_telefono.setObjectName("lbl_telefono")
        self.lay_frm_principal.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_telefono)
        self.txt_telefono = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_telefono.setObjectName("txt_telefono")
        self.lay_frm_principal.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_telefono)
        self.lbl_carnet = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_carnet.setObjectName("lbl_carnet")
        self.lay_frm_principal.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_carnet)
        self.txt_carnet = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_carnet.setObjectName("txt_carnet")
        self.lay_frm_principal.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_carnet)
        self.lbl_carrera = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_carrera.setObjectName("lbl_carrera")
        self.lay_frm_principal.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_carrera)
        self.cbx_carreras = QtWidgets.QComboBox(self.formLayoutWidget)
        self.cbx_carreras.setObjectName("cbx_carreras")
        self.cbx_carreras.addItem("")
        self.cbx_carreras.addItem("")
        self.cbx_carreras.addItem("")
        self.cbx_carreras.addItem("")
        self.cbx_carreras.addItem("")
        self.cbx_carreras.addItem("")
        self.lay_frm_principal.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cbx_carreras)
        self.btn_registrar = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_registrar.setObjectName("btn_registrar")
        self.lay_frm_principal.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.btn_registrar)

        self.retranslateUi(RegistroEstudiante)
        QtCore.QMetaObject.connectSlotsByName(RegistroEstudiante)

    def retranslateUi(self, RegistroEstudiante):
        _translate = QtCore.QCoreApplication.translate
        RegistroEstudiante.setWindowTitle(_translate("RegistroEstudiante", "Registro Estudiante"))
        self.lbl_identidad.setText(_translate("RegistroEstudiante", "Identidad:"))
        self.lbl_nombre_completo.setText(_translate("RegistroEstudiante", "Nombre completo:"))
        self.lbl_telefono.setText(_translate("RegistroEstudiante", "Teléfono:"))
        self.lbl_carnet.setText(_translate("RegistroEstudiante", "Carnet:"))
        self.lbl_carrera.setText(_translate("RegistroEstudiante", "Carrera:"))
        self.cbx_carreras.setItemText(0, _translate("RegistroEstudiante", "Sistemas"))
        self.cbx_carreras.setItemText(1, _translate("RegistroEstudiante", "Civil"))
        self.cbx_carreras.setItemText(2, _translate("RegistroEstudiante", "Industrial"))
        self.cbx_carreras.setItemText(3, _translate("RegistroEstudiante", "Psicología"))
        self.cbx_carreras.setItemText(4, _translate("RegistroEstudiante", "Biología"))
        self.cbx_carreras.setItemText(5, _translate("RegistroEstudiante", "Medicina"))
        self.btn_registrar.setText(_translate("RegistroEstudiante", "Registrar"))
