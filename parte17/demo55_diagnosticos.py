# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo55_diagnosticos.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Diagnosticos(object):
    def setupUi(self, Diagnosticos):
        Diagnosticos.setObjectName("Diagnosticos")
        Diagnosticos.resize(320, 240)
        Diagnosticos.setMinimumSize(QtCore.QSize(320, 240))
        Diagnosticos.setMaximumSize(QtCore.QSize(320, 240))
        self.verticalLayoutWidget = QtWidgets.QWidget(Diagnosticos)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_diagnosticos = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_diagnosticos.setContentsMargins(10, 10, 10, 0)
        self.lay_ver_diagnosticos.setObjectName("lay_ver_diagnosticos")
        self.lbl_seleccion_diagnosticos = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_seleccion_diagnosticos.setObjectName("lbl_seleccion_diagnosticos")
        self.lay_ver_diagnosticos.addWidget(self.lbl_seleccion_diagnosticos)
        self.lst_diagnosticos = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.lst_diagnosticos.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.lst_diagnosticos.setObjectName("lst_diagnosticos")
        item = QtWidgets.QListWidgetItem()
        self.lst_diagnosticos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_diagnosticos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_diagnosticos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_diagnosticos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_diagnosticos.addItem(item)
        self.lay_ver_diagnosticos.addWidget(self.lst_diagnosticos)
        self.lbl_diagnostico_seleccionado = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_diagnostico_seleccionado.setText("")
        self.lbl_diagnostico_seleccionado.setObjectName("lbl_diagnostico_seleccionado")
        self.lay_ver_diagnosticos.addWidget(self.lbl_diagnostico_seleccionado)
        self.lay_ver_diagnosticos.setStretch(0, 1)
        self.lay_ver_diagnosticos.setStretch(1, 2)
        self.lay_ver_diagnosticos.setStretch(2, 1)

        self.retranslateUi(Diagnosticos)
        QtCore.QMetaObject.connectSlotsByName(Diagnosticos)

    def retranslateUi(self, Diagnosticos):
        _translate = QtCore.QCoreApplication.translate
        Diagnosticos.setWindowTitle(_translate("Diagnosticos", "Diagnósticos"))
        self.lbl_seleccion_diagnosticos.setText(_translate("Diagnosticos", "Seleccione el diagnóstico:"))
        __sortingEnabled = self.lst_diagnosticos.isSortingEnabled()
        self.lst_diagnosticos.setSortingEnabled(False)
        item = self.lst_diagnosticos.item(0)
        item.setText(_translate("Diagnosticos", "Rayos X - $5"))
        item = self.lst_diagnosticos.item(1)
        item.setText(_translate("Diagnosticos", "Nivel de azúcar - $3"))
        item = self.lst_diagnosticos.item(2)
        item.setText(_translate("Diagnosticos", "Prueba de hemoglobina - $7"))
        item = self.lst_diagnosticos.item(3)
        item.setText(_translate("Diagnosticos", "Análisis de orina - $8"))
        item = self.lst_diagnosticos.item(4)
        item.setText(_translate("Diagnosticos", "Análisis de PSA - $10"))
        self.lst_diagnosticos.setSortingEnabled(__sortingEnabled)
