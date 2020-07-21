# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo79_descarga_analisis_async.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DescargaAnalisisAsync(object):
    def setupUi(self, DescargaAnalisisAsync):
        DescargaAnalisisAsync.setObjectName("DescargaAnalisisAsync")
        DescargaAnalisisAsync.resize(320, 280)
        DescargaAnalisisAsync.setMinimumSize(QtCore.QSize(320, 280))
        DescargaAnalisisAsync.setMaximumSize(QtCore.QSize(320, 280))
        self.verticalLayoutWidget = QtWidgets.QWidget(DescargaAnalisisAsync)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 10, 10, 10)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.btn_iniciar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_iniciar.setObjectName("btn_iniciar")
        self.lay_ver_principal.addWidget(self.btn_iniciar)
        self.gbx_principal = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.gbx_principal.setObjectName("gbx_principal")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.gbx_principal)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 291, 201))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.lay_ver_operaciones = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.lay_ver_operaciones.setContentsMargins(0, 0, 0, 0)
        self.lay_ver_operaciones.setObjectName("lay_ver_operaciones")
        self.lay_ver_descarga_archivo = QtWidgets.QVBoxLayout()
        self.lay_ver_descarga_archivo.setObjectName("lay_ver_descarga_archivo")
        self.lbl_descarga_archivo = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lbl_descarga_archivo.setFont(font)
        self.lbl_descarga_archivo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_descarga_archivo.setObjectName("lbl_descarga_archivo")
        self.lay_ver_descarga_archivo.addWidget(self.lbl_descarga_archivo)
        self.pgr_descarga_archivo = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.pgr_descarga_archivo.setProperty("value", 0)
        self.pgr_descarga_archivo.setObjectName("pgr_descarga_archivo")
        self.lay_ver_descarga_archivo.addWidget(self.pgr_descarga_archivo)
        self.lay_ver_operaciones.addLayout(self.lay_ver_descarga_archivo)
        self.lay_ver_analisis_archivo = QtWidgets.QVBoxLayout()
        self.lay_ver_analisis_archivo.setObjectName("lay_ver_analisis_archivo")
        self.lbl_analisis_archivo = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lbl_analisis_archivo.setFont(font)
        self.lbl_analisis_archivo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_analisis_archivo.setObjectName("lbl_analisis_archivo")
        self.lay_ver_analisis_archivo.addWidget(self.lbl_analisis_archivo)
        self.pbr_analisis_archivo = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.pbr_analisis_archivo.setProperty("value", 0)
        self.pbr_analisis_archivo.setObjectName("pbr_analisis_archivo")
        self.lay_ver_analisis_archivo.addWidget(self.pbr_analisis_archivo)
        self.lay_ver_operaciones.addLayout(self.lay_ver_analisis_archivo)
        self.lay_ver_principal.addWidget(self.gbx_principal)

        self.retranslateUi(DescargaAnalisisAsync)
        QtCore.QMetaObject.connectSlotsByName(DescargaAnalisisAsync)

    def retranslateUi(self, DescargaAnalisisAsync):
        _translate = QtCore.QCoreApplication.translate
        DescargaAnalisisAsync.setWindowTitle(_translate("DescargaAnalisisAsync", "Descarga & Análisis"))
        self.btn_iniciar.setText(_translate("DescargaAnalisisAsync", "Iniciar"))
        self.gbx_principal.setTitle(_translate("DescargaAnalisisAsync", "Operaciones"))
        self.lbl_descarga_archivo.setText(_translate("DescargaAnalisisAsync", "Descargando archivo..."))
        self.lbl_analisis_archivo.setText(_translate("DescargaAnalisisAsync", "Analizando archivo..."))
