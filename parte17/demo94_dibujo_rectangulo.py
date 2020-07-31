# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo94_dibujo_rectangulo.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DibujoRectangulo(object):
    def setupUi(self, DibujoRectangulo):
        DibujoRectangulo.setObjectName("DibujoRectangulo")
        DibujoRectangulo.resize(640, 480)
        self.wdg_principal = QtWidgets.QWidget(DibujoRectangulo)
        self.wdg_principal.setObjectName("wdg_principal")
        self.lbl_indicacion = QtWidgets.QLabel(self.wdg_principal)
        self.lbl_indicacion.setGeometry(QtCore.QRect(20, 10, 481, 16))
        self.lbl_indicacion.setObjectName("lbl_indicacion")
        DibujoRectangulo.setCentralWidget(self.wdg_principal)
        self.mbr_principal = QtWidgets.QMenuBar(DibujoRectangulo)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.mbr_principal.setObjectName("mbr_principal")
        DibujoRectangulo.setMenuBar(self.mbr_principal)
        self.stt_principal = QtWidgets.QStatusBar(DibujoRectangulo)
        self.stt_principal.setObjectName("stt_principal")
        DibujoRectangulo.setStatusBar(self.stt_principal)

        self.retranslateUi(DibujoRectangulo)
        QtCore.QMetaObject.connectSlotsByName(DibujoRectangulo)

    def retranslateUi(self, DibujoRectangulo):
        _translate = QtCore.QCoreApplication.translate
        DibujoRectangulo.setWindowTitle(_translate("DibujoRectangulo", "Dibujo Rectángulo"))
        self.lbl_indicacion.setText(_translate("DibujoRectangulo", "Click en un punto específico y arrastre el mouse hasta otra ubicación para dibujar un rectángulo."))
