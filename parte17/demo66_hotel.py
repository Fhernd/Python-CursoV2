# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo66_hotel.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HotelSistemaReservas(object):
    def setupUi(self, HotelSistemaReservas):
        HotelSistemaReservas.setObjectName("HotelSistemaReservas")
        HotelSistemaReservas.resize(480, 420)
        HotelSistemaReservas.setMinimumSize(QtCore.QSize(480, 420))
        HotelSistemaReservas.setMaximumSize(QtCore.QSize(480, 420))
        self.verticalLayoutWidget = QtWidgets.QWidget(HotelSistemaReservas)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(4, 6, 471, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 10, 10, 0)
        self.lay_ver_principal.setSpacing(15)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lay_frm_entrada = QtWidgets.QFormLayout()
        self.lay_frm_entrada.setHorizontalSpacing(23)
        self.lay_frm_entrada.setObjectName("lay_frm_entrada")
        self.lbl_fecha_reserva = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_fecha_reserva.setObjectName("lbl_fecha_reserva")
        self.lay_frm_entrada.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_fecha_reserva)
        self.cal_fecha_reserva = QtWidgets.QCalendarWidget(self.verticalLayoutWidget)
        self.cal_fecha_reserva.setObjectName("cal_fecha_reserva")
        self.lay_frm_entrada.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cal_fecha_reserva)
        self.lbl_cantidad_dias = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_cantidad_dias.setObjectName("lbl_cantidad_dias")
        self.lay_frm_entrada.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_cantidad_dias)
        self.sbx_cantidad_dias = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbx_cantidad_dias.setObjectName("sbx_cantidad_dias")
        self.lay_frm_entrada.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sbx_cantidad_dias)
        self.lbl_tipo_habitacion = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_tipo_habitacion.setObjectName("lbl_tipo_habitacion")
        self.lay_frm_entrada.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_tipo_habitacion)
        self.cbx_tipo_habitacion = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cbx_tipo_habitacion.setObjectName("cbx_tipo_habitacion")
        self.cbx_tipo_habitacion.addItem("")
        self.cbx_tipo_habitacion.addItem("")
        self.cbx_tipo_habitacion.addItem("")
        self.cbx_tipo_habitacion.addItem("")
        self.lay_frm_entrada.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cbx_tipo_habitacion)
        self.btn_calcular = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_calcular.setObjectName("btn_calcular")
        self.lay_frm_entrada.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.btn_calcular)
        self.lay_ver_principal.addLayout(self.lay_frm_entrada)
        self.lay_frm_seleccion = QtWidgets.QFormLayout()
        self.lay_frm_seleccion.setHorizontalSpacing(20)
        self.lay_frm_seleccion.setObjectName("lay_frm_seleccion")
        self.lbl_resumen_seleccion = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_resumen_seleccion.setObjectName("lbl_resumen_seleccion")
        self.lay_frm_seleccion.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_resumen_seleccion)
        self.txt_resumen_seleccion = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.txt_resumen_seleccion.setReadOnly(True)
        self.txt_resumen_seleccion.setObjectName("txt_resumen_seleccion")
        self.lay_frm_seleccion.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_resumen_seleccion)
        self.lbl_costo = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_costo.setObjectName("lbl_costo")
        self.lay_frm_seleccion.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_costo)
        self.txt_costo = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_costo.setReadOnly(True)
        self.txt_costo.setObjectName("txt_costo")
        self.lay_frm_seleccion.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_costo)
        self.lay_ver_principal.addLayout(self.lay_frm_seleccion)

        self.retranslateUi(HotelSistemaReservas)
        QtCore.QMetaObject.connectSlotsByName(HotelSistemaReservas)

    def retranslateUi(self, HotelSistemaReservas):
        _translate = QtCore.QCoreApplication.translate
        HotelSistemaReservas.setWindowTitle(_translate("HotelSistemaReservas", "Dialog"))
        self.lbl_fecha_reserva.setText(_translate("HotelSistemaReservas", "Fecha de reserva:"))
        self.lbl_cantidad_dias.setText(_translate("HotelSistemaReservas", "Cantidad de días:"))
        self.lbl_tipo_habitacion.setText(_translate("HotelSistemaReservas", "Tipo habitación:"))
        self.cbx_tipo_habitacion.setItemText(0, _translate("HotelSistemaReservas", "Sencilla"))
        self.cbx_tipo_habitacion.setItemText(1, _translate("HotelSistemaReservas", "Doble"))
        self.cbx_tipo_habitacion.setItemText(2, _translate("HotelSistemaReservas", "Queen"))
        self.cbx_tipo_habitacion.setItemText(3, _translate("HotelSistemaReservas", "Queen doble"))
        self.btn_calcular.setText(_translate("HotelSistemaReservas", "Calcular"))
        self.lbl_resumen_seleccion.setText(_translate("HotelSistemaReservas", "Resumen selección:"))
        self.lbl_costo.setText(_translate("HotelSistemaReservas", "Costo:"))
