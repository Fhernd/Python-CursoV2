# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parte17\demo46_seleccion_vuelo.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SeleccionVuelo(object):
    def setupUi(self, SeleccionVuelo):
        SeleccionVuelo.setObjectName("SeleccionVuelo")
        SeleccionVuelo.resize(320, 184)
        self.wdg_principal = QtWidgets.QWidget(SeleccionVuelo)
        self.wdg_principal.setObjectName("wdg_principal")
        self.lbl_escoger_clase_vuelo = QtWidgets.QLabel(self.wdg_principal)
        self.lbl_escoger_clase_vuelo.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.lbl_escoger_clase_vuelo.setObjectName("lbl_escoger_clase_vuelo")
        self.rbn_primera_clase = QtWidgets.QRadioButton(self.wdg_principal)
        self.rbn_primera_clase.setGeometry(QtCore.QRect(10, 40, 161, 17))
        self.rbn_primera_clase.setObjectName("rbn_primera_clase")
        self.rbn_clase_negocios = QtWidgets.QRadioButton(self.wdg_principal)
        self.rbn_clase_negocios.setGeometry(QtCore.QRect(10, 62, 161, 17))
        self.rbn_clase_negocios.setObjectName("rbn_clase_negocios")
        self.rbn_clase_economica = QtWidgets.QRadioButton(self.wdg_principal)
        self.rbn_clase_economica.setGeometry(QtCore.QRect(10, 84, 161, 17))
        self.rbn_clase_economica.setObjectName("rbn_clase_economica")
        self.lbl_resultado_seleccion = QtWidgets.QLabel(self.wdg_principal)
        self.lbl_resultado_seleccion.setGeometry(QtCore.QRect(10, 120, 301, 16))
        self.lbl_resultado_seleccion.setText("")
        self.lbl_resultado_seleccion.setObjectName("lbl_resultado_seleccion")
        SeleccionVuelo.setCentralWidget(self.wdg_principal)
        self.mbr_principal = QtWidgets.QMenuBar(SeleccionVuelo)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.mbr_principal.setObjectName("mbr_principal")
        SeleccionVuelo.setMenuBar(self.mbr_principal)
        self.stt_principal = QtWidgets.QStatusBar(SeleccionVuelo)
        self.stt_principal.setObjectName("stt_principal")
        SeleccionVuelo.setStatusBar(self.stt_principal)

        self.retranslateUi(SeleccionVuelo)
        QtCore.QMetaObject.connectSlotsByName(SeleccionVuelo)

    def retranslateUi(self, SeleccionVuelo):
        _translate = QtCore.QCoreApplication.translate
        SeleccionVuelo.setWindowTitle(_translate("SeleccionVuelo", "Selección Vuelo"))
        self.lbl_escoger_clase_vuelo.setText(_translate("SeleccionVuelo", "Escoja la clase del vuelo:"))
        self.rbn_primera_clase.setText(_translate("SeleccionVuelo", "Primera clase: $190USD"))
        self.rbn_clase_negocios.setText(_translate("SeleccionVuelo", "Clase negocios: $130USD"))
        self.rbn_clase_economica.setText(_translate("SeleccionVuelo", "Clase económica: $99USD"))
