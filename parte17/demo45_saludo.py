# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo45_saludo.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SaludoVentana(object):
    def setupUi(self, SaludoVentana):
        SaludoVentana.setObjectName("SaludoVentana")
        SaludoVentana.resize(320, 137)
        self.wdg_principal = QtWidgets.QWidget(SaludoVentana)
        self.wdg_principal.setObjectName("wdg_principal")
        self.lbl_nombre = QtWidgets.QLabel(self.wdg_principal)
        self.lbl_nombre.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.txt_nombre = QtWidgets.QLineEdit(self.wdg_principal)
        self.txt_nombre.setGeometry(QtCore.QRect(120, 10, 191, 20))
        self.txt_nombre.setObjectName("txt_nombre")
        self.btn_saludar = QtWidgets.QPushButton(self.wdg_principal)
        self.btn_saludar.setGeometry(QtCore.QRect(120, 40, 191, 23))
        self.btn_saludar.setObjectName("btn_saludar")
        SaludoVentana.setCentralWidget(self.wdg_principal)
        self.mbr_principal = QtWidgets.QMenuBar(SaludoVentana)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.mbr_principal.setObjectName("mbr_principal")
        SaludoVentana.setMenuBar(self.mbr_principal)
        self.stb_principal = QtWidgets.QStatusBar(SaludoVentana)
        self.stb_principal.setObjectName("stb_principal")
        SaludoVentana.setStatusBar(self.stb_principal)

        self.retranslateUi(SaludoVentana)
        QtCore.QMetaObject.connectSlotsByName(SaludoVentana)

    def retranslateUi(self, SaludoVentana):
        _translate = QtCore.QCoreApplication.translate
        SaludoVentana.setWindowTitle(_translate("SaludoVentana", "Saludo"))
        self.lbl_nombre.setText(_translate("SaludoVentana", "Escriba su nombre:"))
        self.btn_saludar.setText(_translate("SaludoVentana", "Saludar"))
