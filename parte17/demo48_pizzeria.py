# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo48_pizzeria.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pizzeria(object):
    def setupUi(self, Pizzeria):
        Pizzeria.setObjectName("Pizzeria")
        Pizzeria.resize(320, 240)
        self.wdg_principal = QtWidgets.QWidget(Pizzeria)
        self.wdg_principal.setObjectName("wdg_principal")
        self.lbl_precio_base_pizza = QtWidgets.QLabel(self.wdg_principal)
        self.lbl_precio_base_pizza.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.lbl_precio_base_pizza.setObjectName("lbl_precio_base_pizza")
        self.lbl_seleccion_extras = QtWidgets.QLabel(self.wdg_principal)
        self.lbl_seleccion_extras.setGeometry(QtCore.QRect(10, 50, 141, 16))
        self.lbl_seleccion_extras.setObjectName("lbl_seleccion_extras")
        self.chk_queso = QtWidgets.QCheckBox(self.wdg_principal)
        self.chk_queso.setGeometry(QtCore.QRect(10, 80, 111, 17))
        self.chk_queso.setObjectName("chk_queso")
        self.chk_aceitunas = QtWidgets.QCheckBox(self.wdg_principal)
        self.chk_aceitunas.setGeometry(QtCore.QRect(10, 106, 111, 17))
        self.chk_aceitunas.setObjectName("chk_aceitunas")
        self.chk_salsas = QtWidgets.QCheckBox(self.wdg_principal)
        self.chk_salsas.setGeometry(QtCore.QRect(10, 130, 111, 17))
        self.chk_salsas.setObjectName("chk_salsas")
        self.lbl_precio_final = QtWidgets.QLabel(self.wdg_principal)
        self.lbl_precio_final.setGeometry(QtCore.QRect(10, 170, 291, 16))
        self.lbl_precio_final.setObjectName("lbl_precio_final")
        Pizzeria.setCentralWidget(self.wdg_principal)
        self.mbr_principal = QtWidgets.QMenuBar(Pizzeria)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.mbr_principal.setObjectName("mbr_principal")
        Pizzeria.setMenuBar(self.mbr_principal)
        self.stt_principal = QtWidgets.QStatusBar(Pizzeria)
        self.stt_principal.setObjectName("stt_principal")
        Pizzeria.setStatusBar(self.stt_principal)

        self.retranslateUi(Pizzeria)
        QtCore.QMetaObject.connectSlotsByName(Pizzeria)

    def retranslateUi(self, Pizzeria):
        _translate = QtCore.QCoreApplication.translate
        Pizzeria.setWindowTitle(_translate("Pizzeria", "Pizzería"))
        self.lbl_precio_base_pizza.setText(_translate("Pizzeria", "Precio Pizza: $15"))
        self.lbl_seleccion_extras.setText(_translate("Pizzeria", "Seleccione los extras:"))
        self.chk_queso.setText(_translate("Pizzeria", "Queso - $1"))
        self.chk_aceitunas.setText(_translate("Pizzeria", "Aceitunas - $2"))
        self.chk_salsas.setText(_translate("Pizzeria", "Salsas - $1"))
        self.lbl_precio_final.setText(_translate("Pizzeria", "Precio final: $15"))
