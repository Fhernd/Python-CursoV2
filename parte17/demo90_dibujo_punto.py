# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo90_dibujo_punto.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DibujoPunto(object):
    def setupUi(self, DibujoPunto):
        DibujoPunto.setObjectName("DibujoPunto")
        DibujoPunto.resize(640, 480)
        self.wdg_principal = QtWidgets.QWidget(DibujoPunto)
        self.wdg_principal.setObjectName("wdg_principal")
        self.lbl_indicacion = QtWidgets.QLabel(self.wdg_principal)
        self.lbl_indicacion.setGeometry(QtCore.QRect(10, 10, 351, 16))
        self.lbl_indicacion.setObjectName("lbl_indicacion")
        DibujoPunto.setCentralWidget(self.wdg_principal)
        self.mbr_principal = QtWidgets.QMenuBar(DibujoPunto)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.mbr_principal.setObjectName("mbr_principal")
        DibujoPunto.setMenuBar(self.mbr_principal)
        self.stt_principal = QtWidgets.QStatusBar(DibujoPunto)
        self.stt_principal.setObjectName("stt_principal")
        DibujoPunto.setStatusBar(self.stt_principal)

        self.retranslateUi(DibujoPunto)
        QtCore.QMetaObject.connectSlotsByName(DibujoPunto)

    def retranslateUi(self, DibujoPunto):
        _translate = QtCore.QCoreApplication.translate
        DibujoPunto.setWindowTitle(_translate("DibujoPunto", "Dibujar Puntos"))
        self.lbl_indicacion.setText(_translate("DibujoPunto", "Haga click en cualquier región de esta ventana para dibujar un punto."))
