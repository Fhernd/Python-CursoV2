# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo74_contenedor_ventanas.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ContenedorVentanas(object):
    def setupUi(self, ContenedorVentanas):
        ContenedorVentanas.setObjectName("ContenedorVentanas")
        ContenedorVentanas.resize(640, 480)
        ContenedorVentanas.setMinimumSize(QtCore.QSize(640, 480))
        ContenedorVentanas.setMaximumSize(QtCore.QSize(640, 480))
        self.wdg_principal = QtWidgets.QWidget(ContenedorVentanas)
        self.wdg_principal.setObjectName("wdg_principal")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.wdg_principal)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 641, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(0, 0, 0, 0)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.mdi_contenedor = QtWidgets.QMdiArea(self.verticalLayoutWidget)
        self.mdi_contenedor.setObjectName("mdi_contenedor")
        self.wdg_primera_ventana = QtWidgets.QWidget()
        self.wdg_primera_ventana.setObjectName("wdg_primera_ventana")
        self.lbl_primera_ventana = QtWidgets.QLabel(self.wdg_primera_ventana)
        self.lbl_primera_ventana.setGeometry(QtCore.QRect(90, 60, 91, 16))
        self.lbl_primera_ventana.setObjectName("lbl_primera_ventana")
        self.wdg_segunda_ventana = QtWidgets.QWidget()
        self.wdg_segunda_ventana.setObjectName("wdg_segunda_ventana")
        self.lbl_segunda_ventana = QtWidgets.QLabel(self.wdg_segunda_ventana)
        self.lbl_segunda_ventana.setGeometry(QtCore.QRect(80, 60, 91, 16))
        self.lbl_segunda_ventana.setObjectName("lbl_segunda_ventana")
        self.lay_ver_principal.addWidget(self.mdi_contenedor)
        ContenedorVentanas.setCentralWidget(self.wdg_principal)
        self.mbr_principal = QtWidgets.QMenuBar(ContenedorVentanas)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.mbr_principal.setObjectName("mbr_principal")
        self.mnu_ventanas = QtWidgets.QMenu(self.mbr_principal)
        self.mnu_ventanas.setObjectName("mnu_ventanas")
        ContenedorVentanas.setMenuBar(self.mbr_principal)
        self.stt_principal = QtWidgets.QStatusBar(ContenedorVentanas)
        self.stt_principal.setObjectName("stt_principal")
        ContenedorVentanas.setStatusBar(self.stt_principal)
        self.mni_tabs = QtWidgets.QAction(ContenedorVentanas)
        self.mni_tabs.setObjectName("mni_tabs")
        self.mni_cascada = QtWidgets.QAction(ContenedorVentanas)
        self.mni_cascada.setObjectName("mni_cascada")
        self.mni_cuadricula = QtWidgets.QAction(ContenedorVentanas)
        self.mni_cuadricula.setObjectName("mni_cuadricula")
        self.mni_subventanas = QtWidgets.QAction(ContenedorVentanas)
        self.mni_subventanas.setObjectName("mni_subventanas")
        self.mnu_ventanas.addAction(self.mni_tabs)
        self.mnu_ventanas.addAction(self.mni_cascada)
        self.mnu_ventanas.addAction(self.mni_cuadricula)
        self.mnu_ventanas.addAction(self.mni_subventanas)
        self.mbr_principal.addAction(self.mnu_ventanas.menuAction())

        self.retranslateUi(ContenedorVentanas)
        QtCore.QMetaObject.connectSlotsByName(ContenedorVentanas)

    def retranslateUi(self, ContenedorVentanas):
        _translate = QtCore.QCoreApplication.translate
        ContenedorVentanas.setWindowTitle(_translate("ContenedorVentanas", "Contenedor Ventanas (MDI)"))
        self.wdg_primera_ventana.setWindowTitle(_translate("ContenedorVentanas", "Subwindow"))
        self.lbl_primera_ventana.setText(_translate("ContenedorVentanas", "Primera ventana"))
        self.wdg_segunda_ventana.setWindowTitle(_translate("ContenedorVentanas", "Subwindow"))
        self.lbl_segunda_ventana.setText(_translate("ContenedorVentanas", "Segunda ventana"))
        self.mnu_ventanas.setTitle(_translate("ContenedorVentanas", "Ventanas"))
        self.mni_tabs.setText(_translate("ContenedorVentanas", "Pestañas"))
        self.mni_cascada.setText(_translate("ContenedorVentanas", "Cascada"))
        self.mni_cuadricula.setText(_translate("ContenedorVentanas", "Cuadrícula"))
        self.mni_subventanas.setText(_translate("ContenedorVentanas", "Subventanas"))
