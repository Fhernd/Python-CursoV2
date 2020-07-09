# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo52_calculadora.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculadora(object):
    def setupUi(self, Calculadora):
        Calculadora.setObjectName("Calculadora")
        Calculadora.resize(333, 184)
        self.wdg_principal = QtWidgets.QWidget(Calculadora)
        self.wdg_principal.setObjectName("wdg_principal")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.wdg_principal)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 330, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(5, 10, 5, 0)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lay_frm_numeros = QtWidgets.QFormLayout()
        self.lay_frm_numeros.setObjectName("lay_frm_numeros")
        self.lbl_primer_numero = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_primer_numero.setObjectName("lbl_primer_numero")
        self.lay_frm_numeros.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_primer_numero)
        self.txt_primer_numero = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_primer_numero.setObjectName("txt_primer_numero")
        self.lay_frm_numeros.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_primer_numero)
        self.lbl_segundo_numero = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_segundo_numero.setObjectName("lbl_segundo_numero")
        self.lay_frm_numeros.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_segundo_numero)
        self.txt_segundo_numero = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_segundo_numero.setObjectName("txt_segundo_numero")
        self.lay_frm_numeros.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_segundo_numero)
        self.lay_ver_principal.addLayout(self.lay_frm_numeros)
        self.lay_hor_operaciones = QtWidgets.QHBoxLayout()
        self.lay_hor_operaciones.setObjectName("lay_hor_operaciones")
        self.btn_sumar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_sumar.setObjectName("btn_sumar")
        self.lay_hor_operaciones.addWidget(self.btn_sumar)
        self.btn_restar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_restar.setObjectName("btn_restar")
        self.lay_hor_operaciones.addWidget(self.btn_restar)
        self.btn_multiplicar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_multiplicar.setObjectName("btn_multiplicar")
        self.lay_hor_operaciones.addWidget(self.btn_multiplicar)
        self.btn_dividir = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_dividir.setObjectName("btn_dividir")
        self.lay_hor_operaciones.addWidget(self.btn_dividir)
        self.lay_ver_principal.addLayout(self.lay_hor_operaciones)
        self.lbl_resultado = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_resultado.setText("")
        self.lbl_resultado.setObjectName("lbl_resultado")
        self.lay_ver_principal.addWidget(self.lbl_resultado)
        self.lay_ver_principal.setStretch(0, 2)
        self.lay_ver_principal.setStretch(1, 1)
        self.lay_ver_principal.setStretch(2, 1)
        Calculadora.setCentralWidget(self.wdg_principal)
        self.mbr_principal = QtWidgets.QMenuBar(Calculadora)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 333, 21))
        self.mbr_principal.setObjectName("mbr_principal")
        Calculadora.setMenuBar(self.mbr_principal)
        self.stt_principal = QtWidgets.QStatusBar(Calculadora)
        self.stt_principal.setObjectName("stt_principal")
        Calculadora.setStatusBar(self.stt_principal)

        self.retranslateUi(Calculadora)
        QtCore.QMetaObject.connectSlotsByName(Calculadora)

    def retranslateUi(self, Calculadora):
        _translate = QtCore.QCoreApplication.translate
        Calculadora.setWindowTitle(_translate("Calculadora", "Calculadora"))
        self.lbl_primer_numero.setText(_translate("Calculadora", "Ingrese primer número:"))
        self.lbl_segundo_numero.setText(_translate("Calculadora", "Ingrese segundo número:"))
        self.btn_sumar.setText(_translate("Calculadora", "+"))
        self.btn_restar.setText(_translate("Calculadora", "-"))
        self.btn_multiplicar.setText(_translate("Calculadora", "*"))
        self.btn_dividir.setText(_translate("Calculadora", "/"))
