# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ex2_reporte_ventas_rango_fechas.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReporteVentasRangoFechas(object):
    def setupUi(self, ReporteVentasRangoFechas):
        ReporteVentasRangoFechas.setObjectName("ReporteVentasRangoFechas")
        ReporteVentasRangoFechas.resize(470, 280)
        ReporteVentasRangoFechas.setMinimumSize(QtCore.QSize(470, 280))
        ReporteVentasRangoFechas.setMaximumSize(QtCore.QSize(470, 280))
        self.gridLayout = QtWidgets.QGridLayout(ReporteVentasRangoFechas)
        self.gridLayout.setObjectName("gridLayout")
        self.lay_ver_principal = QtWidgets.QVBoxLayout()
        self.lay_ver_principal.setSpacing(6)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lay_frm_datos = QtWidgets.QFormLayout()
        self.lay_frm_datos.setHorizontalSpacing(100)
        self.lay_frm_datos.setObjectName("lay_frm_datos")
        self.lbl_fecha_inicio = QtWidgets.QLabel(ReporteVentasRangoFechas)
        self.lbl_fecha_inicio.setObjectName("lbl_fecha_inicio")
        self.lay_frm_datos.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_fecha_inicio)
        self.dat_fecha_inicio = QtWidgets.QDateEdit(ReporteVentasRangoFechas)
        self.dat_fecha_inicio.setObjectName("dat_fecha_inicio")
        self.lay_frm_datos.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dat_fecha_inicio)
        self.lbl_fecha_final = QtWidgets.QLabel(ReporteVentasRangoFechas)
        self.lbl_fecha_final.setObjectName("lbl_fecha_final")
        self.lay_frm_datos.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_fecha_final)
        self.dat_fecha_final = QtWidgets.QDateEdit(ReporteVentasRangoFechas)
        self.dat_fecha_final.setObjectName("dat_fecha_final")
        self.lay_frm_datos.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dat_fecha_final)
        self.btn_buscar = QtWidgets.QPushButton(ReporteVentasRangoFechas)
        self.btn_buscar.setObjectName("btn_buscar")
        self.lay_frm_datos.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btn_buscar)
        self.lay_ver_principal.addLayout(self.lay_frm_datos)
        self.tbl_ventas = QtWidgets.QTableWidget(ReporteVentasRangoFechas)
        self.tbl_ventas.setObjectName("tbl_ventas")
        self.tbl_ventas.setColumnCount(4)
        self.tbl_ventas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ventas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ventas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ventas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ventas.setHorizontalHeaderItem(3, item)
        self.lay_ver_principal.addWidget(self.tbl_ventas)
        self.lay_ver_principal.setStretch(0, 1)
        self.lay_ver_principal.setStretch(1, 2)
        self.gridLayout.addLayout(self.lay_ver_principal, 0, 0, 1, 1)

        self.retranslateUi(ReporteVentasRangoFechas)
        QtCore.QMetaObject.connectSlotsByName(ReporteVentasRangoFechas)

    def retranslateUi(self, ReporteVentasRangoFechas):
        _translate = QtCore.QCoreApplication.translate
        ReporteVentasRangoFechas.setWindowTitle(_translate("ReporteVentasRangoFechas", "Reporte - Ventas Rango Fechas"))
        self.lbl_fecha_inicio.setText(_translate("ReporteVentasRangoFechas", "Fecha inicio:"))
        self.lbl_fecha_final.setText(_translate("ReporteVentasRangoFechas", "Fecha final:"))
        self.btn_buscar.setText(_translate("ReporteVentasRangoFechas", "Buscar"))
        item = self.tbl_ventas.horizontalHeaderItem(0)
        item.setText(_translate("ReporteVentasRangoFechas", "ID Producto"))
        item = self.tbl_ventas.horizontalHeaderItem(1)
        item.setText(_translate("ReporteVentasRangoFechas", "Fecha"))
        item = self.tbl_ventas.horizontalHeaderItem(2)
        item.setText(_translate("ReporteVentasRangoFechas", "Cantidad"))
        item = self.tbl_ventas.horizontalHeaderItem(3)
        item.setText(_translate("ReporteVentasRangoFechas", "Total"))
