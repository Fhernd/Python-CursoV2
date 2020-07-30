# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo92_dibujo_lineas.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DibujoLineas(object):
    def setupUi(self, DibujoLineas):
        DibujoLineas.setObjectName("DibujoLineas")
        DibujoLineas.resize(640, 480)
        self.wdg_principal = QtWidgets.QWidget(DibujoLineas)
        self.wdg_principal.setObjectName("wdg_principal")
        self.lbl_indicacion = QtWidgets.QLabel(self.wdg_principal)
        self.lbl_indicacion.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.lbl_indicacion.setObjectName("lbl_indicacion")
        self.lst_tipos_lineas = QtWidgets.QListWidget(self.wdg_principal)
        self.lst_tipos_lineas.setGeometry(QtCore.QRect(10, 30, 171, 141))
        self.lst_tipos_lineas.setObjectName("lst_tipos_lineas")
        item = QtWidgets.QListWidgetItem()
        self.lst_tipos_lineas.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_tipos_lineas.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_tipos_lineas.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_tipos_lineas.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_tipos_lineas.addItem(item)
        DibujoLineas.setCentralWidget(self.wdg_principal)
        self.mbr_principal = QtWidgets.QMenuBar(DibujoLineas)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.mbr_principal.setObjectName("mbr_principal")
        DibujoLineas.setMenuBar(self.mbr_principal)
        self.stt_principal = QtWidgets.QStatusBar(DibujoLineas)
        self.stt_principal.setObjectName("stt_principal")
        DibujoLineas.setStatusBar(self.stt_principal)

        self.retranslateUi(DibujoLineas)
        QtCore.QMetaObject.connectSlotsByName(DibujoLineas)

    def retranslateUi(self, DibujoLineas):
        _translate = QtCore.QCoreApplication.translate
        DibujoLineas.setWindowTitle(_translate("DibujoLineas", "Dibujo de Líneas"))
        self.lbl_indicacion.setText(_translate("DibujoLineas", "Seleccione el tipo de línea a dibujar:"))
        __sortingEnabled = self.lst_tipos_lineas.isSortingEnabled()
        self.lst_tipos_lineas.setSortingEnabled(False)
        item = self.lst_tipos_lineas.item(0)
        item.setText(_translate("DibujoLineas", "Sólida"))
        item = self.lst_tipos_lineas.item(1)
        item.setText(_translate("DibujoLineas", "Interlineada"))
        item = self.lst_tipos_lineas.item(2)
        item.setText(_translate("DibujoLineas", "Interlineada con punto"))
        item = self.lst_tipos_lineas.item(3)
        item.setText(_translate("DibujoLineas", "Punteada"))
        item = self.lst_tipos_lineas.item(4)
        item.setText(_translate("DibujoLineas", "Interlineada con doble punto"))
        self.lst_tipos_lineas.setSortingEnabled(__sortingEnabled)
