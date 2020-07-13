# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo64_reloj_digital.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RelojDigital(object):
    def setupUi(self, RelojDigital):
        RelojDigital.setObjectName("RelojDigital")
        RelojDigital.resize(320, 200)
        RelojDigital.setMinimumSize(QtCore.QSize(320, 200))
        RelojDigital.setMaximumSize(QtCore.QSize(320, 200))
        self.verticalLayoutWidget = QtWidgets.QWidget(RelojDigital)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(4, 5, 311, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(0, 0, 0, 0)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lcd_hora = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcd_hora.setObjectName("lcd_hora")
        self.lay_ver_principal.addWidget(self.lcd_hora)

        self.retranslateUi(RelojDigital)
        QtCore.QMetaObject.connectSlotsByName(RelojDigital)

    def retranslateUi(self, RelojDigital):
        _translate = QtCore.QCoreApplication.translate
        RelojDigital.setWindowTitle(_translate("RelojDigital", "Reloj Digital"))
