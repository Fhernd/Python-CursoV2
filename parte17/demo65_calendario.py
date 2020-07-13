# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo65_calendario.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Almanaque(object):
    def setupUi(self, Almanaque):
        Almanaque.setObjectName("Almanaque")
        Almanaque.resize(320, 250)
        Almanaque.setMinimumSize(QtCore.QSize(320, 250))
        Almanaque.setMaximumSize(QtCore.QSize(320, 250))
        self.verticalLayoutWidget = QtWidgets.QWidget(Almanaque)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(4, 9, 323, 225))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(0, 0, 10, 0)
        self.lay_ver_principal.setSpacing(10)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.cal_calendario = QtWidgets.QCalendarWidget(self.verticalLayoutWidget)
        self.cal_calendario.setObjectName("cal_calendario")
        self.lay_ver_principal.addWidget(self.cal_calendario)
        self.det_fecha_seleccionada = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.det_fecha_seleccionada.setObjectName("det_fecha_seleccionada")
        self.lay_ver_principal.addWidget(self.det_fecha_seleccionada)

        self.retranslateUi(Almanaque)
        QtCore.QMetaObject.connectSlotsByName(Almanaque)

    def retranslateUi(self, Almanaque):
        _translate = QtCore.QCoreApplication.translate
        Almanaque.setWindowTitle(_translate("Almanaque", "Calendario"))
