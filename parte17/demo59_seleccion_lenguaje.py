# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo59_seleccion_lenguaje.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Lenguajes(object):
    def setupUi(self, Lenguajes):
        Lenguajes.setObjectName("Lenguajes")
        Lenguajes.resize(420, 190)
        Lenguajes.setMinimumSize(QtCore.QSize(420, 190))
        Lenguajes.setMaximumSize(QtCore.QSize(420, 190))
        self.verticalLayoutWidget = QtWidgets.QWidget(Lenguajes)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 13, 401, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(0, 0, 0, 0)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lay_frm_entrada = QtWidgets.QFormLayout()
        self.lay_frm_entrada.setObjectName("lay_frm_entrada")
        self.lbl_seleccion_lenguaje = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_seleccion_lenguaje.setObjectName("lbl_seleccion_lenguaje")
        self.lay_frm_entrada.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_seleccion_lenguaje)
        self.cbx_lenguajes = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cbx_lenguajes.setObjectName("cbx_lenguajes")
        self.cbx_lenguajes.addItem("")
        self.cbx_lenguajes.addItem("")
        self.cbx_lenguajes.addItem("")
        self.cbx_lenguajes.addItem("")
        self.cbx_lenguajes.addItem("")
        self.cbx_lenguajes.addItem("")
        self.cbx_lenguajes.addItem("")
        self.lay_frm_entrada.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cbx_lenguajes)
        self.lay_ver_principal.addLayout(self.lay_frm_entrada)
        self.lbl_seleccion = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_seleccion.setText("")
        self.lbl_seleccion.setObjectName("lbl_seleccion")
        self.lay_ver_principal.addWidget(self.lbl_seleccion)

        self.retranslateUi(Lenguajes)
        QtCore.QMetaObject.connectSlotsByName(Lenguajes)

    def retranslateUi(self, Lenguajes):
        _translate = QtCore.QCoreApplication.translate
        Lenguajes.setWindowTitle(_translate("Lenguajes", "Selección Lenguaje"))
        self.lbl_seleccion_lenguaje.setText(_translate("Lenguajes", "Seleccione lenguaje de programación:"))
        self.cbx_lenguajes.setItemText(0, _translate("Lenguajes", "Python"))
        self.cbx_lenguajes.setItemText(1, _translate("Lenguajes", "C#"))
        self.cbx_lenguajes.setItemText(2, _translate("Lenguajes", "Java"))
        self.cbx_lenguajes.setItemText(3, _translate("Lenguajes", "C++"))
        self.cbx_lenguajes.setItemText(4, _translate("Lenguajes", "JavaScript"))
        self.cbx_lenguajes.setItemText(5, _translate("Lenguajes", "C"))
        self.cbx_lenguajes.setItemText(6, _translate("Lenguajes", "PHP"))
