# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo61_editor_texto.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditorTexto(object):
    def setupUi(self, EditorTexto):
        EditorTexto.setObjectName("EditorTexto")
        EditorTexto.resize(400, 240)
        EditorTexto.setMinimumSize(QtCore.QSize(400, 240))
        EditorTexto.setMaximumSize(QtCore.QSize(400, 240))
        self.verticalLayoutWidget = QtWidgets.QWidget(EditorTexto)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(4, 5, 391, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 10, 10, 0)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lay_frm_componentes = QtWidgets.QFormLayout()
        self.lay_frm_componentes.setObjectName("lay_frm_componentes")
        self.lbl_seleccion_fuente = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_seleccion_fuente.setObjectName("lbl_seleccion_fuente")
        self.lay_frm_componentes.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_seleccion_fuente)
        self.lbl_editor = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_editor.setObjectName("lbl_editor")
        self.lay_frm_componentes.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_editor)
        self.txt_editor = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.txt_editor.setObjectName("txt_editor")
        self.lay_frm_componentes.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_editor)
        self.fcb_fuentes = QtWidgets.QFontComboBox(self.verticalLayoutWidget)
        self.fcb_fuentes.setObjectName("fcb_fuentes")
        self.lay_frm_componentes.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fcb_fuentes)
        self.lay_ver_principal.addLayout(self.lay_frm_componentes)

        self.retranslateUi(EditorTexto)
        QtCore.QMetaObject.connectSlotsByName(EditorTexto)
        EditorTexto.setTabOrder(self.txt_editor, self.fcb_fuentes)

    def retranslateUi(self, EditorTexto):
        _translate = QtCore.QCoreApplication.translate
        EditorTexto.setWindowTitle(_translate("EditorTexto", "Editor Texto"))
        self.lbl_seleccion_fuente.setText(_translate("EditorTexto", "Seleccione fuente:"))
        self.lbl_editor.setText(_translate("EditorTexto", "Editor:"))
