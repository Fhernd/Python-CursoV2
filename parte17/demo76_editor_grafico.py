# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo76_editor_grafico.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditorGrafico(object):
    def setupUi(self, EditorGrafico):
        EditorGrafico.setObjectName("EditorGrafico")
        EditorGrafico.resize(480, 400)
        EditorGrafico.setMinimumSize(QtCore.QSize(480, 400))
        EditorGrafico.setMaximumSize(QtCore.QSize(480, 400))
        self.wdg_principal = QtWidgets.QWidget(EditorGrafico)
        self.wdg_principal.setObjectName("wdg_principal")
        EditorGrafico.setCentralWidget(self.wdg_principal)
        self.mbr_principal = QtWidgets.QMenuBar(EditorGrafico)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.mbr_principal.setObjectName("mbr_principal")
        self.mnu_dibujar = QtWidgets.QMenu(self.mbr_principal)
        self.mnu_dibujar.setObjectName("mnu_dibujar")
        self.mnu_ayuda = QtWidgets.QMenu(self.mbr_principal)
        self.mnu_ayuda.setObjectName("mnu_ayuda")
        EditorGrafico.setMenuBar(self.mbr_principal)
        self.stt_principal = QtWidgets.QStatusBar(EditorGrafico)
        self.stt_principal.setObjectName("stt_principal")
        EditorGrafico.setStatusBar(self.stt_principal)
        self.mni_circulo = QtWidgets.QAction(EditorGrafico)
        self.mni_circulo.setObjectName("mni_circulo")
        self.mni_rectangulo = QtWidgets.QAction(EditorGrafico)
        self.mni_rectangulo.setObjectName("mni_rectangulo")
        self.mni_linea = QtWidgets.QAction(EditorGrafico)
        self.mni_linea.setObjectName("mni_linea")
        self.mni_acerca_de = QtWidgets.QAction(EditorGrafico)
        self.mni_acerca_de.setObjectName("mni_acerca_de")
        self.mnu_dibujar.addAction(self.mni_circulo)
        self.mnu_dibujar.addAction(self.mni_rectangulo)
        self.mnu_dibujar.addAction(self.mni_linea)
        self.mnu_ayuda.addAction(self.mni_acerca_de)
        self.mbr_principal.addAction(self.mnu_dibujar.menuAction())
        self.mbr_principal.addAction(self.mnu_ayuda.menuAction())

        self.retranslateUi(EditorGrafico)
        QtCore.QMetaObject.connectSlotsByName(EditorGrafico)

    def retranslateUi(self, EditorGrafico):
        _translate = QtCore.QCoreApplication.translate
        EditorGrafico.setWindowTitle(_translate("EditorGrafico", "Editor Gráfico"))
        self.mnu_dibujar.setTitle(_translate("EditorGrafico", "Dibujar"))
        self.mnu_ayuda.setTitle(_translate("EditorGrafico", "Ayuda"))
        self.mni_circulo.setText(_translate("EditorGrafico", "Círculo"))
        self.mni_circulo.setShortcut(_translate("EditorGrafico", "Ctrl+C"))
        self.mni_rectangulo.setText(_translate("EditorGrafico", "Rectángulo"))
        self.mni_rectangulo.setShortcut(_translate("EditorGrafico", "Ctrl+R"))
        self.mni_linea.setText(_translate("EditorGrafico", "Línea"))
        self.mni_linea.setShortcut(_translate("EditorGrafico", "Ctrl+L"))
        self.mni_acerca_de.setText(_translate("EditorGrafico", "Acerca de..."))
