# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo44_calculadora_basica.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalculadoraBasicaVentana(object):
    def setupUi(self, CalculadoraBasicaVentana):
        CalculadoraBasicaVentana.setObjectName("CalculadoraBasicaVentana")
        CalculadoraBasicaVentana.resize(320, 185)
        self.wdg_principal = QtWidgets.QWidget(CalculadoraBasicaVentana)
        self.wdg_principal.setObjectName("wdg_principal")
        self.lbl_numero_1 = QtWidgets.QLabel(self.wdg_principal)
        self.lbl_numero_1.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.lbl_numero_1.setObjectName("lbl_numero_1")
        self.txt_numero_1 = QtWidgets.QLineEdit(self.wdg_principal)
        self.txt_numero_1.setGeometry(QtCore.QRect(126, 19, 181, 20))
        self.txt_numero_1.setObjectName("txt_numero_1")
        self.lbl_numero_2 = QtWidgets.QLabel(self.wdg_principal)
        self.lbl_numero_2.setGeometry(QtCore.QRect(10, 47, 101, 16))
        self.lbl_numero_2.setObjectName("lbl_numero_2")
        self.txt_numero_2 = QtWidgets.QLineEdit(self.wdg_principal)
        self.txt_numero_2.setGeometry(QtCore.QRect(126, 45, 181, 20))
        self.txt_numero_2.setObjectName("txt_numero_2")
        self.btn_sumar = QtWidgets.QPushButton(self.wdg_principal)
        self.btn_sumar.setGeometry(QtCore.QRect(125, 70, 181, 23))
        self.btn_sumar.setObjectName("btn_sumar")
        self.lbl_resultado = QtWidgets.QLabel(self.wdg_principal)
        self.lbl_resultado.setGeometry(QtCore.QRect(10, 115, 101, 16))
        self.lbl_resultado.setObjectName("lbl_resultado")
        self.txt_resultado = QtWidgets.QLineEdit(self.wdg_principal)
        self.txt_resultado.setGeometry(QtCore.QRect(127, 112, 181, 20))
        self.txt_resultado.setReadOnly(True)
        self.txt_resultado.setObjectName("txt_resultado")
        CalculadoraBasicaVentana.setCentralWidget(self.wdg_principal)
        self.mbr_principal = QtWidgets.QMenuBar(CalculadoraBasicaVentana)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.mbr_principal.setObjectName("mbr_principal")
        CalculadoraBasicaVentana.setMenuBar(self.mbr_principal)
        self.str_principal = QtWidgets.QStatusBar(CalculadoraBasicaVentana)
        self.str_principal.setObjectName("str_principal")
        CalculadoraBasicaVentana.setStatusBar(self.str_principal)

        self.retranslateUi(CalculadoraBasicaVentana)
        QtCore.QMetaObject.connectSlotsByName(CalculadoraBasicaVentana)

    def retranslateUi(self, CalculadoraBasicaVentana):
        _translate = QtCore.QCoreApplication.translate
        CalculadoraBasicaVentana.setWindowTitle(_translate("CalculadoraBasicaVentana", "Calculadora Básica"))
        self.lbl_numero_1.setText(_translate("CalculadoraBasicaVentana", "Número 1:"))
        self.lbl_numero_2.setText(_translate("CalculadoraBasicaVentana", "Número 2:"))
        self.btn_sumar.setText(_translate("CalculadoraBasicaVentana", "Sumar"))
        self.lbl_resultado.setText(_translate("CalculadoraBasicaVentana", "Resultado:"))
