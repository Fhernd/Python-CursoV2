# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo77_descarga_archivo.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DescargaArchivo(object):
    def setupUi(self, DescargaArchivo):
        DescargaArchivo.setObjectName("DescargaArchivo")
        DescargaArchivo.resize(320, 240)
        DescargaArchivo.setMinimumSize(QtCore.QSize(320, 240))
        DescargaArchivo.setMaximumSize(QtCore.QSize(320, 240))
        self.verticalLayoutWidget = QtWidgets.QWidget(DescargaArchivo)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 10, 10, 80)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lbl_descarga_archivo = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.lbl_descarga_archivo.setFont(font)
        self.lbl_descarga_archivo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_descarga_archivo.setObjectName("lbl_descarga_archivo")
        self.lay_ver_principal.addWidget(self.lbl_descarga_archivo)
        self.pgr_descarga_archivo = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pgr_descarga_archivo.sizePolicy().hasHeightForWidth())
        self.pgr_descarga_archivo.setSizePolicy(sizePolicy)
        self.pgr_descarga_archivo.setProperty("value", 0)
        self.pgr_descarga_archivo.setObjectName("pgr_descarga_archivo")
        self.lay_ver_principal.addWidget(self.pgr_descarga_archivo)
        self.lay_ver_principal.setStretch(0, 1)
        self.lay_ver_principal.setStretch(1, 4)

        self.retranslateUi(DescargaArchivo)
        QtCore.QMetaObject.connectSlotsByName(DescargaArchivo)

    def retranslateUi(self, DescargaArchivo):
        _translate = QtCore.QCoreApplication.translate
        DescargaArchivo.setWindowTitle(_translate("DescargaArchivo", "Descarga Archivo"))
        self.lbl_descarga_archivo.setText(_translate("DescargaArchivo", "Descargando archivo..."))
