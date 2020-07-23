# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo83_consulta_base_datos.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConsultaDatos(object):
    def setupUi(self, ConsultaDatos):
        ConsultaDatos.setObjectName("ConsultaDatos")
        ConsultaDatos.resize(336, 238)
        ConsultaDatos.setMinimumSize(QtCore.QSize(336, 238))
        ConsultaDatos.setMaximumSize(QtCore.QSize(336, 238))
        self.verticalLayoutWidget = QtWidgets.QWidget(ConsultaDatos)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 341, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 10, 10, 0)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.btn_consultar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_consultar.setObjectName("btn_consultar")
        self.lay_ver_principal.addWidget(self.btn_consultar)
        self.tbl_datos = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tbl_datos.setObjectName("tbl_datos")
        self.tbl_datos.setColumnCount(3)
        self.tbl_datos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_datos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_datos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_datos.setHorizontalHeaderItem(2, item)
        self.lay_ver_principal.addWidget(self.tbl_datos)

        self.retranslateUi(ConsultaDatos)
        QtCore.QMetaObject.connectSlotsByName(ConsultaDatos)

    def retranslateUi(self, ConsultaDatos):
        _translate = QtCore.QCoreApplication.translate
        ConsultaDatos.setWindowTitle(_translate("ConsultaDatos", "Consulta Base de Datos"))
        self.btn_consultar.setText(_translate("ConsultaDatos", "Consultar datos"))
        item = self.tbl_datos.horizontalHeaderItem(0)
        item.setText(_translate("ConsultaDatos", "Documento"))
        item = self.tbl_datos.horizontalHeaderItem(1)
        item.setText(_translate("ConsultaDatos", "Nombre"))
        item = self.tbl_datos.horizontalHeaderItem(2)
        item.setText(_translate("ConsultaDatos", "Ahorros"))
