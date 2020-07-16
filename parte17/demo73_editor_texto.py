# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo73_editor_texto.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditorTexto(object):
    def setupUi(self, EditorTexto):
        EditorTexto.setObjectName("EditorTexto")
        EditorTexto.resize(480, 350)
        EditorTexto.setMinimumSize(QtCore.QSize(480, 350))
        EditorTexto.setMaximumSize(QtCore.QSize(480, 350))
        self.wdg_principal = QtWidgets.QWidget(EditorTexto)
        self.wdg_principal.setObjectName("wdg_principal")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.wdg_principal)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(4, 1, 471, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(0, 0, 0, 0)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.txt_contenido = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.txt_contenido.setObjectName("txt_contenido")
        self.lay_ver_principal.addWidget(self.txt_contenido)
        EditorTexto.setCentralWidget(self.wdg_principal)
        self.mbr_principal = QtWidgets.QMenuBar(EditorTexto)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.mbr_principal.setObjectName("mbr_principal")
        self.mnu_archivo = QtWidgets.QMenu(self.mbr_principal)
        self.mnu_archivo.setObjectName("mnu_archivo")
        self.mnu_ayuda = QtWidgets.QMenu(self.mbr_principal)
        self.mnu_ayuda.setObjectName("mnu_ayuda")
        EditorTexto.setMenuBar(self.mbr_principal)
        self.stt_principal = QtWidgets.QStatusBar(EditorTexto)
        self.stt_principal.setObjectName("stt_principal")
        EditorTexto.setStatusBar(self.stt_principal)
        self.mni_abrir = QtWidgets.QAction(EditorTexto)
        self.mni_abrir.setObjectName("mni_abrir")
        self.mni_guardar = QtWidgets.QAction(EditorTexto)
        self.mni_guardar.setObjectName("mni_guardar")
        self.mni_salir = QtWidgets.QAction(EditorTexto)
        self.mni_salir.setObjectName("mni_salir")
        self.mni_acerca_de = QtWidgets.QAction(EditorTexto)
        self.mni_acerca_de.setObjectName("mni_acerca_de")
        self.mnu_archivo.addAction(self.mni_abrir)
        self.mnu_archivo.addAction(self.mni_guardar)
        self.mnu_archivo.addSeparator()
        self.mnu_archivo.addAction(self.mni_salir)
        self.mnu_ayuda.addAction(self.mni_acerca_de)
        self.mbr_principal.addAction(self.mnu_archivo.menuAction())
        self.mbr_principal.addAction(self.mnu_ayuda.menuAction())

        self.retranslateUi(EditorTexto)
        QtCore.QMetaObject.connectSlotsByName(EditorTexto)

    def retranslateUi(self, EditorTexto):
        _translate = QtCore.QCoreApplication.translate
        EditorTexto.setWindowTitle(_translate("EditorTexto", "Editor Texto"))
        self.mnu_archivo.setTitle(_translate("EditorTexto", "Archivo"))
        self.mnu_ayuda.setTitle(_translate("EditorTexto", "Ayuda"))
        self.mni_abrir.setText(_translate("EditorTexto", "Abrir..."))
        self.mni_abrir.setShortcut(_translate("EditorTexto", "Ctrl+O"))
        self.mni_guardar.setText(_translate("EditorTexto", "Guardar..."))
        self.mni_guardar.setShortcut(_translate("EditorTexto", "Ctrl+G"))
        self.mni_salir.setText(_translate("EditorTexto", "Salir"))
        self.mni_salir.setShortcut(_translate("EditorTexto", "Ctrl+Q"))
        self.mni_acerca_de.setText(_translate("EditorTexto", "Acerca de..."))
