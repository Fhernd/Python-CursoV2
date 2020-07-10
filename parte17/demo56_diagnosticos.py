# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo56_diagnosticos.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Diagnosticos(object):
    def setupUi(self, Diagnosticos):
        Diagnosticos.setObjectName("Diagnosticos")
        Diagnosticos.resize(403, 276)
        self.verticalLayoutWidget = QtWidgets.QWidget(Diagnosticos)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_listas = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_listas.setContentsMargins(10, 10, 10, 0)
        self.lay_ver_listas.setObjectName("lay_ver_listas")
        self.lay_hor_fuente_diagnosticos = QtWidgets.QHBoxLayout()
        self.lay_hor_fuente_diagnosticos.setObjectName("lay_hor_fuente_diagnosticos")
        self.lbl_seleccion_diagnostico = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_seleccion_diagnostico.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_seleccion_diagnostico.setObjectName("lbl_seleccion_diagnostico")
        self.lay_hor_fuente_diagnosticos.addWidget(self.lbl_seleccion_diagnostico)
        self.lst_diagnosticos = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.lst_diagnosticos.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
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
        self.lay_hor_fuente_diagnosticos.addWidget(self.lst_diagnosticos)
        self.lay_hor_fuente_diagnosticos.setStretch(0, 2)
        self.lay_hor_fuente_diagnosticos.setStretch(1, 2)
        self.lay_ver_listas.addLayout(self.lay_hor_fuente_diagnosticos)
        self.lay_hor_diagnosticos_seleccionados = QtWidgets.QHBoxLayout()
        self.lay_hor_diagnosticos_seleccionados.setObjectName("lay_hor_diagnosticos_seleccionados")
        self.lbl_diagnosticos_seleccionados = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_diagnosticos_seleccionados.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_diagnosticos_seleccionados.setObjectName("lbl_diagnosticos_seleccionados")
        self.lay_hor_diagnosticos_seleccionados.addWidget(self.lbl_diagnosticos_seleccionados)
        self.lst_diagnosticos_seleccionados = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.lst_diagnosticos_seleccionados.setObjectName("lst_diagnosticos_seleccionados")
        self.lay_hor_diagnosticos_seleccionados.addWidget(self.lst_diagnosticos_seleccionados)
        self.lay_hor_diagnosticos_seleccionados.setStretch(0, 2)
        self.lay_hor_diagnosticos_seleccionados.setStretch(1, 2)
        self.lay_ver_listas.addLayout(self.lay_hor_diagnosticos_seleccionados)

        self.retranslateUi(Diagnosticos)
        QtCore.QMetaObject.connectSlotsByName(Diagnosticos)

    def retranslateUi(self, Diagnosticos):
        _translate = QtCore.QCoreApplication.translate
        Diagnosticos.setWindowTitle(_translate("Diagnosticos", "Diagnósticos"))
        self.lbl_seleccion_diagnostico.setText(_translate("Diagnosticos", "Seleccione el diagnóstico:"))
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
        self.lbl_diagnosticos_seleccionados.setText(_translate("Diagnosticos", "Diagnósticos seleccionados:"))
