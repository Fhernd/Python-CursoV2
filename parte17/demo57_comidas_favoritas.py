# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo57_comidas_favoritas.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ComidaFavorita(object):
    def setupUi(self, ComidaFavorita):
        ComidaFavorita.setObjectName("ComidaFavorita")
        ComidaFavorita.resize(370, 270)
        ComidaFavorita.setMinimumSize(QtCore.QSize(370, 270))
        ComidaFavorita.setMaximumSize(QtCore.QSize(370, 270))
        self.verticalLayoutWidget = QtWidgets.QWidget(ComidaFavorita)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(4, 4, 361, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 10, 10, 0)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lay_frm_ingreso = QtWidgets.QFormLayout()
        self.lay_frm_ingreso.setObjectName("lay_frm_ingreso")
        self.lbl_nombre_comida_favorita = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_nombre_comida_favorita.setObjectName("lbl_nombre_comida_favorita")
        self.lay_frm_ingreso.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_nombre_comida_favorita)
        self.txt_nombre_comida_favorita = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_nombre_comida_favorita.setObjectName("txt_nombre_comida_favorita")
        self.lay_frm_ingreso.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_nombre_comida_favorita)
        self.btn_agregar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_agregar.setObjectName("btn_agregar")
        self.lay_frm_ingreso.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btn_agregar)
        self.lay_ver_principal.addLayout(self.lay_frm_ingreso)
        self.lst_comidas_favoritas = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.lst_comidas_favoritas.setObjectName("lst_comidas_favoritas")
        self.lay_ver_principal.addWidget(self.lst_comidas_favoritas)

        self.retranslateUi(ComidaFavorita)
        QtCore.QMetaObject.connectSlotsByName(ComidaFavorita)

    def retranslateUi(self, ComidaFavorita):
        _translate = QtCore.QCoreApplication.translate
        ComidaFavorita.setWindowTitle(_translate("ComidaFavorita", "Comidas Favoritas"))
        self.lbl_nombre_comida_favorita.setText(_translate("ComidaFavorita", "Nombre comida favorita:"))
        self.btn_agregar.setText(_translate("ComidaFavorita", "Agregar"))
