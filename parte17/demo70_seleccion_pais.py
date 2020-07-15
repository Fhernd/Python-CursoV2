# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo70_seleccion_pais.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SeleccionPais(object):
    def setupUi(self, SeleccionPais):
        SeleccionPais.setObjectName("SeleccionPais")
        SeleccionPais.resize(510, 150)
        SeleccionPais.setMinimumSize(QtCore.QSize(510, 150))
        SeleccionPais.setMaximumSize(QtCore.QSize(510, 150))
        self.horizontalLayoutWidget = QtWidgets.QWidget(SeleccionPais)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(3, 3, 501, 141))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.lay_hor_principal = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.lay_hor_principal.setContentsMargins(10, 0, 10, 0)
        self.lay_hor_principal.setObjectName("lay_hor_principal")
        self.lbl_seleccion_pais = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_seleccion_pais.setObjectName("lbl_seleccion_pais")
        self.lay_hor_principal.addWidget(self.lbl_seleccion_pais)
        self.txt_pais_seleccionado = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.txt_pais_seleccionado.setReadOnly(True)
        self.txt_pais_seleccionado.setObjectName("txt_pais_seleccionado")
        self.lay_hor_principal.addWidget(self.txt_pais_seleccionado)
        self.btn_seleccion_pais = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_seleccion_pais.setObjectName("btn_seleccion_pais")
        self.lay_hor_principal.addWidget(self.btn_seleccion_pais)

        self.retranslateUi(SeleccionPais)
        QtCore.QMetaObject.connectSlotsByName(SeleccionPais)

    def retranslateUi(self, SeleccionPais):
        _translate = QtCore.QCoreApplication.translate
        SeleccionPais.setWindowTitle(_translate("SeleccionPais", "Selección País"))
        self.lbl_seleccion_pais.setText(_translate("SeleccionPais", "Seleccione su país:"))
        self.btn_seleccion_pais.setText(_translate("SeleccionPais", "Seleccionar país..."))
