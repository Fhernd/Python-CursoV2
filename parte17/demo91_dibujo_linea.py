# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo91_dibujo_linea.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DibujoLinea(object):
    def setupUi(self, DibujoLinea):
        DibujoLinea.setObjectName("DibujoLinea")
        DibujoLinea.resize(640, 480)
        self.wdg_principal = QtWidgets.QWidget(DibujoLinea)
        self.wdg_principal.setObjectName("wdg_principal")
        self.lbl_indicacion = QtWidgets.QLabel(self.wdg_principal)
        self.lbl_indicacion.setGeometry(QtCore.QRect(10, 10, 371, 21))
        self.lbl_indicacion.setObjectName("lbl_indicacion")
        DibujoLinea.setCentralWidget(self.wdg_principal)
        self.mbr_principal = QtWidgets.QMenuBar(DibujoLinea)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.mbr_principal.setObjectName("mbr_principal")
        DibujoLinea.setMenuBar(self.mbr_principal)
        self.stt_principal = QtWidgets.QStatusBar(DibujoLinea)
        self.stt_principal.setObjectName("stt_principal")
        DibujoLinea.setStatusBar(self.stt_principal)

        self.retranslateUi(DibujoLinea)
        QtCore.QMetaObject.connectSlotsByName(DibujoLinea)

    def retranslateUi(self, DibujoLinea):
        _translate = QtCore.QCoreApplication.translate
        DibujoLinea.setWindowTitle(_translate("DibujoLinea", "Dibujo Línea"))
        self.lbl_indicacion.setText(_translate("DibujoLinea", "Dibuje una línea con el mouse indicando un punto de inicio y un punto final."))
