# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo96_animacion_objeto.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AnimacionObjeto(object):
    def setupUi(self, AnimacionObjeto):
        AnimacionObjeto.setObjectName("AnimacionObjeto")
        AnimacionObjeto.resize(480, 640)
        self.wdg_principal = QtWidgets.QWidget(AnimacionObjeto)
        self.wdg_principal.setObjectName("wdg_principal")
        self.btn_iniciar_animacion = QtWidgets.QPushButton(self.wdg_principal)
        self.btn_iniciar_animacion.setGeometry(QtCore.QRect(10, 10, 121, 23))
        self.btn_iniciar_animacion.setObjectName("btn_iniciar_animacion")
        self.lbl_imagen = QtWidgets.QLabel(self.wdg_principal)
        self.lbl_imagen.setGeometry(QtCore.QRect(190, 10, 96, 96))
        self.lbl_imagen.setText("")
        self.lbl_imagen.setObjectName("lbl_imagen")
        AnimacionObjeto.setCentralWidget(self.wdg_principal)
        self.mbr_principal = QtWidgets.QMenuBar(AnimacionObjeto)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.mbr_principal.setObjectName("mbr_principal")
        AnimacionObjeto.setMenuBar(self.mbr_principal)
        self.stt_principal = QtWidgets.QStatusBar(AnimacionObjeto)
        self.stt_principal.setObjectName("stt_principal")
        AnimacionObjeto.setStatusBar(self.stt_principal)

        self.retranslateUi(AnimacionObjeto)
        QtCore.QMetaObject.connectSlotsByName(AnimacionObjeto)

    def retranslateUi(self, AnimacionObjeto):
        _translate = QtCore.QCoreApplication.translate
        AnimacionObjeto.setWindowTitle(_translate("AnimacionObjeto", "Animación Objeto"))
        self.btn_iniciar_animacion.setText(_translate("AnimacionObjeto", "Iniciar animación"))
