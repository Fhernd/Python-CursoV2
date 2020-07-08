# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo51_segniales_slots.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SegnialesSlots(object):
    def setupUi(self, SegnialesSlots):
        SegnialesSlots.setObjectName("SegnialesSlots")
        SegnialesSlots.resize(240, 213)
        self.verticalLayoutWidget = QtWidgets.QWidget(SegnialesSlots)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 241, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(5, 0, 5, 0)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.txt_fuente = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_fuente.setObjectName("txt_fuente")
        self.lay_ver_principal.addWidget(self.txt_fuente)
        self.btn_copiar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_copiar.setObjectName("btn_copiar")
        self.lay_ver_principal.addWidget(self.btn_copiar)
        self.btn_pegar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_pegar.setObjectName("btn_pegar")
        self.lay_ver_principal.addWidget(self.btn_pegar)
        self.txt_destino = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_destino.setReadOnly(True)
        self.txt_destino.setObjectName("txt_destino")
        self.lay_ver_principal.addWidget(self.txt_destino)

        self.retranslateUi(SegnialesSlots)
        self.btn_copiar.pressed.connect(self.txt_fuente.selectAll)
        self.btn_copiar.released.connect(self.txt_fuente.copy)
        self.btn_pegar.clicked.connect(self.txt_destino.paste)
        QtCore.QMetaObject.connectSlotsByName(SegnialesSlots)

    def retranslateUi(self, SegnialesSlots):
        _translate = QtCore.QCoreApplication.translate
        SegnialesSlots.setWindowTitle(_translate("SegnialesSlots", "Señales & Slots"))
        self.btn_copiar.setText(_translate("SegnialesSlots", "Copiar"))
        self.btn_pegar.setText(_translate("SegnialesSlots", "Pegar"))
