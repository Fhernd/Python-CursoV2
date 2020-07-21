# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo78_descarga_analisis_archivo.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DescargaEscanerArchivos(object):
    def setupUi(self, DescargaEscanerArchivos):
        DescargaEscanerArchivos.setObjectName("DescargaEscanerArchivos")
        DescargaEscanerArchivos.resize(320, 240)
        DescargaEscanerArchivos.setMinimumSize(QtCore.QSize(320, 240))
        DescargaEscanerArchivos.setMaximumSize(QtCore.QSize(320, 240))
        self.verticalLayoutWidget = QtWidgets.QWidget(DescargaEscanerArchivos)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 10, 10, 20)
        self.lay_ver_principal.setSpacing(15)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lay_ver_descarga = QtWidgets.QVBoxLayout()
        self.lay_ver_descarga.setObjectName("lay_ver_descarga")
        self.lbl_descarga_archivo = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lbl_descarga_archivo.setFont(font)
        self.lbl_descarga_archivo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_descarga_archivo.setObjectName("lbl_descarga_archivo")
        self.lay_ver_descarga.addWidget(self.lbl_descarga_archivo)
        self.pbr_descarga_archivo = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.pbr_descarga_archivo.setProperty("value", 0)
        self.pbr_descarga_archivo.setObjectName("pbr_descarga_archivo")
        self.lay_ver_descarga.addWidget(self.pbr_descarga_archivo)
        self.lay_ver_principal.addLayout(self.lay_ver_descarga)
        self.ver_lay_escaneo = QtWidgets.QVBoxLayout()
        self.ver_lay_escaneo.setObjectName("ver_lay_escaneo")
        self.lbl_escaneo_archivo = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lbl_escaneo_archivo.setFont(font)
        self.lbl_escaneo_archivo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_escaneo_archivo.setObjectName("lbl_escaneo_archivo")
        self.ver_lay_escaneo.addWidget(self.lbl_escaneo_archivo)
        self.pbr_escaneo_archivo = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.pbr_escaneo_archivo.setProperty("value", 0)
        self.pbr_escaneo_archivo.setObjectName("pbr_escaneo_archivo")
        self.ver_lay_escaneo.addWidget(self.pbr_escaneo_archivo)
        self.lay_ver_principal.addLayout(self.ver_lay_escaneo)

        self.retranslateUi(DescargaEscanerArchivos)
        QtCore.QMetaObject.connectSlotsByName(DescargaEscanerArchivos)

    def retranslateUi(self, DescargaEscanerArchivos):
        _translate = QtCore.QCoreApplication.translate
        DescargaEscanerArchivos.setWindowTitle(_translate("DescargaEscanerArchivos", "Descarga y Análisis de Archivos"))
        self.lbl_descarga_archivo.setText(_translate("DescargaEscanerArchivos", "Descargando archivo..."))
        self.lbl_escaneo_archivo.setText(_translate("DescargaEscanerArchivos", "Analizando archivo..."))
