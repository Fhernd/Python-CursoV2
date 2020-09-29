# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ex2_reporte_top_5.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReporteTop5(object):
    def setupUi(self, ReporteTop5):
        ReporteTop5.setObjectName("ReporteTop5")
        ReporteTop5.resize(470, 240)
        ReporteTop5.setMinimumSize(QtCore.QSize(470, 240))
        ReporteTop5.setMaximumSize(QtCore.QSize(470, 240))
        self.gridLayout = QtWidgets.QGridLayout(ReporteTop5)
        self.gridLayout.setObjectName("gridLayout")
        self.lay_ver_principal = QtWidgets.QVBoxLayout()
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.tbl_top_5 = QtWidgets.QTableWidget(ReporteTop5)
        self.tbl_top_5.setObjectName("tbl_top_5")
        self.tbl_top_5.setColumnCount(5)
        self.tbl_top_5.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_top_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_top_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_top_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_top_5.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_top_5.setHorizontalHeaderItem(4, item)
        self.lay_ver_principal.addWidget(self.tbl_top_5)
        self.gridLayout.addLayout(self.lay_ver_principal, 0, 0, 1, 1)

        self.retranslateUi(ReporteTop5)
        QtCore.QMetaObject.connectSlotsByName(ReporteTop5)

    def retranslateUi(self, ReporteTop5):
        _translate = QtCore.QCoreApplication.translate
        ReporteTop5.setWindowTitle(_translate("ReporteTop5", "Reporte"))
        item = self.tbl_top_5.horizontalHeaderItem(0)
        item.setText(_translate("ReporteTop5", "Código"))
        item = self.tbl_top_5.horizontalHeaderItem(1)
        item.setText(_translate("ReporteTop5", "Nombre"))
        item = self.tbl_top_5.horizontalHeaderItem(2)
        item.setText(_translate("ReporteTop5", "Precio"))
        item = self.tbl_top_5.horizontalHeaderItem(3)
        item.setText(_translate("ReporteTop5", "Cantidad"))
        item = self.tbl_top_5.horizontalHeaderItem(4)
        item.setText(_translate("ReporteTop5", "Total"))
