# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo47_venta.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentaVentana(object):
    def setupUi(self, VentaVentana):
        VentaVentana.setObjectName("VentaVentana")
        VentaVentana.resize(320, 261)
        self.wdg_principal = QtWidgets.QWidget(VentaVentana)
        self.wdg_principal.setObjectName("wdg_principal")
        self.lbl_resultado_seleccion = QtWidgets.QLabel(self.wdg_principal)
        self.lbl_resultado_seleccion.setGeometry(QtCore.QRect(10, 200, 400, 16))
        self.lbl_resultado_seleccion.setText("")
        self.lbl_resultado_seleccion.setObjectName("lbl_resultado_seleccion")
        self.gbx_seleccion_talla = QtWidgets.QGroupBox(self.wdg_principal)
        self.gbx_seleccion_talla.setGeometry(QtCore.QRect(10, 10, 301, 81))
        self.gbx_seleccion_talla.setObjectName("gbx_seleccion_talla")
        self.rbn_m = QtWidgets.QRadioButton(self.gbx_seleccion_talla)
        self.rbn_m.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.rbn_m.setObjectName("rbn_m")
        self.rbn_xl = QtWidgets.QRadioButton(self.gbx_seleccion_talla)
        self.rbn_xl.setGeometry(QtCore.QRect(160, 20, 82, 17))
        self.rbn_xl.setObjectName("rbn_xl")
        self.rbn_l = QtWidgets.QRadioButton(self.gbx_seleccion_talla)
        self.rbn_l.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.rbn_l.setObjectName("rbn_l")
        self.rbn_xll = QtWidgets.QRadioButton(self.gbx_seleccion_talla)
        self.rbn_xll.setGeometry(QtCore.QRect(160, 50, 82, 17))
        self.rbn_xll.setObjectName("rbn_xll")
        self.gbx_seleccion_metodo_pago = QtWidgets.QGroupBox(self.wdg_principal)
        self.gbx_seleccion_metodo_pago.setGeometry(QtCore.QRect(10, 99, 301, 80))
        self.gbx_seleccion_metodo_pago.setObjectName("gbx_seleccion_metodo_pago")
        self.rbn_tarjeta_credito_debito = QtWidgets.QRadioButton(self.gbx_seleccion_metodo_pago)
        self.rbn_tarjeta_credito_debito.setGeometry(QtCore.QRect(10, 20, 131, 17))
        self.rbn_tarjeta_credito_debito.setObjectName("rbn_tarjeta_credito_debito")
        self.rbn_pago_contraentrega = QtWidgets.QRadioButton(self.gbx_seleccion_metodo_pago)
        self.rbn_pago_contraentrega.setGeometry(QtCore.QRect(160, 20, 131, 17))
        self.rbn_pago_contraentrega.setObjectName("rbn_pago_contraentrega")
        self.rbn_consignacion_bancaria = QtWidgets.QRadioButton(self.gbx_seleccion_metodo_pago)
        self.rbn_consignacion_bancaria.setGeometry(QtCore.QRect(10, 50, 141, 17))
        self.rbn_consignacion_bancaria.setObjectName("rbn_consignacion_bancaria")
        self.rbn_efectivo = QtWidgets.QRadioButton(self.gbx_seleccion_metodo_pago)
        self.rbn_efectivo.setGeometry(QtCore.QRect(160, 50, 82, 17))
        self.rbn_efectivo.setObjectName("rbn_efectivo")
        VentaVentana.setCentralWidget(self.wdg_principal)
        self.mbr_principal = QtWidgets.QMenuBar(VentaVentana)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.mbr_principal.setObjectName("mbr_principal")
        VentaVentana.setMenuBar(self.mbr_principal)
        self.stt_principal = QtWidgets.QStatusBar(VentaVentana)
        self.stt_principal.setObjectName("stt_principal")
        VentaVentana.setStatusBar(self.stt_principal)

        self.retranslateUi(VentaVentana)
        QtCore.QMetaObject.connectSlotsByName(VentaVentana)

    def retranslateUi(self, VentaVentana):
        _translate = QtCore.QCoreApplication.translate
        VentaVentana.setWindowTitle(_translate("VentaVentana", "Venta"))
        self.gbx_seleccion_talla.setTitle(_translate("VentaVentana", "Escoja la talla de su camisa:"))
        self.rbn_m.setText(_translate("VentaVentana", "M"))
        self.rbn_xl.setText(_translate("VentaVentana", "XL"))
        self.rbn_l.setText(_translate("VentaVentana", "L"))
        self.rbn_xll.setText(_translate("VentaVentana", "XLL"))
        self.gbx_seleccion_metodo_pago.setTitle(_translate("VentaVentana", " Seleccione su método de pago:"))
        self.rbn_tarjeta_credito_debito.setText(_translate("VentaVentana", "Tarjeta crédito/débito"))
        self.rbn_pago_contraentrega.setText(_translate("VentaVentana", "Pago contraentrega"))
        self.rbn_consignacion_bancaria.setText(_translate("VentaVentana", "Consignación bancaria"))
        self.rbn_efectivo.setText(_translate("VentaVentana", "Efectivo"))
