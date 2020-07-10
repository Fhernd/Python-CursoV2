# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo58_editor_comidas_favoritas.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ComidasFavoritasEditor(object):
    def setupUi(self, ComidasFavoritasEditor):
        ComidasFavoritasEditor.setObjectName("ComidasFavoritasEditor")
        ComidasFavoritasEditor.resize(480, 310)
        ComidasFavoritasEditor.setMinimumSize(QtCore.QSize(480, 310))
        ComidasFavoritasEditor.setMaximumSize(QtCore.QSize(480, 310))
        self.verticalLayoutWidget = QtWidgets.QWidget(ComidasFavoritasEditor)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(4, 5, 471, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 10, 10, 0)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lay_frm_captura_datos = QtWidgets.QFormLayout()
        self.lay_frm_captura_datos.setObjectName("lay_frm_captura_datos")
        self.lbl_nombre_comida_favorita = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_nombre_comida_favorita.setObjectName("lbl_nombre_comida_favorita")
        self.lay_frm_captura_datos.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_nombre_comida_favorita)
        self.txt_nombre_comida_favorita = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_nombre_comida_favorita.setObjectName("txt_nombre_comida_favorita")
        self.lay_frm_captura_datos.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_nombre_comida_favorita)
        self.btn_agregar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_agregar.setObjectName("btn_agregar")
        self.lay_frm_captura_datos.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btn_agregar)
        self.lay_ver_principal.addLayout(self.lay_frm_captura_datos)
        self.lst_comidas_favoritas = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.lst_comidas_favoritas.setObjectName("lst_comidas_favoritas")
        self.lay_ver_principal.addWidget(self.lst_comidas_favoritas)
        self.lay_hor_operaciones = QtWidgets.QHBoxLayout()
        self.lay_hor_operaciones.setObjectName("lay_hor_operaciones")
        self.btn_editar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_editar.setEnabled(False)
        self.btn_editar.setObjectName("btn_editar")
        self.lay_hor_operaciones.addWidget(self.btn_editar)
        self.btn_eliminar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_eliminar.setEnabled(False)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.lay_hor_operaciones.addWidget(self.btn_eliminar)
        self.btn_eliminar_todos = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_eliminar_todos.setEnabled(False)
        self.btn_eliminar_todos.setObjectName("btn_eliminar_todos")
        self.lay_hor_operaciones.addWidget(self.btn_eliminar_todos)
        self.lay_ver_principal.addLayout(self.lay_hor_operaciones)

        self.retranslateUi(ComidasFavoritasEditor)
        QtCore.QMetaObject.connectSlotsByName(ComidasFavoritasEditor)

    def retranslateUi(self, ComidasFavoritasEditor):
        _translate = QtCore.QCoreApplication.translate
        ComidasFavoritasEditor.setWindowTitle(_translate("ComidasFavoritasEditor", "Editor Comidas Favoritas"))
        self.lbl_nombre_comida_favorita.setText(_translate("ComidasFavoritasEditor", "Nombre comida favorita:"))
        self.btn_agregar.setText(_translate("ComidasFavoritasEditor", "Agregar"))
        self.btn_editar.setText(_translate("ComidasFavoritasEditor", "Editar"))
        self.btn_eliminar.setText(_translate("ComidasFavoritasEditor", "Eliminar"))
        self.btn_eliminar_todos.setText(_translate("ComidasFavoritasEditor", "Eliminar Todos"))
