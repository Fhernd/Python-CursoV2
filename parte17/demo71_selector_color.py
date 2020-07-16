# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo71_selector_color.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SelectorColor(object):
    def setupUi(self, SelectorColor):
        SelectorColor.setObjectName("SelectorColor")
        SelectorColor.resize(420, 240)
        SelectorColor.setMinimumSize(QtCore.QSize(420, 240))
        SelectorColor.setMaximumSize(QtCore.QSize(420, 240))
        self.verticalLayoutWidget = QtWidgets.QWidget(SelectorColor)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(4, 3, 411, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 10, 10, 0)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lay_hor_seleccion_color = QtWidgets.QHBoxLayout()
        self.lay_hor_seleccion_color.setObjectName("lay_hor_seleccion_color")
        self.btn_seleccionar_color = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_seleccionar_color.setObjectName("btn_seleccionar_color")
        self.lay_hor_seleccion_color.addWidget(self.btn_seleccionar_color)
        self.frm_color_selecciondo = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frm_color_selecciondo.setStyleSheet("QWidget {\n"
" background-color: #000;\n"
"}")
        self.frm_color_selecciondo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_color_selecciondo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_color_selecciondo.setObjectName("frm_color_selecciondo")
        self.lay_hor_seleccion_color.addWidget(self.frm_color_selecciondo)
        self.lay_ver_principal.addLayout(self.lay_hor_seleccion_color)
        self.lbl_color_seleccionado = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_color_seleccionado.setObjectName("lbl_color_seleccionado")
        self.lay_ver_principal.addWidget(self.lbl_color_seleccionado)

        self.retranslateUi(SelectorColor)
        QtCore.QMetaObject.connectSlotsByName(SelectorColor)

    def retranslateUi(self, SelectorColor):
        _translate = QtCore.QCoreApplication.translate
        SelectorColor.setWindowTitle(_translate("SelectorColor", "Selector de Color"))
        self.btn_seleccionar_color.setText(_translate("SelectorColor", "Seleccionar color..."))
        self.lbl_color_seleccionado.setText(_translate("SelectorColor", "#000000"))
