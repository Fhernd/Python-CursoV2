# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo62_gestor_descargas.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GestorDescargas(object):
    def setupUi(self, GestorDescargas):
        GestorDescargas.setObjectName("GestorDescargas")
        GestorDescargas.resize(320, 180)
        GestorDescargas.setMinimumSize(QtCore.QSize(320, 180))
        GestorDescargas.setMaximumSize(QtCore.QSize(320, 180))
        self.verticalLayoutWidget = QtWidgets.QWidget(GestorDescargas)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(4, 4, 311, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 0, 10, 0)
        self.lay_ver_principal.setSpacing(20)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lbl_titulo = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.lay_ver_principal.addWidget(self.lbl_titulo)
        self.pbr_descarga = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.pbr_descarga.setProperty("value", 0)
        self.pbr_descarga.setObjectName("pbr_descarga")
        self.lay_ver_principal.addWidget(self.pbr_descarga)
        self.btn_iniciar_descarga = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_iniciar_descarga.setObjectName("btn_iniciar_descarga")
        self.lay_ver_principal.addWidget(self.btn_iniciar_descarga)
        self.lay_ver_principal.setStretch(0, 1)
        self.lay_ver_principal.setStretch(1, 4)
        self.lay_ver_principal.setStretch(2, 1)

        self.retranslateUi(GestorDescargas)
        QtCore.QMetaObject.connectSlotsByName(GestorDescargas)

    def retranslateUi(self, GestorDescargas):
        _translate = QtCore.QCoreApplication.translate
        GestorDescargas.setWindowTitle(_translate("GestorDescargas", "Gestor de Descargas"))
        self.lbl_titulo.setText(_translate("GestorDescargas", "Gestor de Descargas"))
        self.btn_iniciar_descarga.setText(_translate("GestorDescargas", "Iniciar Descarga"))
