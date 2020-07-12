# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo63_visor.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Visor(object):
    def setupUi(self, Visor):
        Visor.setObjectName("Visor")
        Visor.resize(360, 170)
        Visor.setMinimumSize(QtCore.QSize(360, 170))
        Visor.setMaximumSize(QtCore.QSize(360, 170))
        self.verticalLayoutWidget = QtWidgets.QWidget(Visor)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(4, 4, 351, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(0, 0, 0, 0)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lcd_numero = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcd_numero.setProperty("intValue", 42)
        self.lcd_numero.setObjectName("lcd_numero")
        self.lay_ver_principal.addWidget(self.lcd_numero)
        self.lay_hor_botones = QtWidgets.QHBoxLayout()
        self.lay_hor_botones.setObjectName("lay_hor_botones")
        self.btn_decimal = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_decimal.setObjectName("btn_decimal")
        self.lay_hor_botones.addWidget(self.btn_decimal)
        self.btn_binario = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_binario.setObjectName("btn_binario")
        self.lay_hor_botones.addWidget(self.btn_binario)
        self.btn_octal = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_octal.setObjectName("btn_octal")
        self.lay_hor_botones.addWidget(self.btn_octal)
        self.btn_hexadecimal = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_hexadecimal.setObjectName("btn_hexadecimal")
        self.lay_hor_botones.addWidget(self.btn_hexadecimal)
        self.lay_ver_principal.addLayout(self.lay_hor_botones)

        self.retranslateUi(Visor)
        QtCore.QMetaObject.connectSlotsByName(Visor)

    def retranslateUi(self, Visor):
        _translate = QtCore.QCoreApplication.translate
        Visor.setWindowTitle(_translate("Visor", "Visor"))
        self.btn_decimal.setText(_translate("Visor", "DEC"))
        self.btn_binario.setText(_translate("Visor", "BIN"))
        self.btn_octal.setText(_translate("Visor", "OCT"))
        self.btn_hexadecimal.setText(_translate("Visor", "HEX"))
