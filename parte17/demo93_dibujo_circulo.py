# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo93_dibujo_circulo.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DibujoCirculo(object):
    def setupUi(self, DibujoCirculo):
        DibujoCirculo.setObjectName("DibujoCirculo")
        DibujoCirculo.resize(640, 480)
        self.wdg_principal = QtWidgets.QWidget(DibujoCirculo)
        self.wdg_principal.setObjectName("wdg_principal")
        self.lbl_indicacion = QtWidgets.QLabel(self.wdg_principal)
        self.lbl_indicacion.setGeometry(QtCore.QRect(10, 10, 461, 16))
        self.lbl_indicacion.setObjectName("lbl_indicacion")
        DibujoCirculo.setCentralWidget(self.wdg_principal)
        self.mbr_principal = QtWidgets.QMenuBar(DibujoCirculo)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.mbr_principal.setObjectName("mbr_principal")
        DibujoCirculo.setMenuBar(self.mbr_principal)
        self.stt_principal = QtWidgets.QStatusBar(DibujoCirculo)
        self.stt_principal.setObjectName("stt_principal")
        DibujoCirculo.setStatusBar(self.stt_principal)

        self.retranslateUi(DibujoCirculo)
        QtCore.QMetaObject.connectSlotsByName(DibujoCirculo)

    def retranslateUi(self, DibujoCirculo):
        _translate = QtCore.QCoreApplication.translate
        DibujoCirculo.setWindowTitle(_translate("DibujoCirculo", "Dibujo Círculo"))
        self.lbl_indicacion.setText(_translate("DibujoCirculo", "Click en un punto específico y arrastre el mouse hasta otra ubicación para dibujar un círculo."))
