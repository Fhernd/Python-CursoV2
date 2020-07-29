# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo89_posicion_puntero_mouse.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        VentanaPrincipal.setObjectName("VentanaPrincipal")
        VentanaPrincipal.resize(480, 400)
        self.wdg_principal = QtWidgets.QWidget(VentanaPrincipal)
        self.wdg_principal.setObjectName("wdg_principal")
        VentanaPrincipal.setCentralWidget(self.wdg_principal)
        self.mbr_principal = QtWidgets.QMenuBar(VentanaPrincipal)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.mbr_principal.setObjectName("mbr_principal")
        VentanaPrincipal.setMenuBar(self.mbr_principal)
        self.stt_principal = QtWidgets.QStatusBar(VentanaPrincipal)
        self.stt_principal.setObjectName("stt_principal")
        VentanaPrincipal.setStatusBar(self.stt_principal)

        self.retranslateUi(VentanaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(VentanaPrincipal)

    def retranslateUi(self, VentanaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        VentanaPrincipal.setWindowTitle(_translate("VentanaPrincipal", "Coordenadas Puntero del Mouse"))
