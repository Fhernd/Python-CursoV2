# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo95_dibujo_texto.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DibujoTexto(object):
    def setupUi(self, DibujoTexto):
        DibujoTexto.setObjectName("DibujoTexto")
        DibujoTexto.resize(480, 276)
        self.wdg_principal = QtWidgets.QWidget(DibujoTexto)
        self.wdg_principal.setObjectName("wdg_principal")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.wdg_principal)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 481, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 10, 10, 0)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lbl_indicacion = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_indicacion.setObjectName("lbl_indicacion")
        self.lay_ver_principal.addWidget(self.lbl_indicacion)
        self.lay_hor_entrada_datos = QtWidgets.QHBoxLayout()
        self.lay_hor_entrada_datos.setObjectName("lay_hor_entrada_datos")
        self.txt_texto = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.txt_texto.setObjectName("txt_texto")
        self.lay_hor_entrada_datos.addWidget(self.txt_texto)
        self.lst_fuentes = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.lst_fuentes.setObjectName("lst_fuentes")
        item = QtWidgets.QListWidgetItem()
        self.lst_fuentes.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_fuentes.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_fuentes.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_fuentes.addItem(item)
        self.lay_hor_entrada_datos.addWidget(self.lst_fuentes)
        self.cbx_tamagnios = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cbx_tamagnios.setObjectName("cbx_tamagnios")
        self.cbx_tamagnios.addItem("")
        self.cbx_tamagnios.addItem("")
        self.cbx_tamagnios.addItem("")
        self.cbx_tamagnios.addItem("")
        self.cbx_tamagnios.addItem("")
        self.lay_hor_entrada_datos.addWidget(self.cbx_tamagnios)
        self.btn_dibujar_texto = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_dibujar_texto.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_dibujar_texto.setAutoDefault(False)
        self.btn_dibujar_texto.setDefault(False)
        self.btn_dibujar_texto.setFlat(False)
        self.btn_dibujar_texto.setObjectName("btn_dibujar_texto")
        self.lay_hor_entrada_datos.addWidget(self.btn_dibujar_texto)
        self.lay_ver_principal.addLayout(self.lay_hor_entrada_datos)
        DibujoTexto.setCentralWidget(self.wdg_principal)
        self.mbr_principal = QtWidgets.QMenuBar(DibujoTexto)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.mbr_principal.setObjectName("mbr_principal")
        DibujoTexto.setMenuBar(self.mbr_principal)
        self.stt_principal = QtWidgets.QStatusBar(DibujoTexto)
        self.stt_principal.setObjectName("stt_principal")
        DibujoTexto.setStatusBar(self.stt_principal)

        self.retranslateUi(DibujoTexto)
        QtCore.QMetaObject.connectSlotsByName(DibujoTexto)

    def retranslateUi(self, DibujoTexto):
        _translate = QtCore.QCoreApplication.translate
        DibujoTexto.setWindowTitle(_translate("DibujoTexto", "Dibujo de Texto"))
        self.lbl_indicacion.setText(_translate("DibujoTexto", "Especifique el texto, fuente y tamaño para dibujar texto en una ventana."))
        __sortingEnabled = self.lst_fuentes.isSortingEnabled()
        self.lst_fuentes.setSortingEnabled(False)
        item = self.lst_fuentes.item(0)
        item.setText(_translate("DibujoTexto", "Arial"))
        item = self.lst_fuentes.item(1)
        item.setText(_translate("DibujoTexto", "Courier New"))
        item = self.lst_fuentes.item(2)
        item.setText(_translate("DibujoTexto", "Times New Roman"))
        item = self.lst_fuentes.item(3)
        item.setText(_translate("DibujoTexto", "Sans Serif"))
        self.lst_fuentes.setSortingEnabled(__sortingEnabled)
        self.cbx_tamagnios.setItemText(0, _translate("DibujoTexto", "8"))
        self.cbx_tamagnios.setItemText(1, _translate("DibujoTexto", "10"))
        self.cbx_tamagnios.setItemText(2, _translate("DibujoTexto", "13"))
        self.cbx_tamagnios.setItemText(3, _translate("DibujoTexto", "15"))
        self.cbx_tamagnios.setItemText(4, _translate("DibujoTexto", "18"))
        self.btn_dibujar_texto.setText(_translate("DibujoTexto", "Dibujar texto"))
