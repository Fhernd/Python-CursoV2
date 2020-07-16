# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo72_selector_fuente.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SelectorFuente(object):
    def setupUi(self, SelectorFuente):
        SelectorFuente.setObjectName("SelectorFuente")
        SelectorFuente.resize(320, 240)
        SelectorFuente.setMinimumSize(QtCore.QSize(320, 240))
        SelectorFuente.setMaximumSize(QtCore.QSize(320, 240))
        self.verticalLayoutWidget = QtWidgets.QWidget(SelectorFuente)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 3, 301, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 10, 10, 10)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.btn_seleccionar_fuente = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_seleccionar_fuente.setObjectName("btn_seleccionar_fuente")
        self.lay_ver_principal.addWidget(self.btn_seleccionar_fuente)
        self.txt_contenido = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.txt_contenido.setObjectName("txt_contenido")
        self.lay_ver_principal.addWidget(self.txt_contenido)

        self.retranslateUi(SelectorFuente)
        QtCore.QMetaObject.connectSlotsByName(SelectorFuente)

    def retranslateUi(self, SelectorFuente):
        _translate = QtCore.QCoreApplication.translate
        SelectorFuente.setWindowTitle(_translate("SelectorFuente", "Selector Fuente"))
        self.btn_seleccionar_fuente.setText(_translate("SelectorFuente", "Seleccionar fuente..."))
        self.txt_contenido.setHtml(_translate("SelectorFuente", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">¡Python es tremendo!</span></p></body></html>"))
